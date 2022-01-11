import requests
import pandas as pd
import numpy as np


def get_api_data(endpoint):
    """
    Function will pull data from API interface in a while loop to get stores, items, and sales data
    """
    host = "https://python.zgulde.net/"
    api = "api/v1/"
    
    url = host + api + endpoint

    response = requests.get(url).json()

    payload = response['payload']

    contents = payload[endpoint]

    df = pd.DataFrame(contents)

    next_page = payload['next_page']

    while next_page:

        url = host + next_page

        response = requests.get(url).json()

        payload = response['payload']

        contents = pd.DataFrame(payload[endpoint])

        df = pd.concat([df, contents])

        df = df.reset_index(drop=True)

        next_page = payload['next_page']
        
    return df


def stores_sales_items(sales, stores, items):
    stores_sales = pd.merge(sales, stores, how='left', left_on='store', right_on='store_id')
    stores_sales.head()

    stores_sales_items = pd.merge(stores_sales, items, how='left', left_on='item', right_on='item_id')
    stores_sales_items.head()
    
    return stores_sales_items