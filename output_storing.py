from logger import log
from db_config import get_client
import pandas as pd

def insert_into_clickhouse(df, table_name):
    """Insert transformed data back into ClickHouse"""
    try:
        client = get_client()
        
        # Convert DataFrame to list of tuples for insertion
        data_to_insert = [tuple(x) for x in df.to_numpy()]
        
        # Insert data into the specified table
        client.insert(table_name, data_to_insert)
        log(f"Final data inserted successfully into '{table_name}' in 'AH' database.", level="info")
    except Exception as e:
        log(f"Error in inserting data: {str(e)}", level="error")
        raise
