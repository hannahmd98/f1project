import pandas as pd 
import numpy as np
# from datetime import date, time
import traceback
#import json
import os
import functions


def main():

    config = functions.import_config('/Users/hannahdorney/Documents/GitHub/f1project/config.json')
    for filename in os.listdir('/Users/hannahdorney/Documents/GitHub/f1project/data'):
        f = os.path.join('/Users/hannahdorney/Documents/GitHub/f1project/data', filename)
        df = functions.import_csv(f)
        df = functions.replace_str(df, config["nullable_columns"], '\\N', np.nan)
        df = functions.drop_columns(df, config['drop_columns'])
        df = functions.datatype_col(df, config["columns_datatypes"])
        print(filename.replace('.csv', ''))
        #print(df.dtypes)

if __name__ == '__main__':
    main()