import os
from schema_handler import ensure_table
from query_runner import fetch_data
from db_config import get_client
from logger import log
from output_storing import insert_into_clickhouse

def execute_query_file(file_path):
    """Execute the process for a single query file."""
    try:
        local_vars = {}
        with open(file_path, 'r') as f:
            exec(f.read(), {}, local_vars)

        query = local_vars.get("query")
        create_table_query = local_vars.get("create_table_query")
        output_table_name = local_vars.get("output_table_name")
        transform_data = local_vars.get("transform_data")

        if not query or not create_table_query or not output_table_name or not transform_data:
            log(f"Error in processing {file_path}: Missing required variables or function", level="error")
            return

        # Starting the process pipeline
        log(f"Starting data processing for {file_path}", level="info")
        get_client()
        log("Connected to ClickHouse database.", level="info")
        ensure_table(create_table_query,output_table_name)
        df = fetch_data(query)
        transformed_df = transform_data(df)
        insert_into_clickhouse(transformed_df, output_table_name)
        log(f"Data processing pipeline for {file_path} completed successfully!", level="info")
    except Exception as e:
        log(f"Error in processing {file_path}: {str(e)}", level="error")

def main():
    """Execute the full process for all query files in the queries folder."""
    
    log("Starting the data processing pipeline for all query files.", level="info")

    # Get list of all files in the queries folder
    query_files = [os.path.join("queries", file) for file in os.listdir("queries") if file.endswith(".py")]

    for file_path in query_files:
        execute_query_file(file_path)

    log("All query files processed successfully!", level="info")

if __name__ == "__main__":
    main()
