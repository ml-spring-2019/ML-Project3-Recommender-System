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
CF_LAMBDA = 0
CF_ALPHA = 0

def main(argv, argc):
    if argc < 2:
        print("Usage: python main.py <jester-data> [plot-output-filename]")
        exit(1)

    global CF_ALPHA, CF_LAMBDA
    CF_LAMBDA, CF_ALPHA = config_read()

    ratings, answeredCount = fileIO(argv)
    # meanNormalization(ratings)

    features = np.asarray(init_data(FEATURE_COUNT, NUMBER_OF_JOKES))
    prefs = np.asarray(init_data(FEATURE_COUNT, len(ratings)))

    collaborativeFilteringAlgorithm(features, prefs, np.asarray(ratings))

    example_results = [1.1, 3.3, 6.6, 3.8, 5.2, 1.9, 0.7]
    if argc == 3:
        plotResults(example_results, argv[2])
    else:
        plotResults(example_results)
    pdb.set_trace()

#   row - i
#   column - k
#   FEATURE_COUNT
#
# need function for regularized gradient descent for the theta and x values

def findPredictedRatings(jokes_matrix, users_matrix):
    predictedRatings = np.matmul(np.transpose(users_matrix), jokes_matrix)
    return predictedRatings

def calculateCostFunction(jokes_matrix, users_matrix, ratings):
    predictedRatings = findPredictedRatings(jokes_matrix, users_matrix)
#   subtract predicted ratings by actual ratings
    difference = np.subtract(predictedRatings, ratings)
    errored_ratings = np.square(difference)
    error_rate = np.sum(errored_ratings)
    return error_rate

def regularized_gradient_descent(num_jokes, num_users, features, prefs, ratings):
    error_rate = 0
    
    itr = 0
    for k in range(FEATURE_COUNT):
        for i in range(num_jokes):
            # continual gradient descent for one cell
            previous_error_rate = 100
            while (True):
                itr += 1
                previously_optimized_feature = features[k][i]
                regularized_variable = CF_LAMBDA*features[k][i]
                gradient_descent_val = 0
                for j in range(num_users):
                    if ratings[j][i] != 99:
                        predicted_rating = np.dot(np.transpose(prefs[:,j]), features[:,i])
                        error_rate = (predicted_rating-ratings[j][i])
                        altered_error_rate = error_rate * prefs[k][j]
                        gradient_descent_val += altered_error_rate + regularized_variable
                        pdb.set_trace()
            
                if (error_rate**2 > previous_error_rate**2):
                    pdb.set_trace()
                    break
                features[k][i] = features[k][i] - (gradient_descent_val * CF_ALPHA)
#               print("error rate: ", error_rate, "feature: ", features[k][i])
#               print("gd: ", gradient_descent_val, "predicted rating: ", predicted_rating)
                
                previous_error_rate = error_rate
                
#   need to do the for loops for the preferences matrix
    return

def collaborativeFilteringAlgorithm(features, prefs, ratings):
    num_jokes = np.shape(features)[1]
    num_users = np.shape(prefs)[1]

    regularized_gradient_descent(num_jokes, num_users, features, prefs, ratings)
    
#   minimize features
#    features = regularized_gradient_descent(feature_dimensions[1], prefs_dimensions[1], features, prefs, ratings, "features")

#   minimize preferences
#    prefs = regularized_gradient_descent(feature_dimensions[1], prefs_dimensions[1], prefs, features, ratings, "preferences")

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

def plotResults(squaredErrorRateList, outputFilename="cf_results.png"):
    plotList = []

    xLabel = "Iterations"
    yLabel = "Squared Error Rate"
    plotTitle = "Squared Error Rate Change per Iteration"
    showGrid = True

    for i in range(1, len(squaredErrorRateList)):
        plotList.extend([i, squaredErrorRateList[i]])

    pyplot.plot(plotList)
    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)
    pyplot.title(plotTitle)
    pyplot.grid(showGrid)
    pyplot.savefig(outputFilename)
    print("Successfully exported plot to: " + outputFilename + ".")

if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
