import sys
import pdb
import re

NUMBER_OF_JOKES = 100
UNRATED = 99.0

def main(argv, argc):
    if argv < 3:
        print("Usage: python main.py <jester-data>")
        exit(1)

    data, jokeCountList = fileIO(argv)
    meanNormalization(data)


    pdb.set_trace()


def fileIO(argv):
    print("-> fileIO()")
    DATA_FILE = 1
    data = []
    file = open(argv[DATA_FILE], 'r')
    jokeCountlist = []
    for line in file.readlines():
        splitLine = line.split(",")
        jokeCountlist.append(str(re.sub('[!\xef\xbb\xbf]', '', splitLine[0])))
        tempList = []
        for i in range(1, len(splitLine)):
            tempList.append(float(splitLine[i]))
        data.append(tempList)
    return data, jokeCountlist


def isUnrated(rating):
    return rating == UNRATED


def meanNormalization(data):
    print("-> meanNormalization()")

    for joke in range(0, NUMBER_OF_JOKES):

        jokeRatingCount = 0.0
        jokeRatingTotal = 0.0

        for d in data:
            rating = d[joke]
            if not isUnrated(rating):
                jokeRatingTotal += rating
                jokeRatingCount += 1

        jokeRatingAverage = jokeRatingTotal / jokeRatingCount

        for i in range(0, len(data)):
            rating = data[i][joke]
            if not isUnrated(rating):
                data[i][joke] -= jokeRatingAverage

if __name__ == "__main__":
    main(sys.argv, len(sys.argv))