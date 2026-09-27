import os
import requests
import pandas as pd

def fetch_upcoming_fixtures(api_token):
    """
    Fetches real upcoming matches from the football-data.org API.
    """
    url = "https://api.football-data.org/v4/matches"
    headers = {'X-Auth-Token': 5ddc072719ca46f18184f6bad9a945f5}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        matches = data.get('matches', [])
        
        fixture_list = []
        for match in matches:
            fixture_list.append({
                'date': match['utcDate'].split('T')[0],
                'home_team': match['homeTeam']['name'],
                'away_team': match['awayTeam']['name'],
                'status': match['status']
            })
        
        df_fixtures = pd.DataFrame(fixture_list)
        print(f"Successfully fetched {len(df_fixtures)} upcoming fixtures.")
        return df_fixtures
    else:
        print(f"Failed to fetch fixtures. Status code: {response.status_code}")
        return pd.DataFrame()