'''
You will run this problem set from main.py, so set things up accordingly
'''

import pandas as pd
from etl import etl
from preprocessing import preprocess
import logistic_regression
import decision_tree
import calibration_plot


# Call functions / instanciate objects from the .py files
def main():

    # PART 1: Instanciate etl, saving the two datasets in `./data/`
    etl()
    # PART 2: Call functions/instanciate objects from preprocessing
    preprocess()
    # PART 3: Call functions/instanciate objects from logistic_regression

    # PART 4: Call functions/instanciate objects from decision_tree

    # PART 5: Call functions/instanciate objects from calibration_plot


if __name__ == "__main__":
    main()