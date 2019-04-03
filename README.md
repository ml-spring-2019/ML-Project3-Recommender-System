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
- `alpha` - variable used in the collaborative filtering algorithm. `0.0005` is used for the large jester datasets.
- `lambda` - variable used in the collaborative filtering algorithm. `0.0001` is used for the large jester datasets.
- `unrated_representation` - the number used to represent an unrated joke. This value should be `99.0`
- `iterations_to_run` - the number of iterations to run. At least `10` is recommended.

## Results
Results of running the large jester datasets can be found in the `results/` directory. 

The parameters used are:
- `alpha: 0.0005`
- `lambda: 0.0001`
- `unrated_representation: 99.0`
- `iterations_to_run: 100`

## References

Jester Datasets: http://eigentaste.berkeley.edu/dataset/
