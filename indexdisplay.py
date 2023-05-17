import argparse


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
        parser.add_argument("input_map", help="Input map of values for exercise")
        args = parser.parse_args()
        self.inputList = args.input_list.strip('][').split(",")
        self.inputDict = eval(args.input_map)
        self.outputList = []
        for x in self.inputList:
            try:
                if self.inputDict[int(x)]:
                    self.outputList.append(self.inputDict[int(x)])
            except KeyError:
                self.outputList.append(int(x))
        print(f"Your list with substitutions is: {self.outputList}")


if __name__ == '__main__':
    indexDisplay = IndexDisplay()
    # indexDisplay.getlist()
    # indexDisplay.getdict()
    indexDisplay.process()
