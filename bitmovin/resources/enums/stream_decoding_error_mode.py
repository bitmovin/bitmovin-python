from enum import Enum


class StreamDecodingErrorMode(Enum):
    FAIL_ON_ERROR = 'FAIL_ON_ERROR'
    DUPLICATE_FRAMES = 'DUPLICATE_FRAMES'
