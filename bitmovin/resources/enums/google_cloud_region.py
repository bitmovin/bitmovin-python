import enum


class GoogleCloudRegion(enum.Enum):
    ASIA_EAST_1 = 'ASIA_EAST_1'
    EUROPE_WEST_1 = 'EUROPE_WEST_1'
    US_CENTRAL_1 = 'US_CENTRAL_1'
    US_EAST_1 = 'US_EAST_1'
    US_WEST_1 = 'US_WEST_1'

    @staticmethod
    def default():
        return GoogleCloudRegion.EUROPE_WEST_1
