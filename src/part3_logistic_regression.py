'''
PART 3: Logistic Regression
x Read in `df_arrests`
x Use train_test_split to create two dataframes from `df_arrests`, the first is called `df_arrests_train` and the second is called `df_arrests_test`. Set test_size to 0.3, shuffle to be True. Stratify by the outcome  
x Create a list called `features` which contains our two feature names: pred_universe, num_fel_arrests_last_year
x Create a parameter grid called `param_grid` containing three values for the C hyperparameter. (Note C has to be greater than zero) 
x Initialize the Logistic Regression model with a variable called `lr_model` 
x Initialize the GridSearchCV using the logistic regression model you initialized and parameter grid you created. Do 5 fold crossvalidation. Assign this to a variable called `gs_cv` 
x Run the model 
- What was the optimal value for C? Did it have the most or least regularization? Or in the middle? Print these questions and your answers. 
- Now predict for the test set. Name this column `pred_lr`
- Return dataframe(s) for use in main.py for PART 4 and PART 5; if you can't figure this out, save as .csv('s) in `data/` and read into PART 4 and PART 5 in main.py
'''

# Standard library imports
from pathlib import Path

# Third party imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import StratifiedKFold as KFold_strat
from sklearn.linear_model import LogisticRegression as lr

# Local application imports
from file_manager import df_from_csv, csv_from_df

# Setting constants
MAIN_FOLDER: Path = Path(__file__).absolute().parent
DATA_PATH: str = '../data/'

# Function to complete logical regression
def regression():
    '''
    This function brings in data from prior parts, works through logical regression to provide files for future analysis.
    '''

    # Pulling in the targeted dataframe for regression
    beginning_file: str = 'preprocessed.csv'
    df_arrests: pd = df_from_csv(DATA_PATH + beginning_file)
    
    # Create list of features
    features: list = ['num_fel_arrests_last_year', 'current_charge_felony']

    # Using train_test_split to build training and testing dataframes
    df_arrests_train, df_arrests_test, subs_felony_train, subs_felony_test = train_test_split(df_arrests[features] ,df_arrests['y'], test_size = 0.3, shuffle = True, stratify = df_arrests['y'])

    # Create a parameter grid with three values for C hyperparameter
    param_grid: dict = {'C': [.5, 5, 50, 500, 5000]}

    # Initialize logisitic regression model
    lr_model: lr = lr(solver = 'liblinear')

    # Initialize GridSearchSCV using lr_moeld and param_grid
    gs_cv: GridSearchCV = GridSearchCV(lr_model, param_grid, scoring = 'accuracy')

    # Run the model
    model = gs_cv.fit(df_arrests_train, subs_felony_train)
    print(sorted(model.best_params_))




# Script run control
if __name__ == "__main__":
    regression()
