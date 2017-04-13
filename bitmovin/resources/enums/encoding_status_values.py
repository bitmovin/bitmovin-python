import enum


class EncodingStatusValues(enum.Enum):
    RUNNING = 'RUNNING'
    QUEUED = 'QUEUED'
    CREATED = 'CREATED'
    FINISHED = 'FINISHED'
    ERROR = 'ERROR'
