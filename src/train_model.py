import pandas as pd
from sklearn.ensemble import IsolationForest
from src.preprocess import preprocess

def train_model():
    df = preprocess()
    features = df.dropna()

    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(features)

    df["anomaly"] = model.predict(features)
    df["anomaly"] = df["anomaly"].map({1: "normal", -1: "anomaly"})
    df.to_csv("data/metrics_with_anomaly.csv", index=False)

    print("✅ Model trained. Anomalies flagged.")
    print(df.tail())

if __name__ == "__main__":
    train_model()
