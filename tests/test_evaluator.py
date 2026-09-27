import unittest
import sys
import os

# Add parent directory to path so we can import src modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.evaluator import decimal_to_probability, evaluate_value_bet

class TestEvaluator(unittest.TestCase):
    
    def test_decimal_to_probability(self):
        # Odds of 2.00 should equal a 50% (0.5) implied probability
        self.assertAlmostEqual(decimal_to_probability(2.0), 0.5)
        # Odds of 4.00 should equal a 25% (0.25) implied probability
        self.assertAlmostEqual(decimal_to_probability(4.0), 0.25)

    def test_evaluate_value_bet_positive_edge(self):
        # Model prob 60% (0.6), Betway odds 2.0 (implied 50%). Edge should be positive.
        has_value = evaluate_value_bet("Team A", model_probability=0.60, bookmaker_odds=2.0)
        self.assertTrue(has_value)

    def test_evaluate_value_bet_no_edge(self):
        # Model prob 40% (0.4), Betway odds 1.8 (implied ~55.5%). Edge should be negative.
        has_value = evaluate_value_bet("Team B", model_probability=0.40, bookmaker_odds=1.8)
        self.assertFalse(has_value)

if __name__ == '__main__':
    unittest.main()