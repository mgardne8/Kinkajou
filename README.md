# Kinkajou #
Kinkajou Is Not Kinkajou, Amazingly Just Outright Useless.
A ~~knockoff~~ unique and in no way not a parody of any well know animal based data library 😊

## Setup ##

### Quick Setup ###
run setup-environment.bat or setup-enviornment.sh to create kinkajou env and install package or see the following section for instructions on manual installation

### Manual Setup ###
 * Ensure Anaconda or Miniconda are installed (https://docs.conda.io/en/latest/miniconda.html )
 * Create Conda environment from env file
 * Install Kinkajou as local package

From the root directory:
```
Conda env create -n kinkajou -f environment.yml
conda env update -n kinkajou --file environment.yml --prune
pip install -e .
```

## Run ##
Activate kinkajou conda environment
```
conda activate kinkajou
```
Run scripts or notebooks from respective directories, or import kinkajou to your own scripts

### Quick Example ###
 * import kinkajou
 * load a csv file without headers
 * add 69 to all values in the second column
 * print all rows where column 2 < 80

```python
import kinkajou as kj

data = kj.cage_csv('./testdata.csv',has_header=False)

data.modify_column(1,(lambda x: x + 69))

for row in data.filter((lambda x: x[1] < 80))
    print(row) 

# output:
# ['row_01', 72, 'APPLE']
# ['row_07', 79, 'ORANGE']
# ['row_11', 70, 'DOG']
```
