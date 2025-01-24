import sqlalchemy as sql
import pandas as pd

# This query attempts to evaluate which teams have the best offensive lines
# Logic: sum the average rush yards before contact, group by each team, order by the highest total
# Short comings: fails to consider running back skill
o_line_query = "SELECT SUM(rushing_yards_before_contact_avg), MAX(team), SUM(carries) FROM nfl_data.ADVSTATS_WEEK_RUSH GROUP BY team ORDER BY SUM(rushing_yards_before_contact_avg) DESC"