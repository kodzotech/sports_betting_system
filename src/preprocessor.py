import pandas as pd

def clean_data(df):
    """
    Cleans raw match data by removing missing values and standardizing team names.
    """
    # Drop rows with missing scores or team names
    df = df.dropna(subset=['home_team', 'away_team', 'home_score', 'away_score'])
    
    # Standardize team names to strip whitespace and format properly
    df['home_team'] = df['home_team'].str.strip().str.title()
    df['away_team'] = df['away_team'].str.strip().str.title()
    
    # Create target variable: 1 for Home Win, 0 for Draw, 2 for Away Win
    def get_match_outcome(row):
        if row['home_score'] > row['away_score']:
            return 1  # Home Win
        elif row['home_score'] == row['away_score']:
            return 0  # Draw
        else:
            return 2  # Away Win

    df['target'] = df.apply(get_match_outcome, axis=1)
    return df