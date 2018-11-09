import enum


class LiveEncodingMode(enum.Enum):
    STANDARD = 'STANDARD'
    SINGLE_PASS = 'SINGLE_PASS'
    TWO_PASS = 'TWO_PASS'
