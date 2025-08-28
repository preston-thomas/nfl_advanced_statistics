import sqlalchemy as sql
import pandas as pd
import data_ingestion as di

# This query attempts to evaluate which teams have the best offensive lines
# Logic: sum the average rush yards before contact, group by each team, order by the highest total
# Short comings: fails to consider running back skill independently from offensive line play
# Example: Kenneth Walker may make Seattle's line look better than they are

# Processing offensive line performance query
# NOTE: This does not consider scheme in yards before contact
# A team who runs more inside zone likely has more yards after contact and less before than a team that runs more outside zone

def process_o_line_query() -> di.Dataset:
    o_line = di.Dataset()
    o_line.set_query("""
        SELECT 
            team, 
            SUM(rushing_yards_before_contact_avg * carries) / SUM(carries) AS szn_rush_yds_before_contact_weighted_avg, 
            SUM(carries) AS szn_carries 
        FROM nfl_data.advstats_week_rush 
        WHERE season = 2024 AND week <= 17 
        GROUP BY team 
        ORDER BY szn_rush_yds_before_contact_weighted_avg DESC
    """)
    o_line.set_dataframe(pd.read_sql_query(o_line.get_query(), di.engine))
    return o_line

def process_rb_roe_query() -> di.Dataset:
    rb_roe = di.Dataset()
    rb_roe.set_query("select efficiency, player_display_name, (cast(rush_yards_over_expected as decimal)/rush_attempts) as rush_over_exp_pg, team_abbr from nfl_data.ngs_rushing where season = 2024 and week = 0 order by rush_over_exp_pg desc")
    rb_roe.set_dataframe(pd.read_sql_query(rb_roe.get_query(), di.engine))
    return rb_roe

def process_wr_query() -> di.Dataset:
    wr = di.Dataset()
    wr.set_query("select avg_yac_above_expectation, player_display_name, catch_percentage, team_abbr from nfl_data.ngs_receiving where season = 2024 and week = 0 order by avg_yac_above_expectation desc")
    wr.set_dataframe(pd.read_sql_query(wr.get_query(), di.engine))
    return wr

def process_qb_query() -> di.Dataset:
    qb = di.Dataset()
    qb.set_query("select completion_percentage_above_expectation, player_display_name, aggressiveness, team_abbr from nfl_data.ngs_passing where season = 2024 and week = 0 order by completion_percentage_above_expectation desc")
    qb.set_dataframe(pd.read_sql_query(qb.get_query(), di.engine))
    return qb