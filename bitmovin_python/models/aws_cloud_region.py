# coding: utf-8
from enum import Enum


class AwsCloudRegion(Enum):
    """
    allowed enum values
    """
    US_EAST_1 = "US_EAST_1"
    US_EAST_2 = "US_EAST_2"
    US_WEST_1 = "US_WEST_1"
    US_WEST_2 = "US_WEST_2"
    EU_WEST_1 = "EU_WEST_1"
    EU_CENTRAL_1 = "EU_CENTRAL_1"
    AP_SOUTHEAST_1 = "AP_SOUTHEAST_1"
    AP_SOUTHEAST_2 = "AP_SOUTHEAST_2"
    AP_NORTHEAST_1 = "AP_NORTHEAST_1"
    AP_NORTHEAST_2 = "AP_NORTHEAST_2"
    AP_SOUTH_1 = "AP_SOUTH_1"
    SA_EAST_1 = "SA_EAST_1"
