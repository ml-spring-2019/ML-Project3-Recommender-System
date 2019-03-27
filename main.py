import sys
import pdb
import re

def main(argv, argc):
    UNRATED = 99.0

    if argv < 3:
        print("Usage: python main.py <jester-data>")
        exit(1)

    data = fileIO(argv)

    pdb.set_trace()


def fileIO(argv):
    DATA_FILE = 1
    data = []
    file = open(argv[DATA_FILE], 'r')
    for line in file.readlines():
        splitLine = line.split(",")
        tempDict = {}

        tempDict["rated_count"] = str(re.sub('[!\xef\xbb\xbf]', '', splitLine[0]))
        tempList = []
        for i in range(1, len(splitLine)):
            tempList.append(float(splitLine[i]))
        tempDict["ratings"] = tempList
        data.append(tempDict)
    return data


if __name__ == "__main__":
    main(sys.argv, len(sys.argv))