from typing import Any

def removeObj(stringIn: str)-> tuple[(dict[str,Any]), str]:
    tempJsonObj = {}
    stringIn = removeWhiteSpace(stringIn)
    if stringIn.startswith("{"):
        stringIn = stringIn[1:]
        stringIn = removeWhiteSpace(stringIn)
        if stringIn.startswith("}"):
            stringIn = stringIn[1:]
            return tempJsonObj, stringIn
        while True:
            stringIn = removeWhiteSpace(stringIn)
            tempName, stringIn = removeString(stringIn)
            stringIn = removeWhiteSpace(stringIn)
            if stringIn.startswith(":"):
                stringIn = stringIn[1:]
                tempVal, stringIn = removeValue(stringIn)
                tempJsonObj[str(tempName)] = tempVal
            stringIn = removeWhiteSpace(stringIn)
            if stringIn.startswith(","):
                stringIn = stringIn[1:]
                continue
            elif stringIn.startswith("}"):
                stringIn = stringIn[1:]
                break
            else:
                raise Exception("can't continue json-object:\n"+stringIn[:100])
    return tempJsonObj, stringIn

def removeArray(stringIn: str)-> tuple[(list[Any]), str]:
    tempJsonArray = []
    if stringIn.startswith("["):
        stringIn = stringIn[1:]
        stringIn = removeWhiteSpace(stringIn)
        if stringIn.startswith("]"):
            stringIn = stringIn[1:]
            return tempJsonArray, stringIn
        while True:
            valueRes, stringIn = removeValue(stringIn)
            tempJsonArray.append(valueRes)
            stringIn = removeWhiteSpace(stringIn)
            if stringIn.startswith(","):
                stringIn = stringIn[1:]
                continue
            elif stringIn.startswith("]"):
                return tempJsonArray, stringIn[1:]
            else:
                raise Exception("can't continue json-array:\n"+stringIn[:100])
    return tempJsonArray, stringIn

def removeValue(stringIn: str)-> tuple[Any, str]:
    stringIn = removeWhiteSpace(stringIn)
    if stringIn.startswith("true"):
        #print("true")
        stringIn = stringIn[4:]
        return True, stringIn
    elif stringIn.startswith("false"):
        #print("false")
        stringIn = stringIn[5:]
        return False, stringIn
    elif stringIn.startswith("null"):
        #print("null")
        stringIn = stringIn[4:]
        return None, stringIn
    else:
        tempJsonObj, readObjString = removeObj(stringIn)
        if readObjString != stringIn:
            #print("Obj")
            return tempJsonObj, readObjString
            #return readObjString

        tempJsonArray, readArrayString = removeArray(stringIn)
        if readArrayString != stringIn:
            #print("Array")
            return tempJsonArray, readArrayString
            #return readArrayString

        numRes, readNumString = removeNumber(stringIn)
        if readNumString != stringIn:
            #print("Number")
            return numRes, readNumString
            #return readNumString

        stringRes, readStringString = removeString(stringIn)
        if readStringString != stringIn:
            #print("String")
            return stringRes, readStringString
            #return readStringString

    stringIn = removeWhiteSpace(stringIn)
    raise Exception("can't continue json-value:\n", stringIn[:100])
    return 0,stringIn

def removeWhiteSpace(stringIn: str)-> str:
    while True:
        if stringIn.startswith(" ") or \
           stringIn.startswith("\t") or \
           stringIn.startswith("\n") or \
           stringIn.startswith("\r"):
               stringIn = stringIn[1:]
        else:
            break
    return stringIn

def removeString(stringIn: str)-> tuple[str, str]:
    if stringIn.startswith("\""):
        stringIn = stringIn[1:]
        readString = ""
        while len(stringIn) > 0:
            if stringIn.startswith("\""):
                stringIn = stringIn[1:]
                break
            if stringIn.startswith("\\u") and len(stringIn) >= 6:
                readString += stringIn[:6]
                stringIn = stringIn[6:]
                continue
            if stringIn.startswith("\\") and \
                    len(stringIn) >= 2 and\
                    stringIn[1] in ["\"","\\","/","b","f","n","r","t"]:
                readString += stringIn[:2]
                stringIn = stringIn[2:]
                continue
            readString += stringIn[0]
            stringIn = stringIn[1:]
        return readString, stringIn
    else:
        return "", stringIn
    return "", stringIn

def removeNumber(stringIn: str)-> tuple[(int|float), str]:
    originalString = stringIn
    numString = ""

    #sign
    if stringIn.startswith("-"):
            numString += "-"
            stringIn = stringIn[1:]

    while len(stringIn) > 0 and ord(stringIn[0]) >= 48 and ord(stringIn[0]) <= 57:
        numString += stringIn[0]
        stringIn = stringIn[1:]
    if (numString.startswith("0") and int(numString) != 0) or (numString == "-" or numString == ""):
        return -1, originalString

    #decimal
    if stringIn.startswith("."):
        numString += stringIn[0]
        stringIn = stringIn[1:]

    #rest after deciaml
    while len(stringIn) > 0 and ord(stringIn[0]) >= 48 and ord(stringIn[0]) <= 57:
        numString += stringIn[0]
        stringIn = stringIn[1:]
    #check if no new numbers
    if numString.endswith("."):
        return -1, numString+stringIn

    if stringIn.startswith("e") or stringIn.startswith("E"):
        numString += stringIn[0]
        stringIn = stringIn[1:]
        if stringIn.startswith("-") or stringIn.startswith("+"):
            numString += stringIn[0]
            stringIn = stringIn[1:]
        while len(stringIn) > 0 and ord(stringIn[0]) >= 48 and ord(stringIn[0]) <= 57:
            numString += stringIn[0]
            stringIn = stringIn[1:]
        if numString.endswith("e") or numString.endswith("E"):
            return -1, numString+stringIn
    if "." in numString or "e" in numString.lower():
        return float(numString), stringIn
    else:
        return int(numString), stringIn

def getJsonObj(inputString: str):
    jsonObj, testString = removeValue(inputString)
    if len(removeWhiteSpace(testString)) != 0:
        raise Exception("unable to parse rest:\n"+testString)
    return jsonObj

def stringify(jsonInput)->str:
    if isinstance(jsonInput, str):
        return f"\"{jsonInput}\""
    elif isinstance(jsonInput, bool):
        return str(jsonInput).lower()
    elif isinstance(jsonInput, int) or isinstance(jsonInput, float):
        return str(jsonInput)
    elif jsonInput == None:
        return "null"
    elif isinstance(jsonInput, dict):
        jsonStrings = []
        for key,val in jsonInput.items():
            jsonStrings.append(f"\"{key}\":{stringify(val)}")
        return "{"+','.join(jsonStrings)+"}"
    elif isinstance(jsonInput, list):
        jsonStrings = []
        for val in jsonInput:
            jsonStrings.append(stringify(val))
        return "["+','.join(jsonStrings)+"]"
    raise Exception("unable to stringify:\n"+jsonInput)
