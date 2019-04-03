# Project 3 - Recommender System
## Quick Start
To run the program, type:
```bash
> python main.py <jester-data> [out-filename]
```

`main.py` takes in the following parameters:
- `jester-data` - training data
- `out-filename` (optional) - filename for the data output as `.csv`. If not provided, the default name will be used: `out.csv`

#### Examples

No output filename:
```bash
> python main.py data/jester-data-1.csv
``` 

With output filename:
```bash
> python main.py data/jester-data-2.csv data2-out.csv
```  

## Plotting Results
To generate a plot using `plot.py`, type:
```bash
> python plot.py <datafile> [plot-output-filename]
``` 
`plot.py` takes in the following parameters:
- `datafile` - the output file `main.py` produces.
- `plot-output-filename` (optional) - filename for the output plot (recommended to be `.png`). If not provided, the default name will be used: `results.png`

#### Examples

No output filename:
```bash
> python plot.py out.csv
``` 

With output filename:
```bash
> python plot.py data2-out.csv data2-out-results.png
``` 

## Data Files Format 
- Data input files are `.csv` type found in the `data/` directory.
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
- `unrated_representation` - the number used to represent an unrated joke.
- `iterations_to_run` - the number of iterations to run.

## References

Jester Datasets: http://eigentaste.berkeley.edu/dataset/
