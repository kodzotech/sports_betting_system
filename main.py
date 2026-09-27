import os
import pandas as pd
from src.collector import load_local_data
from src.preprocessor import clean_data
from src.features import calculate_rolling_averages
from src.model import MatchPredictor
from src.evaluator import evaluate_value_bet

def main():
    print("=== Initializing Sports Betting Prediction System ===")
    
    # Define file path for raw data
    raw_data_path = os.path.join('data', 'raw', 'matches.csv')
    
    # 1. Check if raw data exists, create a sample if missing for demonstration
    if not os.path.exists(raw_data_path):
        print(f"[Notice] No file found at {raw_data_path}. Creating a sample dataset...")
        os.makedirs(os.path.join('data', 'raw'), exist_ok=True)
        sample_df = pd.DataFrame({
            'date': ['2026-01-01', '2026-01-05', '2026-01-10', '2026-01-15', '2026-01-20'],
            'home_team': ['Arsenal', 'Chelsea', 'Man Utd', 'Arsenal', 'Chelsea'],
            'away_team': ['Chelsea', 'Man Utd', 'Arsenal', 'Man Utd', 'Arsenal'],
            'home_score': [2, 1, 3, 0, 2],
            'away_score': [1, 1, 0, 2, 2]
        })
        sample_df.to_csv(raw_data_path, index=False)

    # 2. Load Data
    print("\n[1/5] Loading match data...")
    df = load_local_data(raw_data_path)
    
    # 3. Preprocess Data
    print("[2/5] Cleaning data and generating targets...")
    df = clean_data(df)
    
    # 4. Feature Engineering
    print("[3/5] Calculating rolling averages...")
    df = calculate_rolling_averages(df, window=2)
    
    # Save processed data
    processed_path = os.path.join('data', 'processed', 'processed_matches.csv')
    os.makedirs(os.path.join('data', 'processed'), exist_ok=True)
    df.to_csv(processed_path, index=False)
    print(f"Processed data saved to {processed_path}")
    
    # 5. Train Model (Requires at least a few rows with valid features/targets)
    print("[4/5] Training machine learning model...")
    feature_cols = ['home_rolling_scored', 'away_rolling_scored']
    predictor = MatchPredictor()
    
    try:
        predictor.train_and_evaluate(df, feature_cols)
    except Exception as e:
        print(f"Training skipped/deferred due to small sample size: {e}")
    
    # 6. Odds Evaluation Example (Simulating a live Betway odds check)
    print("\n[5/5] Checking Betway odds for value...")
    # Example: Your model estimates Arsenal has a 58% chance to win, Betway offers 1.90 odds
    evaluate_value_bet(team_name="Arsenal", model_probability=0.58, bookmaker_odds=1.90)
    
    print("\n=== Pipeline Execution Complete ===")

if __name__ == "__main__":
    main()