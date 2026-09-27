import pandas as pd

def calculate_rolling_averages(df, window=5):
    """
    Calculates rolling averages for goals scored and conceded over the last N matches.
    """
    if 'date' in df.columns:
        df = df.sort_values('date')

    # Rolling goals scored
    df['home_rolling_scored'] = df.groupby('home_team')['home_score'].transform(lambda x: x.shift(1).rolling(window, min_periods=1).mean())
    df['away_rolling_scored'] = df.groupby('away_team')['away_score'].transform(lambda x: x.shift(1).rolling(window, min_periods=1).mean())
    
    # Rolling goals conceded
    df['home_rolling_conceded'] = df.groupby('home_team')['away_score'].transform(lambda x: x.shift(1).rolling(window, min_periods=1).mean())
    df['away_rolling_conceded'] = df.groupby('away_team')['home_score'].transform(lambda x: x.shift(1).rolling(window, min_periods=1).mean())
    
    # Fill initial NaNs with 0
    df = df.fillna(0)
    return df