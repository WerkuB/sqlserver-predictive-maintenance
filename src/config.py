import os
from dotenv import load_dotenv

load_dotenv()

def get_conn_string():
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    driver = os.getenv("ODBC_DRIVER", "{ODBC Driver 17 for SQL Server}")
    trusted = os.getenv("TRUSTED_CONNECTION", "no")

    if trusted.lower() == "yes":
        return f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
    else:
        return f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password};"
