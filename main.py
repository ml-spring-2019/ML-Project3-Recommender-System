'''
    features: 2d numpy array
    row - feature scores
    column - joke features
    
    preferences: 2d numpy array
    row - preference scores
    column - user preferences
    
    ratings: 2d numpy array
    row - user ratings
    column - joke ratings
'''

import sys
import pdb
import re
import random
import numpy as np
import json
from matplotlib import pyplot

NUMBER_OF_JOKES = 100
UNRATED = 99.0
FEATURE_COUNT = 5
CONFIG_FILE = "config.json"

def main(argv, argc):
    if argc < 2:
        print("Usage: python main.py <jester-data>")
        exit(1)

    cf_lambda, cf_alpha = config_read()

    ratings, answeredCount = fileIO(argv)
    # meanNormalization(ratings)

    features = np.asarray(init_data(NUMBER_OF_JOKES, FEATURE_COUNT))
    prefs = np.asarray(init_data(FEATURE_COUNT, len(ratings)))

    # collaborativeFilteringAlgorithm(features, prefs, np.asarray(ratings))

    example_results = [1.1, 3.3, 6.6, 3.8, 5.2, 1.9, 0.7]
    plotResults(example_results)
    pdb.set_trace()

#   row - i
#   column - k
#   FEATURE_COUNT
#
# need function for regularized gradient descent for the theta and x values
def collaborativeFilteringAlgorithm(features, prefs, ratings):
    feature_dimensions = np.shape(features)
    prefs_dimensions = np.shape(prefs)
    transposed_prefs = np.transpose(prefs)
    
    for i in range(feature_dimensions[1]):
        for f in range(prefs_dimensions[1]):
            pdb.set_trace()
            predicted_rating = np.matmul(transposed_prefs[f,:],features[:,i])
            error_rate = predicted_rating - 
    return

def config_read():
    print("-> config_read()")
    configFile = json.loads(open(CONFIG_FILE, 'r').read())
    return configFile["lambda"], configFile["alpha"]


def init_data(rows, cols):
    print("-> init_data(rows=" + str(rows) + ", cols=" + str(cols) + ")")
    features = []
    for _ in range(0, rows):
        tempFeatures = []
        for _ in range(0, cols):
            # random number between -1.0 and 1.0 inclusive
            randomNum = round(float(random.randint(0, 200)) / 100 - 1, 2)
            tempFeatures.append(randomNum)
        features.append(tempFeatures)
    return features


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

def plotResults(squaredErrorRateList):
    plotList = []

    xLabel = "Iterations"
    yLabel = "Squared Error Rate"
    plotTitle = "Squared Error Rate Change per Iteration"
    showGrid = True
    outputFile = "cf_results.png"

    for i in range(1, len(squaredErrorRateList)):
        plotList.extend([i, squaredErrorRateList[i]])

    pyplot.plot(plotList)
    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)
    pyplot.title(plotTitle)
    pyplot.grid(showGrid)
    pyplot.savefig(outputFile)

if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
