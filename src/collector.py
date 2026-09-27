import os
import requests
import pandas as pd

def fetch_upcoming_fixtures(api_token, date_from=None, date_to=None):
    """
    Fetches upcoming matches from the football-data.org API within a specified date range.
    """
    url = "https://api.football-data.org/v4/matches"
    
    params = {}
    if date_from and date_to:
        params['dateFrom'] = date_from
        params['dateTo'] = date_to
        
    headers = {'X-Auth-Token': api_token}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        matches = data.get('matches', [])
        
        fixture_list = []
        for match in matches:
            fixture_list.append({
                'date': match['utcDate'].split('T')[0],
                'home_team': match['homeTeam']['name'],
                'away_team': match['awayTeam']['name'],
                'status': match['status'],
                'competition': match['competition']['name']
            })
        
        df_fixtures = pd.DataFrame(fixture_list)
        print(f"Successfully fetched {len(df_fixtures)} upcoming fixtures.")
        return df_fixtures
    else:
        print(f"Failed to fetch fixtures. Status code: {response.status_code}, Response: {response.text}")
        return pd.DataFrame()