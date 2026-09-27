from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class MatchPredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        
    def train_and_evaluate(self, df, feature_columns):
        """
        Trains the Random Forest model and prints test accuracy.
        """
        X = df[feature_columns]
        y = df['target']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model.fit(X_train, y_train)
        
        predictions = self.model.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        print(f"Model Training Complete. Test Accuracy: {acc * 100:.2f}%")
        
    def predict_match_probabilities(self, match_features):
        """
        Returns outcome probabilities for live fixtures.
        """
        return self.model.predict_proba(match_features)