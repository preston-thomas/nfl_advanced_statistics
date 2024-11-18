# All code for this program directly contributed by Preston Thomas

import sqlalchemy as sql
import pandas as pd

# Establish database connection
# Might have to modify depending on your local database configuration
# Password will likely be different on your own installation
engine = sql.create_engine("postgresql+psycopg2://postgres:nfl_football_rocks@localhost:5432/postgres")
combine_query = "SELECT * FROM postgres.nfl_data.combine_data"
player_query = "SELECT * FROM postgres.nfl_data.nfl_players"
qbr_szn_query = "SELECT * FROM postgres.nfl_data.qbr_szn"
qbr_week_query = "SELECT * FROM postgres.nfl_data.qbr_week"
roster_query = "SELECT * FROM postgres.nfl_data.rosters_2024"

# Processing raw data from SQL databases in pandas dataframes
combine_raw = pd.read_sql_query(combine_query, engine)
player_raw = pd.read_sql_query(player_query, engine)
qbr_szn_raw = pd.read_sql_query(qbr_szn_query, engine)
qbr_week_raw = pd.read_sql_query(qbr_week_query, engine)
rosters_raw = pd.read_sql_query(roster_query, engine)