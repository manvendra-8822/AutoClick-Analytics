# import clickhouse_connect
# import pymysql
# import os
# from logger import log
# from dotenv import load_dotenv

# load_dotenv()

import clickhouse_connect 
from logger import log
import pymysql

def get_client():
    try:
        client = clickhouse_connect.get_client(host='YOUR HOST',user='', password='',secure=True,database='')
        # log("Connected to ClickHouse database.", level="info")
        return client
    except Exception as e:
        log(f"Failed to connect to ClickHouse: {str(e)}", level="error")
        raise

def get_SQLClient():
    try:
        sclient = pymysql.connect(
            host='',  
            user='',       
            password='', 
            database='',
            cursorclass=pymysql.cursors.DictCursor
        )
        log("Connected to MySQL database.", level="info")
        return sclient
    except Exception as e:
        log(f"Failed to connect to MySQL: {str(e)}", level="error")
        raise

# def get_client():
#     try:
#         client = clickhouse_connect.get_client(
#             host=os.getenv('CLICKHOUSE_HOST'),
#             user=os.getenv('CLICKHOUSE_USER'),
#             password=os.getenv('CLICKHOUSE_PASSWORD'),
#             port=8443,
#             secure=True,
#             database=os.getenv('CLICKHOUSE_DATABASE')
#         )
#         log("Connected to ClickHouse database.", level="info")
#         return client
#     except Exception as e:
#         log(f"Failed to connect to ClickHouse: {str(e)}", level="error")
#         raise

# def get_SQLClient():
#     try:
#         sclient = pymysql.connect(
#             host=os.getenv('MYSQL_HOST'),
#             user=os.getenv('MYSQL_USER'),
#             password=os.getenv('MYSQL_PASSWORD'),
#             database=os.getenv('MYSQL_DATABASE'),
#             cursorclass=pymysql.cursors.DictCursor
#         )
#         log("Connected to MySQL database.", level="info")
#         return sclient
#     except Exception as e:
#         log(f"Failed to connect to MySQL: {str(e)}", level="error")
#         raise