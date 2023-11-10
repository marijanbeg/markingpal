# markingpal

## About

Python package for helping in marking and feedback.

## How to run the demo?

Run the following steps:

```
$ git clone https://github.com/marijanbeg/markingpal.git
$ cd markingpal
$ conda env create -f environment.yml
$ conda activate markingpal
$ jupyter lab &
```

Run the demo in `demo.ipynb`.

## How to install?

``` bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
python3 -m pip install --upgrade -e .
```

Finally create the file `~/.markingpal/env` with the following content:

```bash
OPENAI_API_KEY=sk-XXXXXX
```
