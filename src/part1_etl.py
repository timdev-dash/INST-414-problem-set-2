'''
PART 1: ETL the two datasets and save each in `data/` as .csv's
'''

# Third party imports
import pandas as pd

# The etl function will extract the data from the url's, transform the data with the provided
# instructions, and load the data into csv files in the ./data folder
def etl():
    '''
    etl function performs the extract, transform, and load work necessary to proceed through the problem

    Returns
    pred_universe_raw(Dataframe): Pred Universe dataframe
    arrest_events_raw(Dataframe): Arrest Events dataframe
    '''

    # Extract dataframes from the provided data sources
    pred_universe_raw: pd = pd.read_csv('https://www.dropbox.com/scl/fi/69syqjo6pfrt9123rubio/universe_lab6.feather?rlkey=h2gt4o6z9r5649wo6h6ud6dce&dl=1')
    arrest_events_raw: pd = pd.read_csv('https://www.dropbox.com/scl/fi/wv9kthwbj4ahzli3edrd7/arrest_events_lab6.feather?rlkey=mhxozpazqjgmo6qqahc2vd0xp&dl=1')

    # Transform data within the dataframes to allow for future analysis
    pred_universe_raw['arrest_date_univ'] = pd.to_datetime(pred_universe_raw.filing_date)
    arrest_events_raw['arrest_date_event'] = pd.to_datetime(arrest_events_raw.filing_date)
    pred_universe_raw.drop(columns=['filing_date'], inplace=True)
    arrest_events_raw.drop(columns=['filing_date'], inplace=True)

    return pred_universe_raw, arrest_events_raw

# Script run control
if __name__ == "__main__":
    etl()