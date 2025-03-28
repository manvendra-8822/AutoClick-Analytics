from db_config import get_client
from logger import log

def ensure_table(create_table_query,output_table_name):
    """Check if the table exists, create if not."""
    try:
        client = get_client()
        client.command(create_table_query)
        log(f"Table {output_table_name} checked/created successfully in 'AH' database.", level="info")
    except Exception as e:
        log(f"Error in ensuring table: {str(e)}", level="error")
        raise

if __name__ == "__main__":
    ensure_table()
