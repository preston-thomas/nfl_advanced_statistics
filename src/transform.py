import store_data as sd


if __name__ == "__main__":
    for obj in sd.datasets:
        print(obj.get_query())

#TODO: I think I want to narrow the scope of this project, comparing QBR to fantasy football performance, and then using QBR against matchups to try and predict the strongest fantasy football starts (standard full-PPR scoring)
#Will try to consider rushing statistics, as well.
