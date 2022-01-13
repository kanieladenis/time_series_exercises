import requests
import pandas as pd
import numpy as np






def get_api_data(endpoint):
    """
    Function will pull data from API interface in a while loop
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

        df = pd.concat([df, contents]).reset_index(drop=True)

        next_page = payload['next_page']
        
    return df


def csv_files():
    import os
    if (os.path.isfile('items.csv') == False) or (os.path.isfile('sales.csv')==False) or (os.path.isfile('stores.csv')==False):
        items, stores, sales = stores_sales()
        items.to_csv('items.csv', index=False)
        stores.to_csv('stores.csv', index=False)
        sales.to_csv('sales.csv', index=False)
    else:
        items = pd.read_csv('items.csv')
        stores = pd.read_csv('stores.csv')
        sales = pd.read_csv('sales.csv')
        
    return items, stores, sales
        
        

def stores_sales():
    
    items = get_api_data(endpoint="items")
    
    stores = get_api_data(endpoint='stores')
    
    sales = get_api_data(endpoint='sales')
    
       
    return items, stores, sales




        
        
def sales_merged():
    
    items, stores, sales = csv_files()
    
    stores_sales = pd.merge(sales, stores, how='left', left_on='store', right_on='store_id')
    
    sales_merged = pd.merge(stores_sales, items, how='left', left_on='item', right_on='item_id')
    
    return sales_merged
    
    