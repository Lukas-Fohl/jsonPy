from jsonMod import json as json

def main():
    with open("./examples/titanic.json", "r") as file:
        jsonObj = json.getJsonObj(file.read())

        #get element from list
        print(jsonObj[0])

        #get value from object
        print(jsonObj[0]["Age"])
        print(jsonObj[0]["Name"])

        #check for null
        print(jsonObj[0]["Cabin"]==None)

        #iterate over list
        for element in jsonObj:
            if element["Age"] != None and element["Age"] >= 70:
                print(element["Name"])

        #iterate over object
        for name, element in jsonObj[0].items():
            print(f"{name}:{element}")

        #check if key is contained
        print("Age" in jsonObj[0])

    return

if __name__ == "__main__":
    main()
