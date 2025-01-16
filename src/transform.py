import store_data as sd


if __name__ == "__main__":
    for obj in sd.datasets:
        print(obj.get_query())

# TODO: I think I want to narrow the scope of this project, comparing QBR to fantasy football performance, and then using QBR against matchups to try and predict the strongest fantasy football starts (standard full-PPR scoring)
# Another idea would be to make a player/team search tool & provide advanced stats
# Full PPR scoring: .04 points per passing yards, .1 per rush yard, 4 point passing TDs, 6 point rush/receiving TDs
# Putting this on pause for now until I can narrow & understand intended scope