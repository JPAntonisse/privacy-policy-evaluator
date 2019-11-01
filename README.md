# Privacy Policy Evaluator


## How to install
Make sure Anaconda is installed on your system.

Create the Environment for Privacy Policy Evaluator
```
conda env create -f environment.yml
```


## Activate Environment
To activate the environment
```sh
$ conda activate ./env
```

## Running Privacy Policy Evaluator
Before running the privacy policy evaluator, make sure to have run setup.py. There are some downloads from NLTK that needs to be completed on your system.
```
python setup.py
```
```
python ppe.py {args}
```


## Update environment
To update the environment if any changes are made
```
conda activate ./env
```
```
conda env update --file environment.yml
```
