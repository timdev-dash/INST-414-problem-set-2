'''
This script contains the various methods of opening and saving data with files. Its
intention is to be used as a code package to carry over from project to 
project without needing to rewrite or copy/paste working ingestion script
'''

# Standard library imports
from pathlib import Path
import requests

# Third party imports
import pandas as pd

# Setting constants
MAIN_FOLDER: Path = Path(__file__).absolute().parent

def from_web_b(self, url: str, download_settings: dict, file_name: str, relative_path: str = ''):
    '''
    Ingests a targeted file from a website and saves in a directory with a name in a binary form
    
    Parameters:
        url(string): The url to download the file from
        download_settings(dict): The dictionary of settings to be used in the download
        file_name(string): The name the file should be saved as, included extension
        relative_path(string): Details on where, other than the script's native directory
            the file should be saved
    '''

    # Requests data from the targeted site
    response: requests = requests.get(url, params = download_settings, timeout = 90)

    # Saves requested file in the provided directory
    with (open(MAIN_FOLDER / relative_path / file_name, mode = "wb")) as file:
        file.write(response.content)

def from_web(url: str, download_settings: dict, file_name: str, relative_path: str = '', encoding_type: str = 'UTF-8'):
    '''
    Ingests a targeted file from a website and saves in a directory with a name
    
    Parameters:
        url(string): The url to download the file from
        download_settings(dict): The dictionary of settings to be used in the download
        file_name(string): The name the file should be saved as, included extension
        relative_path(string): Details on where, other than the script's native directory
            the file should be saved
        encoding_type(string): The type of encoding to be used for opening the file.
            Defaults to UTF-8
    '''

    # Requests data from the targeted site
    response: requests = requests.get(url, params = download_settings, timeout = 90)

    # Saves requested file in the provided directory
    with (open(MAIN_FOLDER / relative_path / file_name, mode = "w", encoding = encoding_type)) as file:
        file.write(response.content)

def df_from_csv(path_and_file: str):
    '''
    Ingests a targeted file from a directory and returns it as a dataframe using a generic
    numeric index and default column names.

    Parameters:
        path_and_file(string): Location and name details for the csv file to be opened

    Returns:
        data(Dataframe): The dataframe containing the contents of the .csv file
    '''

    # Setting up the dataframe for ingestion
    data: pd = pd.read_csv(MAIN_FOLDER / path_and_file, sep = '\t', encoding = 'UTF-8')

    # Returns the dataframe
    return data

def csv_from_df(file_to_write:pd, path_and_file: str, separation_type: str = '\t', encoding_type: str = 'UTF-8'):
    '''
    Takes a provided dataframe and saves it as a csv file with the provided name and directory

    Parameters:
        file_to_write(pandas): The dataframe to be saved as a csv file
        path_and_file(string): Location and name details for the csv file to be saved
        separation_type(string): The separator to use on the csv file, defaults to '\t'
        encoding_type(string): The encoding to use on th csv file, defaults to 'UTF-8'
    '''

    # Writes the provide dataframe to a file
    file_to_write.to_csv(MAIN_FOLDER / path_and_file, sep = separation_type, encoding = encoding_type)

# Script run control
if __name__ == "__main__":
    pass