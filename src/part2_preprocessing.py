'''
PART 2: Pre-processing
x Take the time to understand the data before proceeding
x Load `pred_universe_raw.csv` into a dataframe and `arrest_events_raw.csv` into a dataframe
x Perform a full outer join/merge on 'person_id' into a new dataframe called `df_arrests`
x Create a column in `df_arrests` called `y` which equals 1 if the person was arrested for a felony crime in the 365 days after their arrest date in `df_arrests`. 
x - So if a person was arrested on 2016-09-11, you would check to see if there was a felony arrest for that person between 2016-09-12 and 2017-09-11.
x - Use a print statment to print this question and its answer: What share of arrestees in the `df_arrests` table were rearrested for a felony crime in the next year?
x Create a predictive feature for `df_arrests` that is called `current_charge_felony` which will equal one if the current arrest was for a felony charge, and 0 otherwise. 
x - Use a print statment to print this question and its answer: What share of current charges are felonies?
x Create a predictive feature for `df_arrests` that is called `num_fel_arrests_last_year` which is the total number arrests in the one year prior to the current charge. 
x - So if someone was arrested on 2016-09-11, then you would check to see if there was a felony arrest for that person between 2015-09-11 and 2016-09-10.
x - Use a print statment to print this question and its answer: What is the average number of felony arrests in the last year?
- Print the mean of 'num_fel_arrests_last_year' -> pred_universe['num_fel_arrests_last_year'].mean()
- Print pred_universe.head()
x Return `df_arrests` for use in main.py for PART 3; if you can't figure this out, save as a .csv in `data/` and read into PART 3 in main.py
'''

# Standard library imports
from pathlib import Path
import re

# Third party imports
import pandas as pd

# Local application imports
from file_manager import df_from_csv, csv_from_df

# Setting constants
MAIN_FOLDER: Path = Path(__file__).absolute().parent
DATA_PATH: str = '../data/'
FINAL_ARRESTS_FILE: str = 'preprocessed.csv'#'preprocessed_arrests.csv'
FINAL_PRED_FILE: str = 'preprocessed_pred_universe.csv'

# Fuction to complete preprocessing
def preprocess():
    '''
    Preprocessing function to perform assigned tasks
    '''
    # Pulling in the targeted dataframes for pre-processing
    pred_universe_df = preload('pred_universe_raw.csv')
    arrest_events_df = preload('arrest_events_raw.csv')

    # Joining the dataframes to create df_arrests for further evaluation
    df_arrests:pd = prejoin(arrest_events_df, pred_universe_df, 'person_id')
    df_arrests.sort_values('arrest_date_event', inplace = True) 
    
    ## Create a column in `df_arrests` called `y` which equals 1 if the person was arrested for a felony 
    ## crime in the 365 days after their arrest date in `df_arrests`. 
    
    # Setting up the column and preparing for analysis
    df_arrests['y'] = 0
    arrest_entries: int = df_arrests.shape[0]
    arrestee: int = 0

    ## Create a predictive feature for `df_arrests` that is called `current_charge_felony` which 
    ## will equal one if the current arrest was for a felony charge, and 0 otherwise. 

    # Setting up the column
    df_arrests['current_charge_felony'] = 0

    ## Create a predictive feature for `df_arrests` that is called `num_fel_arrests_last_year` which 
    ## is the total number arrests in the one year prior to the current charge. 

    # Setting up the column
    df_arrests['num_fel_arrests_last_year'] = 0

    # Using a while loop to compare current arrestee's number to future arrests within one year
    while arrestee < arrest_entries:

        # Pulling arrestee details for comparison
        arrestee_id: int = df_arrests.loc[arrestee, 'person_id']
        arrestee_charge: str = df_arrests.loc[arrestee, 'charge_degree']
        
        # Converting the arrest date to a date object
        arrestee_year: int = int(re.findall(r'[\d]{4}(?=-)', df_arrests.loc[arrestee,'arrest_date_event'])[0])
        arrestee_month: int = int(re.findall(r'(?<=-)[\d]*(?=-[\d])', df_arrests.loc[arrestee,'arrest_date_event'])[0])
        arrestee_day: int = int(re.findall(r'(?<=-[\d]{2}-)[\d]{2}', df_arrests.loc[arrestee,'arrest_date_event'])[0])
        arrestee_date: int = (arrestee_year * 10000) + (arrestee_month * 100) + arrestee_day
        arrestee_plus_year: int = ((arrestee_year + 1) * 10000) + (arrestee_month * 100) + arrestee_day
        arrestee_minus_year: int = ((arrestee_year - 1) * 10000) + (arrestee_month * 100) + arrestee_day

        # Setting up a while loop to compare future arrests
        arrest_compare_number: int = 0

        while arrest_compare_number < arrest_entries:

            # Pulling comparison data
            arrest_compare_id: int = df_arrests.loc[arrest_compare_number, 'person_id']
            arrest_compare_degree: str = df_arrests.loc[arrest_compare_number, 'charge_degree']

            # Converting the arrest comparison date to a date object
            arrest_compare_year: int = int(re.findall(r'[\d]{4}(?=-)', df_arrests.loc[arrest_compare_number,'arrest_date_event'])[0])
            arrest_compare_month: int = int(re.findall(r'(?<=-)[\d]*(?=-[\d])', df_arrests.loc[arrest_compare_number,'arrest_date_event'])[0])
            arrest_compare_day: int = int(re.findall(r'(?<=-[\d]{2}-)[\d]{2}', df_arrests.loc[arrest_compare_number,'arrest_date_event'])[0])
            arrest_compare_date: int = (arrest_compare_year * 10000) + (arrest_compare_month * 100) + arrest_compare_day
            
            # Running logic to see if the comparison arrest is:
            # 1. For the same arrestee
            # 2. A felony charge
            # 3. After the date of the previous arrest
            # 4. Less than a year after the date of the previous arrest
            # print(arrestee_id, ',', arrest_compare_id, ':', arrest_compare_degree, ':', arrestee_date, ',', arrest_compare_date)

            if arrest_compare_id != arrestee_id:
                pass
            elif arrest_compare_degree != 'felony':
                pass
            elif arrest_compare_date <= arrestee_date:
                pass    
            elif arrest_compare_date > arrestee_plus_year:
                pass
            else:
                df_arrests.at[arrestee, 'y'] = 1
            
            ## So if someone was arrested on 2016-09-11, then you would check to see if there was a felony arrest for that person between 2015-09-11 and 2016-09-10.
            # Running logic to see if the comparison arrest is:
            # 1. For the same arrestee
            # 2. A felony charge
            # 3. Before the date of the previous event
            # 4. No more than a year before the date of the previous event

            if arrest_compare_id != arrestee_id:
                pass
            elif arrest_compare_degree != 'felony':
                pass
            elif arrest_compare_date >= arrestee_date:
                pass
            elif arrest_compare_date < arrestee_minus_year:
                pass
            else:
                df_arrests.at[arrestee, 'num_fel_arrests_last_year'] += 1

            #  Iterate the loop to continue
            arrest_compare_number += 1
        
        # Checking the arrestee's charge_degree, and if felony, changing the value of current_charge_felony
        if arrestee_charge == 'felony':
            df_arrests.at[arrestee, 'current_charge_felony'] = 1
        

        # Iterate the loop to continue
        arrestee += 1
        
    # Saving the final dataframe for future stages
    csv_from_df(df_arrests, DATA_PATH + FINAL_ARRESTS_FILE)

    # Runs analysis function for dataset to provide requested answers
    analysis()

# Loading of the files and creating the dataframes for additional processing
def preload(file_name: str):
    '''
    This function loads the pred_universe and arrest_events csv files into dataframes for
    additional pre-processing

    Parameter:
        file_name(string): The name of the file to be opened

    Returns:
        new_dataframe(pandas): The loaded dataframe
    '''

    new_dataframe: pd = df_from_csv(DATA_PATH + file_name)

    return new_dataframe

# Joining the two dataframes into a new dataframe
def prejoin(df1: pd, df2: pd, merge_key: str):
    '''
    This function joins the pred_universe and arrest_events dataframes into a new dataframe
    for further pre-processing
    
    Parameters:
        df1(pandas): The first dataframe, used as the basis for the joined_dataframe
        df2(pandas): The second dataframe, to be merged to the first dataframe
        merge_key(string): The column name on which to conduct the merge
    
    Returns:
        joined_dataframe(pandas): The joined dataframe for further pre-processing
    '''

    # Creating the dataframe to join onto
    joined_dataframe: pd = df1.copy()
    joined_dataframe = joined_dataframe.merge(df2, on = merge_key, how = 'outer')

    return joined_dataframe

# Performing anaylsis of preprocessed data
def analysis():
    '''
    This function performs analysis on the preproccesed data and provides print statments regarding the results
    - Create a column in `df_arrests` called `y` which equals 1 if the person was arrested for a felony crime in the 365 days after their arrest date in `df_arrests`. 
    - - So if a person was arrested on 2016-09-11, you would check to see if there was a felony arrest for that person between 2016-09-12 and 2017-09-11.
    - - Use a print statment to print this question and its answer: What share of arrestees in the `df_arrests` table were rearrested for a felony crime in the next year?
    - Create a predictive feature for `df_arrests` that is called `current_charge_felony` which will equal one if the current arrest was for a felony charge, and 0 otherwise. 
    - - Use a print statment to print this question and its answer: What share of current charges are felonies?
    - Create a predictive feature for `df_arrests` that is called `num_fel_arrests_last_year` which is the total number arrests in the one year prior to the current charge. 
    - - So if someone was arrested on 2016-09-11, then you would check to see if there was a felony arrest for that person between 2015-09-11 and 2016-09-10.
    - - Use a print statment to print this question and its answer: What is the average number of felony arrests in the last year?
    - Print the mean of 'num_fel_arrests_last_year' -> pred_universe['num_fel_arrests_last_year'].mean()
    - Print pred_universe.head()
    '''

    # Brings in the preprocessed data set
    preprocessed_df:pd = df_from_csv(DATA_PATH + FINAL_ARRESTS_FILE)
    pred_universe_file_name: str = 'pred_universe_raw.csv'
    pred_universe_df: pd = df_from_csv(DATA_PATH + pred_universe_file_name)

    # Determine and print the number of arrestees that were arrested for a felony within a year of their current arrest
    felony_rearrests: int = preprocessed_df.y.sum()
    print(felony_rearrests, 'arrestees were rearrested for a felony crime in the year following their intial arrest.')

    # Determine and print the number of charges that are felonies
    felony_charges: int = preprocessed_df.current_charge_felony.sum()
    print(felony_charges, 'of all current charges are for felonies.')

    # Determine and print the average of num_fel_arrests_last_year
    num_felony_last_year: int = preprocessed_df.num_fel_arrests_last_year.sum()
    num_of_arrests: int = preprocessed_df.shape[0]
    avg_felonies_last_year: float = num_felony_last_year / num_of_arrests
    print('The average number of felony arrests last year is', avg_felonies_last_year)

    # Determine mean of num_fel_arrests_last_year and add to pred_universe_df
    mean_fel_arrests_last_year: float = preprocessed_df.num_fel_arrests_last_year.mean()
    print(mean_fel_arrests_last_year)
    #print(pred_universe_df.head())

# Script run control
if __name__ == "__main__":
    #preprocess()
    analysis()



