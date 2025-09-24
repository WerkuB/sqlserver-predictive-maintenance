import pyodbc
import pandas as pd
from src.config import get_conn_string

QUERIES = {
    "cpu": """
        SELECT 
            cntr_value AS BatchRequestsPerSec
        FROM sys.dm_os_performance_counters
        WHERE counter_name = 'Batch Requests/sec';
    """,
    "memory": """
        SELECT
            (SELECT cntr_value FROM sys.dm_os_performance_counters
             WHERE counter_name = 'Total Server Memory (KB)') AS TotalMemoryKB,
            (SELECT cntr_value FROM sys.dm_os_performance_counters
             WHERE counter_name = 'Target Server Memory (KB)') AS TargetMemoryKB;
    """,
    "sessions": """
        SELECT COUNT(*) AS ActiveSessions
        FROM sys.dm_exec_sessions
        WHERE status = 'running';
    """,
    "io": """
        SELECT 
            SUM(num_of_reads) AS Reads,
            SUM(num_of_writes) AS Writes
        FROM sys.dm_io_virtual_file_stats(NULL, NULL);
    """
}

def collect_metrics(conn):
    metrics = {}
    cur = conn.cursor()
    for name, sql in QUERIES.items():
        df = pd.read_sql(sql, conn)
        for col in df.columns:
            metrics[f"{name}_{col}"] = df.iloc[0][col]
    return metrics

if __name__ == "__main__":
    conn = pyodbc.connect(get_conn_string())
    data = collect_metrics(conn)
    df = pd.DataFrame([data])
    df.to_csv("data/metrics.csv", mode="a", header=False, index=False)
    print("✅ Metrics collected:", data)
