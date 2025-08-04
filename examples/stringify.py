
from jsonMod import json as json

def main():
    with open("./examples/test.json", "r") as file:
        jsonObj = json.getJsonObj(file.read())

        #print string
        print(json.stringify(jsonObj[0]["username"]))

        #print number
        print(json.stringify(jsonObj[0]["userId"]))

        #print bool
        print(json.stringify(jsonObj[0]["preferences"]["notifications"]["sms"]))
        
        #print object
        print(json.stringify(jsonObj[0]["profile"]))

        #print array
        print(json.stringify(jsonObj[0]["activityLogs"]))

    return

if __name__ == "__main__":
    main()
