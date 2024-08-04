'''
PART 4: Decision Trees
x Read in the dataframe(s) from PART 3
x Create a parameter grid called `param_grid_dt` containing three values for tree depth. (Note C has to be greater than zero) 
x Initialize the Decision Tree model. Assign this to a variable called `dt_model`. 
x Initialize the GridSearchCV using the logistic regression model you initialized and parameter grid you created. Do 5 fold crossvalidation. Assign this to a variable called `gs_cv_dt`. 
x Run the model 
x What was the optimal value for max_depth?  Did it have the most or least regularization? Or in the middle? 
x Now predict for the test set. Name this column `pred_dt` 
x Return dataframe(s) for use in main.py for PART 5; if you can't figure this out, save as .csv('s) in `data/` and read into PART 5 in main.py
'''

# Standard library imports
from pathlib import Path 

# Third party imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import StratifiedKFold as KFold_strat
from sklearn.tree import DecisionTreeClassifier as DTC

# Local application imports
from file_manager import df_from_csv, csv_from_df

# Setting constants
MAIN_FOLDER: Path = Path(__file__).absolute().parent
DATA_PATH: str = '../data/'

# Fuction to complete decision tree
def decision_tree(df_arrests_train: pd, df_arrests_test: pd, subs_felony_train: pd):
    '''
    This function brings in data from prior parts, works through decision tree analysis to provide files for future analysis.

    Parameters
    df_arrests_train(Dataframe): Training dataframe of df_arrests features
    df_arrests_test(Dataframe): Testing dataframe of df_arrests features
    subs_felony_train(Dataframe): Training dataframe of df_arrests outcome
    '''

    # Create parameter grid for decision tree
    param_grid_dt: dict = {'max_depth' : [3, 5, 10]}

    # Initialize decision tree model
    dt_model: DTC = DTC()

    # Initialize GridSearchCV
    gs_cv_dt: GridSearchCV = GridSearchCV(dt_model, param_grid_dt, cv = 5)

    # Run the model
    model = gs_cv_dt.fit(df_arrests_train, subs_felony_train)

    # Assing best_depth
    best_depth: float = model.best_params_['max_depth']
    best_depth_index: int = param_grid_dt['max_depth'].index(best_depth)

    # What is the optimal value for max_depth?
    print(best_depth, 'is the best value for the hyperparameter "max_depth".')

    # Regualarization of max_depth
    if best_depth_index == 0:
        print('The best "max_depth" of', best_depth, 'had the least regularization of all options.')
    elif best_depth_index == len(param_grid_dt['max_depth']):
        print('The best "max_depth" of', best_depth, 'had the most regularization of all options.')
    else:
        print('The best "max_depth" of', best_depth, 'was in the middle of regularization of all options.')

    # Predict the test set
    df_arrests_dt_test: pd = df_arrests_test.drop(columns = ['pred_lr'])
    df_arrests_test['pred_dt'] = gs_cv_dt.predict(df_arrests_dt_test)

    # Return dataframe(s?)
    return df_arrests_test

# Script run control
if __name__ == "__main__":
    #decision_tree()
    pass