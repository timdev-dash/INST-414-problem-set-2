'''
You will run this problem set from main.py, so set things up accordingly
'''

import pandas as pd
from part1_etl import etl
from part2_preprocessing import preprocess
from part3_logistic_regression import regression
from part4_decision_tree import decision
from part5_calibration_plot import calibration


# Call functions / instanciate objects from the .py files
def main():

    # PART 1: Instanciate etl, saving the two datasets in `./data/`
    etl()
    # PART 2: Call functions/instanciate objects from preprocessing
    preprocess()
    # PART 3: Call functions/instanciate objects from logistic_regression
    regression()
    # PART 4: Call functions/instanciate objects from decision_tree

    # PART 5: Call functions/instanciate objects from calibration_plot


if __name__ == "__main__":
    main()