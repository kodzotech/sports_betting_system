def decimal_to_probability(decimal_odds):
    """Convert decimal bookmaker odds to implied probability."""
    return 1 / decimal_odds

def evaluate_value_bet(team_name, model_probability, bookmaker_odds):
    """
    Compares model probability against bookmaker odds to find value bets.
    """
    implied_prob = decimal_to_probability(bookmaker_odds)
    edge = model_probability - implied_prob
    
    print(f"\n--- Betting Evaluation for {team_name} ---")
    print(f"Model Probability: {model_probability * 100:.2f}%")
    print(f"Bookmaker Implied Prob: {implied_prob * 100:.2f}%")
    print(f"Calculated Edge: {edge * 100:.2f}%")
    
    if edge > 0:
        print("Status: [VALUE BET FOUND] Model probability exceeds bookmaker implied probability.")
        return True
    else:
        print("Status: [NO VALUE] Odds are too short.")
        return False