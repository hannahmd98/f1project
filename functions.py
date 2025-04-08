import pandas as pd 
from datetime import date, time
import numpy as np
import json
import traceback

def import_csv(csv_path):
    ''' Import csv file.
    Arg: 
        csv_path: path name for csv file
    Returns:
        dataframe of csv file
    Raises:
        TypeError: if csv is not a path.
    '''
    try:
        df = pd.read_csv(csv_path)
        #df = pd.read_csv(csv_path, na_values="\\N")
        return df
    except Exception as e:
        print(e)

def import_config(path):
    ''' Import config json file.
    Arg: 
        path: path name for json config file
    Returns:
        json config file
    Raises:
        TypeError: if path is not a path.
    '''
    try: 
        with open(path, "r") as f:
            jsonf = json.loads(f.read())
        return jsonf
    except Exception as e:
        print(e)

def drop_columns(df, col_ls):
    '''Drops columns that are determined not to use
    Arg: 
        df: dataframe
        col_ls: list of columns
    Returns:
        dataframe without the determined columns
    Raises:
        TypeError: anything is the wrong with any of the inputs
    '''
    try:
        for col in col_ls:
            if col in df.columns:

                df = df.drop(col_ls, axis=1)
                return df
            else: 
                return df
    except Exception as e:
        print(e)

def replace_str(df, col_ls, str1, str2):
    ''' Replaces 1 string with another string
    Arg: 
        df: dataframe
        col_ls: list of columns
        str1: the string to change
        str2: what to change the string to
    Returns:
        dataframe with fixed columns
    Raises:
        TypeError: anything is the wrong with any of the inputs
    '''
    try:
        for col in col_ls:
            if col in df.columns and df[col].dtype != int:
                df[col] = df[col].str.lstrip("+")
                df[col] = df[col].replace(str1, str2)
        return df
    except Exception as e:
        print(e)

def datatype_col(df, col_dict): 
    ''' Fixes datatype for each column based on what datatype is specified. 
    Arg: 
        df: dataframe
        col_dict: dictionary, the key is datatype and the value is list of columns to change
    Returns:
        dataframe with fixed columns
    Raises:
        TypeError: anything is the wrong with any of the inputs
    '''
    try:
        for key in col_dict: 
            if key == "datetime": 
                for value in col_dict[key]: 
                    if value in df.columns:
                        df[value] = pd.to_datetime(df[value])
            if key == 'time': 
                # d = {'^(\d+\.\d+)$': r'00:00:\1', '^(\d+:\d+\.\d+)$': r'00:\1'}
                for value in col_dict[key]: 
                    if value in df.columns:
                        # Apply the convert_to_time function to the specified column
                        df[value] = df[value].apply(lambda x: convert_to_time(x) if pd.notnull(x) else np.nan)
            elif key in ["int", "float"]:
                for value in col_dict[key]: 
                    if value in df.columns:
                        df[value] = pd.to_numeric(df[value], errors='coerce')
            elif key == 'string':
                for value in col_dict[key]: 
                    if value in df.columns:
                        df[value] = df[value].astype(str)
        return df
    except Exception as e:
        print(e)

def convert_to_time(value):
    try:
        # Try to parse format H:M:S.f
        if ':' in value:
            return pd.to_datetime(value, format='%H:%M:%S.%f', errors='coerce').time()
        # Try to parse decimal seconds
        else:
            seconds = float(value)
            return (pd.Timestamp('1970-01-01') + pd.to_timedelta(seconds, unit='s')).time()
    except:
        return np.nan