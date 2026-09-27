import os
import pandas as pd
from src.collector import fetch_upcoming_fixtures
from src.evaluator import evaluate_value_bet

def main():
    print("=== AI Sports Betting Advisor & Strategy Engine ===")
    
    # 1. Insert your free API token here (or store it in an environment variable)
    API_TOKEN = "5ddc072719ca46f18184f6bad9a945f5"
    
    if API_TOKEN == "5ddc072719ca46f18184f6bad9a945f5":
        print("[Notice] Please paste your actual free API token from football-data.org to fetch live matches.")
        return

    # 2. Fetch real upcoming fixtures
    print("\n[1/3] Fetching live upcoming matches...")
    fixtures_df = fetch_upcoming_fixtures(API_TOKEN)
    
    if fixtures_df.empty:
        print("No upcoming matches found or API limit reached.")
        return

    print(fixtures_df.head(5))

    # 3. Simulate getting model predictions & bookmaker odds for upcoming games
    print("\n[2/3] Running prediction model on upcoming matches...")
    
    # (In a fully trained pipeline, you pass fixture features into predictor.predict_match_probabilities())
    # Here is a strategy simulation for the first upcoming match found:
    if not fixtures_df.empty:
        sample_match = fixtures_df.iloc[0]
        home = sample_match['home_team']
        away = sample_match['away_team']
        match_date = sample_match['date']
        
        print(f"\nAnalyzing Match: {home} vs {away} on {match_date}")
        
        # Suppose your model calculates a 62% chance for Home Win
        model_prob_home_win = 0.62 
        
        # Suppose Betway offers decimal odds of 1.80 for the Home Win
        betway_odds = 1.80 
        
        # 4. Apply Betting Strategy Evaluation
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