# Python NFL Statistics Machine Learning & Modeling Project

This will hone my machine-learning and data engineering skills while exploring some of my greatest passions in life - NFL football, fantasy football, and advanced metrics.

More coming soon...

# Anticipated Requirements
* DBeaver or another database manager of your choice
* A local PostgreSQL installation
* Python
*  psycopg2 Python package for SQL connection to PostgreSQL database, pandas for data manipulation

# Run Instructions
**FAIR WARNING**: The current SQL script that creates the database and loads the initial data into the tables is massive. This might lead to performance issues when initially creating the database, depending on your hardware & database manager. I will try to come up with a way to split this into a few digestible SQL scripts, rather than one huge one. The likely approach will be to have one script create the database & tables, and then have a separate script for each table to load the table with data. Coming soon...
* You will need to download the database dump located in the SQL directory and run it in your local database manager
* You will then need to establish a connection to your local PostgreSQL database, using the connection string, which is found at the top of the data_ingestion.py file
* More TBD...

# Citations
All data currently in the database contributed from the CSVs found here: zackthoutt/nfl-player-stats. This repository contains the source code responsible for scraping data from multiple sources weekly.
