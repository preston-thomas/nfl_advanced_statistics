import data_ingestion as di

class Dataset:

    def __init__(self, query, df):
        self.query = query
        self.df = df
        self.mean = 0
        self.avg = 0
        self.median = 0
        self.mode = 0

    def set_query(self, query):
        self.query = query

    def get_query(self):
        return self.query
    
    def set_mean(self, mean):
        self.mean = mean

    def get_mean(self):
        return self.mean
    
    def set_avg(self, avg):
        self.avg = avg

    def get_avg(self):
        return self.avg
    
    def set_median(self, median):
        self.median = median

    def get_median(self):
        return self.median
    
    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode
    
combine = Dataset(di.combine_query, di.combine_raw)
player = Dataset(di.player_query, di.player_raw)
qbr_szn = Dataset(di.qbr_szn_query, di.qbr_szn_raw)
qbr_week = Dataset(di.qbr_week_query, di.qbr_week_raw)
rosters = Dataset(di.roster_query, di.rosters_raw)

datasets = []
datasets.append(combine)
datasets.append(player)
datasets.append(qbr_szn)
datasets.append(qbr_week)
datasets.append(rosters)