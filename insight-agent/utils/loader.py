import pandas as pd
import duckdb
import os

def load_data(file_path: str) -> pd.DataFrame:
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".csv":
        return pd.read_csv(file_path)
    elif ext == ".json":
        return pd.read_json(file_path)
    elif ext == ".db":
        con = duckdb.connect(file_path)
        return con.execute("SELECT * FROM your_table_name").df()
    else:
        raise ValueError(f"Unsupported file format: {ext}")

def load_json(path):
    """Load data from a JSON file."""
    pass


def load_sql(query, db_path):
    """Load data from a SQL database using DuckDB."""
    pass
