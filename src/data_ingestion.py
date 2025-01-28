# All code for this program directly contributed by Preston Thomas

import sqlalchemy as sql
import pandas as pd

class Dataset:

# Getters, setters for datasets
    def __init__(self):
        self.query = None
        self.dataframe = None

    def set_query(self, query: str) -> None:
        self.query = query

    def get_query(self) -> str:
        return self.query
    
    def set_dataframe(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

    def get_dataframe(self) -> pd.DataFrame:
        return self.dataframe
    
# Establish database connection
# Might have to modify depending on your local database configuration
# Password will likely be different on your own installation
engine = sql.create_engine("postgresql+psycopg2://postgres:nfl_football_rocks@localhost:5432/postgres")
# Basic queries for each dataset, filtering out historical data

def process_raw_data() -> list[Dataset]:
    # Emtpy list to store datasets as they're made
    datasets = []
    # Create dataset objects
    rushing = Dataset()
    receiving = Dataset()
    passing = Dataset()
    adv_rush = Dataset()
    # Basic queries for each dataset, filtering out historical data
    adv_rush.set_query("SELECT * FROM postgres.nfl_data.advstats_week_rush WHERE season = 2024")
    passing.set_query("SELECT * FROM postgres.nfl_data.ngs_passing WHERE season = 2024")
    rushing.set_query("SELECT * FROM postgres.nfl_data.ngs_rushing WHERE season = 2024")
    receiving.set_query("SELECT * FROM postgres.nfl_data.ngs_receiving WHERE season = 2024")
    # Set the dataframes, ingesting the raw SQL data
    adv_rush.set_dataframe(pd.read_sql_query(adv_rush.get_query(), engine))
    passing.set_dataframe(pd.read_sql_query(passing.get_query(), engine))
    rushing.set_dataframe(pd.read_sql_query(rushing.get_query(), engine))
    receiving.set_dataframe(pd.read_sql_query(receiving.get_query(), engine))
    # Append each dataset object to the list & return it
    datasets.append(rushing)
    datasets.append(receiving)
    datasets.append(passing)
    datasets.append(adv_rush)
    return datasets