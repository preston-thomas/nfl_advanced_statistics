# All code for this program directly contributed by Preston Thomas

import sqlalchemy as sql
import pandas as pd

# Establish database connection
# Might have to modify depending on your local database configuration
# Password will likely be different on your own installation
engine = sql.create_engine("postgresql+psycopg2://postgres:nfl_football_rocks@localhost:5432/postgres")
adv_rush_ing_query = "SELECT * FROM postgres.nfl_data.advstats_week_rush WHERE season = 2024"
pass_ing_query = "SELECT * FROM postgres.nfl_data.ngs_passing WHERE season = 2024"
rush_ing_query = "SELECT * FROM postgres.nfl_data.ngs_rushing WHERE season = 2024"
rec_ing_query = "SELECT * FROM postgres.nfl_data.ngs_receiving WHERE season = 2024"

# Processing raw data from SQL databases in pandas dataframes
adv_rush_raw = pd.read_sql_query(adv_rush_ing_query, engine)
pass_raw = pd.read_sql_query(pass_ing_query, engine)
rush_raw = pd.read_sql_query(rush_ing_query, engine)
rec_raw = pd.read_sql_query(rec_ing_query, engine)