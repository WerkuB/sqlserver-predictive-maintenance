import pandas as pd

def preprocess(file="data/metrics.csv"):
    df = pd.read_csv(file, header=None)
    df.columns = [
        "cpu_BatchRequestsPerSec",
        "memory_TotalMemoryKB",
        "memory_TargetMemoryKB",
        "sessions_ActiveSessions",
        "io_Reads",
        "io_Writes"
    ]
    df["MemoryUtilization"] = df["memory_TotalMemoryKB"] / df["memory_TargetMemoryKB"]
    return df

if __name__ == "__main__":
    df = preprocess()
    print("✅ Preprocessed data sample:")
    print(df.head())
