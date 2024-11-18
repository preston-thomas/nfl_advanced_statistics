import store_data as sd


if __name__ == "__main__":
    for obj in sd.datasets:
        print(obj.get_query())