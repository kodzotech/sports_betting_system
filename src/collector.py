import os
import pandas as pd
import requests

def load_local_data(filepath):
    """
    Load raw historical match data from a local CSV file.
    Expected columns: date, home_team, away_team, home_score, away_score
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found at {filepath}")
    
    df = pd.read_csv(filepath)
    print(f"Successfully loaded {len(df)} rows from {filepath}")
    return df

def fetch_api_data(api_url, api_key=None):
    """
    Template function to fetch live or historical fixtures from a sports API.
    (e.g., API-Football, Football-Data.org)
    """
    headers = {'X-Auth-Token': api_key} if api_key else {}
    
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            print("Successfully fetched data from API.")
            return response.json()
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while connecting to the API: {e}")
        return None