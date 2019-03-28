import sys
import pdb
import re

NUMBER_OF_JOKES = 100
UNRATED = 99.0

def main(argv, argc):
    if argc < 2:
        print("Usage: python main.py <jester-data>")
        exit(1)

    ratings, answeredCount = fileIO(argv)
    # meanNormalization(ratings)

    for i in range(0, len(ratings)):
        pdb.set_trace()


def fileIO(argv):
    print("-> fileIO()")
    DATA_FILE = 1
    ratings = []
    file = open(argv[DATA_FILE], 'r')
    answeredCount = []
    for line in file.readlines():
        splitLine = line.split(",")
        answeredCount.append(str(re.sub('[!\xef\xbb\xbf]', '', splitLine[0])))
        tempList = []
        for i in range(1, len(splitLine)):
            tempList.append(float(splitLine[i]))
        ratings.append(tempList)
    return ratings, answeredCount


def isUnrated(rating):
    return rating == UNRATED


def meanNormalization(ratings):
    print("-> meanNormalization()")

    for joke in range(0, NUMBER_OF_JOKES):

        jokeRatingCount = 0.0
        jokeRatingTotal = 0.0

        for d in ratings:
            rating = d[joke]
            if not isUnrated(rating):
                jokeRatingTotal += rating
                jokeRatingCount += 1

        jokeRatingAverage = jokeRatingTotal / jokeRatingCount

        for i in range(0, len(ratings)):
            rating = ratings[i][joke]
            if not isUnrated(rating):
                ratings[i][joke] -= jokeRatingAverage





if __name__ == "__main__":
    main(sys.argv, len(sys.argv))