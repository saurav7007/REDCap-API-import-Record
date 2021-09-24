# Importing the necessary packages
import pandas as pd, config, requests, hashlib, json, os


# Stroring the path where the csv file is stored and uploading the file
try:
    path = input('Enter the full path of the csv file: ')
    #/home/newuser/Desktop/BackUP_Uploaded_data_for_testing_ROW_BANKCF.csv
    #/home/newuser/Desktop//Update_New_Record_Upload_ARESTCFSSMCRIOpenSpecimenTest_ImportTemplate_2021-09-20.csv
except Exception as e1:
    print(str(e1))

try:
    api_token = input('Enter the api token: ')
    # BANK_CF : A410D356AFFEC0B8A2742EBC366784D2 , CF SS MCRI : 370670AAD1220B04EFDE62C152A9DD31
except Exception as e2:
    print(str(e2))
    
try:
    file = pd.read_csv(path)
except Exception as e3:
    print(str(e3))
 
    
# Converting all nan values to enpty string
try:
    file = file.fillna('')
except Exception as e4:
    print(str(e4))


# Creating a empty list to store all records from csv file
records = []


# Appending each record into the list variable records
try:
    for record_index in range(len(file)):
        try:
            record = file.iloc[record_index,:].to_dict()
        except Exception as e6:
            print(str(e6))
        try:
            records.append(record)
        except Exception as e7:
            print(str(e7))
except Exception as e5:
    print(str(e5))


# Converting json object into string
try:
    data = json.dumps(records)
except Exception as e8:
    print(str(e8))


# Importing the data via REDCap API
try:
    fields = {
        'token': api_token,
        'content': 'record',
        'action': 'import',
        'format': 'json',
        'type': 'flat',
        'overwriteBehavior': 'normal',
        'forceAutoNumber': 'false',
        'data': data,
        'returnContent': 'count',
        'returnFormat': 'json'
        }
except Exception as e9:
    print(str(e9))

try:
    r = requests.post('https://redcap.telethonkids.org.au/redcap/api/',data=fields)
except Exception as e10:
    print(str(e10))
 
    
# Creating a default dictionary for API responses:
try:
    api_response_detail = {200: 'OK: Success!',
                           400: 'Bad Request: The request was invalid. An accompanying message will explain why.',
                           401: 'Unauthorized: API token was missing or incorrect.',
                           403: 'Forbidden: You do not have permissions to use the API.',
                           404: 'Not Found: The URI you requested is invalid or the resource does not exist.',
                           406: 'Not Acceptable: The data being imported was formatted incorrectly.',
                           500: 'Internal Server Error: The server encountered an error processing your request.',
                           501: 'Not Implemented: The requested method is not implemented.'
                           }
except Exception as e11:
    print(str(e11))
    
    
# Printing the HTTP status for the API request
print('HTTP Status: ' + str(r.status_code) + '- ' + str(api_response_detail[r.status_code]))

# Printing the count of the records imported sucessfully
print('The number of records that are succussfully recorded are : ' + str(r.json()))


