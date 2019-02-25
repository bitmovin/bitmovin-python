
class DailyStatisticsPerLabelsListByDateRangeQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, labels: str = None, *args, **kwargs):
        super(DailyStatisticsPerLabelsListByDateRangeQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
        self.labels = labels
