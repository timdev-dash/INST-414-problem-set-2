'''
You will run this problem set from main.py, so set things up accordingly
'''

import pandas as pd
from part1_etl import etl
from part2_preprocessing import preprocess
from part3_logistic_regression import regression
from part4_decision_tree import decision_tree
from part5_calibration_plot import calibration_plot


# Call functions / instanciate objects from the .py files
def main():

    # PART 1: Instanciate etl, saving the two datasets in `./data/`
    pred_universe_raw, arrest_events_raw = etl()
    # PART 2: Call functions/instanciate objects from preprocessing
    df_arrests: pd = preprocess(pred_universe_raw, arrest_events_raw)
    # PART 3: Call functions/instanciate objects from logistic_regression
    df_arrests_train, df_arrests_test_lr, subs_felony_train, subs_felony_test = regression(df_arrests)
    # PART 4: Call functions/instanciate objects from decision_tree
    df_arrests_test_dt:pd = decision_tree(df_arrests_train, df_arrests_test_lr, subs_felony_train)
    # PART 5: Call functions/instanciate objects from calibration_plot
    calibration_plot(df_arrests_test_lr['pred_lr'], subs_felony_test)
    calibration_plot(df_arrests_test_dt['pred_dt'], subs_felony_test)

    print('Based on the results of the calibration plot, the logistic regression is the more calibrated.')

if __name__ == "__main__":
    main()