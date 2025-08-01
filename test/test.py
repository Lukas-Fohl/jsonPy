from jsonMod import json as json

from enum import Enum

class testType(Enum):
    stringify = 1
    jsonConv = 2

class testAssertion:
    def __init__(self, inputJson, outputJson, testTypeIn):
        self.inputJson = inputJson
        self.outputJson = outputJson
        self.testType = testTypeIn

    def checkJsonConv(self) -> bool:
        res = json.getJsonObj(self.inputJson)
        if res == self.outputJson and type(self.outputJson) == type(res):
            self.printSuccess()
            return True
        self.printError()
        print("input:")
        print(self.inputJson)
        print("expected output:")
        print(self.outputJson)
        print("real output:")
        print(res)
        if type(self.outputJson) != type(res):
            print("wrong type:")
            print(f"wanted: {type(self.outputJson)}, got: {type(res)}")
        return False

    def checkStringify(self) -> bool:
        res = json.stringify(json.getJsonObj(self.inputJson))
        if res == self.outputJson:
            self.printSuccess()
            return True
        self.printError()
        print("input:")
        print(self.inputJson)
        print("expected output:")
        print(self.outputJson)
        print("real output:")
        print(res)
        return False

    def printError(self):
        print("\033[91merror\033[0m")
        return

    def printSuccess(self):
        print("\033[92mok\033[0m")
        return

tests: list[testAssertion] = [
    testAssertion("5", 5, testType.jsonConv),
    testAssertion("0", 0, testType.jsonConv),
    testAssertion("0.0", 0.0, testType.jsonConv),
    testAssertion("-0", 0, testType.jsonConv),
    testAssertion("-0.0", 0.0, testType.jsonConv),
    testAssertion("5.8", 5.8, testType.jsonConv),
    testAssertion("5.8E1", 58.0, testType.jsonConv),
    testAssertion("5.8E-1", 0.58, testType.jsonConv),
    testAssertion("5.8e-1", 0.58, testType.jsonConv),
    testAssertion("5.8E+1", 58.0, testType.jsonConv),
    testAssertion("5.8e+1", 58.0, testType.jsonConv),
    testAssertion("\"test\"", "test", testType.jsonConv),
    testAssertion("\"te\\\"st\"", "te\\\"st", testType.jsonConv),
    testAssertion("{\"a\":5}", {"a":5}, testType.jsonConv),
    testAssertion("{\"a\":{\"a\":5}}", {"a":{"a":5}}, testType.jsonConv),
    testAssertion("{\"a\":{\"a\":5}}", "{\"a\":{\"a\":5}}", testType.stringify),
    testAssertion("5.0", "5.0", testType.stringify),
    testAssertion("\"test\"", "\"test\"", testType.stringify),

    testAssertion("true", True, testType.jsonConv),
    testAssertion("false", False, testType.jsonConv),
    testAssertion("null", None, testType.jsonConv),
    testAssertion("[1, 2, 3]", [1, 2, 3], testType.jsonConv),
    testAssertion("[true, false, null]", [True, False, None], testType.jsonConv),
    testAssertion("{\"arr\": [1, 2, 3]}", {"arr": [1, 2, 3]}, testType.jsonConv),
    testAssertion("{\"nested\": {\"a\": [1, {\"b\": 2}]}}", {"nested": {"a": [1, {"b": 2}]}}, testType.jsonConv),
    testAssertion("  { \"a\" : 1 , \"b\" : [ 2 , 3 ] }  ", {"a": 1, "b": [2, 3]}, testType.jsonConv),
    testAssertion("\"line\\nbreak\"", "line\\nbreak", testType.jsonConv),
    testAssertion("\"tab\\tchar\"", "tab\\tchar", testType.jsonConv),
    testAssertion("[]", [], testType.jsonConv),
    testAssertion("{}", {}, testType.jsonConv),
    testAssertion("[{\"a\":1}, {\"b\":2}]", [{"a":1}, {"b":2}], testType.jsonConv),
    testAssertion("[1]", [1], testType.jsonConv),
    testAssertion("\"\"", "", testType.jsonConv),
    testAssertion("\"\\\\\"", "\\\\", testType.jsonConv),
    testAssertion("[1,2,3]", "[1,2,3]", testType.stringify),
    testAssertion("{\"a\":true}", "{\"a\":true}", testType.stringify),
    testAssertion("null", "null", testType.stringify),
    testAssertion("false", "false", testType.stringify),
    testAssertion("true", "true", testType.stringify),
    testAssertion("[true, false, null]", "[true,false,null]", testType.stringify),
]

def runTests():
    counter = 0
    for test in tests:
        if test.testType == testType.jsonConv:
            if not test.checkJsonConv():
                continue
        elif test.testType == testType.stringify:
            if not test.checkStringify():
                continue
        counter += 1
    print(f"[{counter}/{len(tests)}]")
    return

if __name__ == "__main__":
    runTests()
