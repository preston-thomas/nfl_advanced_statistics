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
    o_line.set_query("select SUM(rushing_yards_before_contact_avg) as szn_rush_yds_before_contact_avg_sum, MAX(team) as team, sum(carries) as szn_carries from nfl_data.ADVSTATS_WEEK_RUSH where season = 2024 and week <= 17 group by team order by SUM(rushing_yards_before_contact_avg) desc")
    o_line.set_dataframe(pd.read_sql_query(o_line.get_query(), di.engine))
    player_statistics = dict(zip(o_line.get_dataframe()["szn_rush_yds_before_contact_avg_sum"], o_line.get_dataframe()["team"]))
    return o_line

# Running back efficiency, rushing yards over expected per carry
def process_rb_roe_query() -> di.Dataset:
    rb_roe = di.Dataset()
    rb_roe.set_query("select efficiency, player_display_name, (cast(rush_yards_over_expected as decimal)/rush_attempts) as rush_over_exp_pg, team_abbr from nfl_data.ngs_rushing where season = 2024 and week = 0 order by rush_over_exp_pg desc")
    rb_roe.set_dataframe(pd.read_sql_query(rb_roe.get_query(), di.engine))
    return rb_roe