import enum


class FTPTransferVersion(enum.Enum):
    V1_0_0 = '1.0.0'
    V1_1_0 = '1.1.0'

    @staticmethod
    def default():
        return FTPTransferVersion.V1_0_0
