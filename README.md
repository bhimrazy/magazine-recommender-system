# MAGAZINE RECOMMENDER SYSTEM

MAGAZINE RECOMMENDER SYSTEM.
Follow these commands to run the project.

## Setup

```shell
    # download data
    $ make data # it will download inside -> notebooks/data/

```

```shell
    #create a python environment
    $ python -m venv venv
    #activate environment
    $ source venv/bin/activate # use venv/Scripts/activate for windows
    #install packages from requirements.txt file
    $ pip install -r requirements.txt

    # Run app
    $ python src/main.py

    # Run test and coverage
    $ pytest
    $ coverage run -m pytest
    $ coverage report -i

    # Run flake8
    $ flake8

```
