##################################################
## this script will calculate BMI in bulk
## it will take input json file
##################################################
## Author: Satyam
## Version: 0.0.1
## Email: shivharesatyam1@gmail.com
## Status: development
##################################################


import json
import os
import pip
import sys

class style():
    '''Please ignore this class this is for the only color styling...'''
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def get_health_risk(bmi):
    '''let's assign the health risk according bmi'''
    if (bmi <= 18.4):
        return 'Malnutrition risk'
    elif (18.5 <= bmi <= 24.5):
        return 'Low risk'
    elif (25 <= bmi <= 29.9):
        return 'Enhanced risk'
    elif (30 <= bmi <= 34.9):
        return 'Medium risk'
    elif (35 <= bmi <= 39.9):
        return 'High risk'
    elif (40 <= bmi):
        return 'Very high risk'
    else:
        return ''

def get_category(bmi):
    '''let's assign the category according bmi'''
    if (bmi <= 18.4):
        return 'Under weight'
    elif (18.5 <= bmi <= 24.5):
        return 'Normal weight'
    elif (25 <= bmi <= 29.9):
        return 'Over weight'
    elif (30 <= bmi <= 34.9):
        return 'Moderately obese'
    elif (35 <= bmi <= 39.9):
        return 'Severely obese'
    elif (40 <= bmi):
        return 'Very severely obese'
    else:
        return ''

def process_data_method1(input_file):
    '''Process the data here I am avoiding the loop that for used the pandas'''
    import pandas as pd
    df = pd.read_json(input_file)
    df['BMI'] = df.apply(lambda x: x['WeightKg']/((x['HeightCm']/100)*(x['HeightCm']/100)), axis=1)
    df['Category'] = df.apply(lambda x: get_category(x['BMI']), axis=1)
    df['Health Risk'] = df.apply(lambda x: get_health_risk(x['BMI']), axis=1)

    df.to_json ('bmi_out.json', orient='records')

def check_packages():
    '''Lets verify the package and install the all missing package '''
    package = 'pandas'
    try:
        __import__(package)
        print(style.YELLOW + "###"*20)
        print(style.GREEN + "\n Dependencies 'pandas' is installed \n")
        print(style.YELLOW + "###"*20)
    except ImportError:
        print(style.YELLOW + "###"*20)
        print(style.RED + "\n Dependencies 'pandas' is not installed \n")
        print(style.GREEN + "\n Installing the all missing dependencies...\n")
        print(style.YELLOW + "###"*20)
        pip.main(['install', package])

    return True

'''Here is the some commented working code but this code will slow upto 10k entry this code will also work perfectly'''

# def calculate_bmi(weight, height):
#     return weight/(height*height)

# def process_data_method2(input_file):

    ## with open('input.json') as file:
    ##     loadData = json.load(file)
    ##     print(loadData)

    # df = pd.read_json(input_file)

    # for index, row in df.iterrows():
    #     result = {}
    #     heightMeter = row['HeightCm']/100
    #     bmi = calculate_bmi(row['WeightKg'], heightMeter)
    #     health_risk = get_health_risk(bmi)
    #     category = get_category(bmi)
    #     df.loc[index,'BMI'] = bmi
    #     df.loc[index,'Category'] = category
    #     df.loc[index,'Health Risk'] = health_risk
    
    # print(df)
    # df.to_json ('bmi_out.json', orient='records')

    
#MAIN
if __name__ == "__main__":
    #check the packages
    if check_packages():
        print(style.GREEN + "\n Dependencies scanning completed*** \n")

        input_file_path = str(input('Please give me the JSON input file name with full path (Absolute file path): '))
        if os.path.isfile(input_file_path) and 'json' in input_file_path:
            input_file = input_file_path
        else:
            print(style.RED + "\n*********   JSON Input file path is not correct, Please give me correct path   ************\n")
            sys.exit()

        if not input_file:
            input_file = "input.json"


        print(style.GREEN + "\n BMI Calculation inprogrss... \n")
        process_data_method1(input_file)
        print(style.GREEN + "\n\n All BMI is calculated your output is available inside dir: {} /bmi_out.json \n\n\n".format(str(os.getcwd())))

    else:
        print(style.RED + "Some problem is on dependencies.")

    # process_data_method2(input_file)