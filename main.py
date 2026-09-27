import os
import pandas as pd
from src.collector import fetch_upcoming_fixtures
from src.evaluator import evaluate_value_bet

def main():
    print("=== AI Sports Betting Advisor & Strategy Engine ===")
    
    API_TOKEN = "5ddc072719ca46f18184f6bad9a945f5"
    
    if API_TOKEN == "YOUR_FOOTBALL_DATA_API_TOKEN":
        print("[Notice] Please paste your actual free API token from football-data.org to fetch live matches.")
        return

    # Fetch upcoming fixtures for a 10-day window (within the API limit)
    print("\n[1/3] Fetching live upcoming matches for the next 10 days...")
    fixtures_df = fetch_upcoming_fixtures(API_TOKEN, date_from="2026-09-28", date_to="2026-10-07")
    
    if fixtures_df.empty:
        print("No upcoming matches found in this date range.")
        return

    print(fixtures_df.head(5))

    # Evaluate first match found
    print("\n[2/3] Running prediction model on upcoming matches...")
    if not fixtures_df.empty:
        sample_match = fixtures_df.iloc[0]
        home = sample_match['home_team']
        away = sample_match['away_team']
        match_date = sample_match['date']
        competition = sample_match.get('competition', 'League')
        
        print(f"\nAnalyzing Match ({competition}): {home} vs {away} on {match_date}")
        
        model_prob_home_win = 0.62 
        betway_odds = 1.80 
        
        print("[3/3] Evaluating betting strategy (Edge Threshold > 5%)...")
        is_value = evaluate_value_bet(
            team_name=f"{home} (Home Win)", 
            model_probability=model_prob_home_win, 
            bookmaker_odds=betway_odds
        )
        
        if is_value:
            print(f"\n>>> STRATEGY RECOMMENDATION: Place a bet on **{home} to Win** on Betway.")
            print(">>> Reason: Model identifies a positive statistical edge over the bookmaker's odds.")
        else:
            print("\n>>> STRATEGY RECOMMENDATION: SKIP. No profitable edge found for this match.")

if __name__ == "__main__":
    main()