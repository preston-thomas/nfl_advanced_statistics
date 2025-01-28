import sqlalchemy as sql
import pandas as pd
import data_ingestion as di

# This query attempts to evaluate which teams have the best offensive lines
# Logic: sum the average rush yards before contact, group by each team, order by the highest total
# Short comings: fails to consider running back skill
# TODO: Filter on non-playoff games (do not consider playoffs in the calculation)
# TODO: Deepseek LLM integration via local install seems possible, and would add breadth to this project. Investigate how possible this is, see if it can query data to answer user prompts

# Processing offensive line performance query
def process_o_line_query() -> pd.DataFrame:
    o_line = di.Dataset()
    o_line.set_query("SELECT SUM(rushing_yards_before_contact_avg), MAX(team), SUM(carries) FROM nfl_data.ADVSTATS_WEEK_RUSH GROUP BY team ORDER BY SUM(rushing_yards_before_contact_avg) DESC")
    o_line.set_dataframe(pd.read_sql_query(o_line.get_query(), di.engine))
    return o_line
