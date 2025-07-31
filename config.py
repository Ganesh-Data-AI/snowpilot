import os

conn_params = {
    "account": os.environ.get("SNOWFLAKE_ACCOUNT"),
    "region": os.environ.get("SNOWFLAKE_REGION"),
    "user": os.environ.get("SNOWFLAKE_USER"),
    "password": os.environ.get("SNOWFLAKE_PASSWORD"),
    "database": os.environ.get("SNOWFLAKE_DATABASE"),
    "db_schema": os.environ.get("SNOWFLAKE_DB_SCHEMA")
}
