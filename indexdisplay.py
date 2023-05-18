import argparse
import json


class IndexDisplay:
    def __init__(self):
        self.inputList = None
        self.inputDict = None

    def getlist(self):
        self.inputListString = input("Please enter a comma separated series of indexes you would like to see: ")
        self.inputList = self.inputListString.strip('][').split(",")

    def getdict(self):
        self.inputDictString = input("Please enter the dictionary or map you wish to use for this exercise: ")
        self.inputDict = eval(self.inputDictString)

    def process(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("input_list", help="Input list of indices you would like printed")
        parser.add_argument("input_file", help="Input name of json file")
        args = parser.parse_args()
        self.inputList = args.input_list.strip('][').split(",")
        # self.inputDict = eval(args.input_map)
        with open(args.input_file) as file:
            self.inputDict = json.load(file)
        outputList = []
        for x in self.inputList:
            try:
                if self.inputDict[x]:
                    print(self.inputDict[x])
                    outputList.append(self.inputDict[x])
            except KeyError:
                outputList.append(x)
        print(f"Your list with substitutions is: {outputList}")


if __name__ == '__main__':
    indexDisplay = IndexDisplay()
    # indexDisplay.getlist()
    # indexDisplay.getdict()
    indexDisplay.process()
