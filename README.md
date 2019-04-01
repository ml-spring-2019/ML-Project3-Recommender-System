# Project 3 - Recommender System
## Quick Start
To run the program, type:
```bash
> python main.py <jester-data> [plot-output-filename]
```

`main.py` takes in the following parameters:
- `jester-data` - training data
- `output-filename` (optional) - filename for the output plot. File extension must be provided. Default name: `cf_results.png`

#### Examples

No output filename:
```bash
> python main.py data/jester-data-1.csv
``` 

With output filename:
```bash
> python main.py data/jester-data-2.csv my_plot.png
```  

## Data Files Format 
- Data files are `.csv` type.
- Each row represents a single user.
- The first column gives the number of jokes rated by that user.
- The next 100 columns give the ratings for jokes 1 - 100.
- Ratings are `float` type from `-10.0` to `10.0`.
- Ratings containing `99.0` represent an unvoted (null rated) joke.

## Configuration File
Configurations may be changed at: `config.json`.
The following may be modified:
- `alpha` - variable used in the collaborative filtering algorithm.
- `lambda` - variable used in the collaborative filtering algorithm.
- `number_of_jokes` - the number of jokes for the entire dataset.
- `unrated_representation` - the number used to represent an unrated joke.
- `number_of_features` - the number of features to generate.
- `iterations_to_run` - the number of iterations to run.

## References

Jester Datasets: http://eigentaste.berkeley.edu/dataset/
