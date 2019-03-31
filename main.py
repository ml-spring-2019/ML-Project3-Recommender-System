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

CONFIG_FILE = "config.json"
CF_LAMBDA = 0
CF_ALPHA = 0

ALPHA = 0.0
LAMBDA = 0.0
NUMBER_OF_JOKES = 0
NUMBER_OF_USERS = 0
UNRATED = 0.0
FEATURE_COUNT = 5
JOKE_RATING_MEAN = 0
GD_ITERATION = 0


def main(argv, argc):
    if argc < 2:
        print("Usage: python main.py <jester-data> [plot-output-filename]")
        exit(1)
#   ------------------------
    config_read()
#   read file
    ratings, answeredCount = fileIO(argv)
#   compute mean normalization
    rating_means = []
    meanNormalization(ratings, rating_means)
    features = np.asarray(init_data(FEATURE_COUNT, len(ratings[0])))
    prefs = np.asarray(init_data(FEATURE_COUNT, len(ratings)))
    global NUMBER_OF_JOKES, NUMBER_OF_USERS
    NUMBER_OF_JOKES, NUMBER_OF_USERS = np.shape(ratings)[1], np.shape(ratings)[0]
#   ------------------------
    error_rates = []
#   Calculate the sqaured error rates of each iteration of the collaborative filtering algorithm
    for i in range(GD_ITERATION):
        error_rates.append(collaborativeFilteringAlgorithm(features, prefs, np.asarray(ratings)))

#   Create graph of squared error rate change per iteration
    if argc == 3:
        plotResults(error_rates, argv[2])
    else:
        plotResults(error_rates)
    return 0


def findPredictedRatings(jokes_matrix, users_matrix):
    predictedRatings = np.matmul(np.transpose(users_matrix), jokes_matrix)
    return addJokeRatingMean(predictedRatings)

def addJokeRatingMean(rating_data):
    return JOKE_RATING_MEAN + rating_data

def calculateCostFunction(jokes_matrix, users_matrix, ratings):
    predictedRatings = findPredictedRatings(jokes_matrix, users_matrix)
#   subtract predicted ratings by actual ratings
#    difference = np.subtract(predictedRatings, ratings)
#    errored_ratings = np.square(difference)
#    error_rate = np.sum(errored_ratings)

    difference = predictedRatings
    ratings_range = np.shape(ratings)
    for i in range(ratings_range[0]):
        for j in range(ratings_range[1]):
            if ratings[i][j] < 95:
                difference [i][j] = difference[i][j] - ratings[i][j]

    error_ratings = np.where(difference < 95, difference**2, 99)

    total_error_rate = 0

    for error_rating_row in error_ratings:
        for error_rating in error_rating_row:
            if error_rating < 95:
                total_error_rate += error_rating
    return total_error_rate

def add(a, b):
    return a + b

def matrix_assignment(features, prefs, bool):
    if bool:
        return features, prefs
    return prefs, features

def regularized_gradient_descent(RANGE, features, prefs, bool, ratings):
    
    dependent_rating, independent_rating = matrix_assignment(features, prefs, bool)
    
    for i in range(RANGE):
        actual_ratings = ratings[i,:] if not bool else ratings[:,i]
        for k in range(FEATURE_COUNT):
            predicted_rating = np.matmul(np.transpose(independent_rating), dependent_rating[:,i])
            
#           error_rate = np.subtract(predicted_rating, actual_ratings)
            error_rate = np.where(actual_ratings<80, predicted_rating - actual_ratings, 99)
            
            for itr in range(np.shape(error_rate)[0]):
                if error_rate[itr] < 95:
                    error_rate[itr] = independent_rating[k][itr] * error_rate[itr]
            regularizing_val = LAMBDA*dependent_rating[k][i]
            gradient_descent_vector = np.where(error_rate != 99, regularizing_val + error_rate, error_rate)
            sum = 0
            for num in gradient_descent_vector:
                if num < 95:
                    sum += num
            gradient_descent_val = sum * ALPHA
            dependent_rating[k][i] = dependent_rating[k][i]-gradient_descent_val

    return dependent_rating

def collaborativeFilteringAlgorithm(features, prefs, ratings):
    num_jokes = np.shape(features)[1]
    num_users = np.shape(prefs)[1]
    feature_gd = True
    
#   minimize features
    features = regularized_gradient_descent(NUMBER_OF_JOKES, features, prefs, feature_gd, ratings)

#   minimize preferences
    prefs = regularized_gradient_descent(NUMBER_OF_USERS, features, prefs, not feature_gd, ratings)

#   find total error rate
    error_rate = calculateCostFunction(features, prefs, ratings)
    
    return error_rate

def config_read():
    global ALPHA, LAMBDA, NUMBER_OF_JOKES, UNRATED, FEATURE_COUNT, GD_ITERATION
    print("-> config_read()")
    configs = json.loads(open(CONFIG_FILE, 'r').read())
    ALPHA = float(configs["alpha"])
    LAMBDA = float(configs["lambda"])
#    NUMBER_OF_JOKES = int(configs["number_of_jokes"])
    UNRATED = float(configs["unrated_representation"])
    FEATURE_COUNT = int(configs["number_of_features"])
    GD_ITERATION = int(configs["iterations_to_run"])


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


def meanNormalization(ratings, rating_means):
    print("-> meanNormalization()")
    global JOKERATINGMEAN

    for joke in range(0, NUMBER_OF_JOKES):

        jokeRatingCount = 0.0
        jokeRatingTotal = 0.0

        for d in ratings:
            rating = d[joke]
            if not isUnrated(rating):
                jokeRatingTotal += rating
                jokeRatingCount += 1

        JOKE_RATING_MEAN = jokeRatingTotal / jokeRatingCount

        for i in range(0, len(ratings)):
            rating = ratings[i][joke]
            if not isUnrated(rating):
                ratings[i][joke] -= JOKE_RATING_MEAN
                rating_means.append(JOKE_RATING_MEAN)

def plotResults(squaredErrorRateList, outputFilename="results.png"):
    xLabel = "Iterations"
    yLabel = "Squared Error Rate"
    plotTitle = "Squared Error Rate Change per Iteration"
    showGrid = True

    pyplot.plot(squaredErrorRateList)
    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)
    pyplot.title(plotTitle)
    pyplot.grid(showGrid)
    pyplot.savefig(outputFilename)
    print("Successfully exported plot to: " + outputFilename + ".")

if __name__ == "__main__":
    main(sys.argv, len(sys.argv))








'''
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
    regularized_variable = LAMBDA*features[k][i]
    gradient_descent_val = 0
    for j in range(num_users):
    if ratings[j][i] != 99:
    predicted_rating = np.dot(np.transpose(prefs[:,j]), features[:,i])
    error_rate = (predicted_rating-ratings[j][i])
    altered_error_rate = error_rate * prefs[k][j]
    gradient_descent_val += altered_error_rate + regularized_variable
    pdb.set_trace()
    
    if (error_rate**2 > previous_error_rate**2):
    
    break
    features[k][i] = features[k][i] - (gradient_descent_val * ALPHA)
    
    
    previous_error_rate = error_rate
    
    #   need to do the for loops for the preferences matrix
    return
    '''
