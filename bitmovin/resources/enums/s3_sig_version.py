import enum

class S3SignatureVersion(enum.Enum):
    S3_V2 = "S3_V2"
    S3_V4 = "S3_V4"
    