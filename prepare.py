import pandas as pd
from datetime import timedelta, datetime
import numpy as np

def prep_sales(df):
    # drop duplicate columns
    df = df.drop(columns=['store','item'])

    # convert date column to dytpe datetime
    df.sale_date = pd.to_datetime(df.sale_date)

    # set sales_date as index and sort index
    df = df.set_index('sale_date').sort_index()

    # add month columns
    df['month'] = df.index.month

    # add column for day of the week
    df['weekday'] = df.index.weekday

    # add columns sales_total by multiplying sale_amount and item_price
    df['total_sales'] = df.sale_amount * df.item_price
    
    return df