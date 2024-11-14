# All code for this program directly contributed by Preston Thomas

import psycopg2 as sql
import pandas as pd

# Establish database connection
# Might have to modify depending on your local database configuration

conn = sql.connect(
    dbname = "nfl_data",
    user = "postgres",
    host = "localhost",
    port = "5432"
)

#TODO: Run various queries to extract raw data into data frames & transform