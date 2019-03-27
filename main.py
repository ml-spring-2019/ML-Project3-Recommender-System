import sys
import pdb
import re

NUMBER_OF_JOKES = 100
UNRATED = 99.0

def main(argv, argc):
    if argv < 3:
        print("Usage: python main.py <jester-data>")
        exit(1)

    data = fileIO(argv)
    meanNormalization(data)

    pdb.set_trace()


def fileIO(argv):
    print("-> fileIO()")
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


def isUnrated(rating):
    return rating == UNRATED


def meanNormalization(data):
    print("-> meanNormalization()")

    jokeRatingTotal = 0.0
    jokeRatingAverage = 0.0

    for joke in range(0, NUMBER_OF_JOKES):

        jokeRatingCount = 0.0
        jokeRatingTotal = 0.0
        jokeRatingAverage = 0.0

        for d in data:
            rating = d["ratings"][joke]
            if not isUnrated(rating):
                jokeRatingTotal += rating
                jokeRatingCount += 1

        jokeRatingAverage = jokeRatingTotal / jokeRatingCount

        for i in range(0, len(data)):
            rating = data[i]["ratings"][joke]
            if not isUnrated(rating):
                data[i]["ratings"][joke] -= jokeRatingAverage

if __name__ == "__main__":
    main(sys.argv, len(sys.argv))