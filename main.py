from jsonMod import json as json

def main():
    with open("test.json", "r") as jsonFile:
        jsonObj = json.getJsonObj(jsonFile.read())
        print(json.stringify(jsonObj))

if __name__ == "__main__":
    main()
