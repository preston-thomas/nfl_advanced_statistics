# All code for this program directly contributed by Preston Thomas

import sqlalchemy as sql
import pandas as pd

# Establish database connection
# Might have to modify depending on your local database configuration
# Password will likely be different on your own installation
engine = sql.create_engine("postgresql+psycopg2://postgres:nfl_football_rocks@localhost:5432/nfl_data")
test_query = "SELECT season, draft_year, draft_team, draft_round FROM nfl_data.combine_data ORDER BY shuttle LIMIT 10"

if __name__ == "__main__":
    test_df = pd.read_sql_query(test_query, engine)
    print(test_df.head())