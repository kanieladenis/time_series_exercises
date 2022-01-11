import requests
import pandas as pd
import numpy as np


def get_api_data(endpoint):
    """
    Function will pull data from API interface in a while loop
    """
    host = "https://python.zgulde.net/"
    api = "api/v1/"
    endpoint = 'items'

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