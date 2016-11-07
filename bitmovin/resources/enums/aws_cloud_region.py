import enum


class AWSCloudRegion(enum.Enum):
    AP_NORTHEAST_1 = 'AP_NORTHEAST_1'
    AP_NORTHEAST_2 = 'AP_NORTHEAST_2'
    AP_SOUTHEAST_1 = 'AP_SOUTHEAST_1'
    AP_SOUTHEAST_2 = 'AP_SOUTHEAST_2'
    AP_SOUTH_1 = 'AP_SOUTH_1'
    EU_CENTRAL_1 = 'EU_CENTRAL_1'
    EU_WEST_1 = 'EU_WEST_1'
    SA_EAST_1 = 'SA_EAST_1'
    US_EAST_1 = 'US_EAST_1'
    US_WEST_1 = 'US_WEST_1'
    US_WEST_2 = 'US_WEST_2'

    @staticmethod
    def default():
        return AWSCloudRegion.EU_WEST_1
