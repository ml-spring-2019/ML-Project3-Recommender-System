import sys
import pdb

def main(argv, argc):
    CITY_FILE = 1
    FEATURES_FILE = 2

    if argv < 3:
        print("Usage: python main.py <city-file> <features-file>")
        exit(1)

    cityFile = open(argv[CITY_FILE], 'r')
    featuresFile = open(argv[FEATURES_FILE], 'r')

    featuresDict = {}
    for l in featuresFile.readlines():
        line = l.split()
        id = int(l[:3])
        classification = l[4:]
        pdb.set_trace()

        featuresDict[id] = line[classification]






if __name__ == "__main__":
    main(sys.argv, len(sys.argv))