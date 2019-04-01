import sys
from matplotlib import pyplot

def main(argv, argc):
    if (argc < 2):
        print("Usage: python plot.py <datafile> [plot-output-filename]")
        return 1

    file = open(argv[1], "r")
    error_rates = []
    for f in file:
        error_rates.append(float(f))

    if argc == 3:
        plotResults(error_rates, argv[2])
    else:
        plotResults(error_rates)


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