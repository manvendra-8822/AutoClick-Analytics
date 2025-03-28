from db_config import get_client,get_SQLClient
from logger import log
import pandas as pd

def fetch_data(query):
    """Fetch data from MySQL database."""
    try:
        client = get_SQLClient()
        # log("Connected to MySQL database.", level="info")
        # result = client.query_df(query) 
        cursor = client.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        log("Query execution completed", level="info")

        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(result, columns=columns)

        if not df.empty:
                rows=df.shape[0]
                log("Data fetched successfully from database.", level="info")
                log(f"{rows} rows fetched", level="info")
                return df
        else:
                log("No data returned from the query.", level="warning")
                return pd.DataFrame()
    except Exception as e:
        log(f"Error in fetching data: {str(e)}", level="error")
        raise
    finally:
        cursor.close()
        client.close()
        log("MySQL connection closed.", level="info")

# if __name__ == "__main__":
#     df = fetch_data(query)
#     print(df.head())



