# All code for this program directly contributed by Preston Thomas

import psycopg2 as sql
import pandas as pd

# Establish database connection
# Might have to modify depending on your local database configuration
# Password will likely be different on your own installation
connection_string = "dbname = nfl_data user = postgres password = nfl_football_rocks host = localhost port = 5432"
conn = sql.connect(connection_string)
cur = conn.cursor()

# Sample query and print statement to verify successful database connection made
cur.execute("SELECT * FROM nfl_data.combine_data ORDER BY shuttle LIMIT 10")
results = cur.fetchall()

for row in results:
    print(row)