from bitmovin.bitmovin_object import BitmovinObject
from .s3_output_service import S3
from .gcs_output_service import GCS
from .azure_output_service import Azure
from .ftp_output_service import FTP
from .sftp_output_service import SFTP


class OutputService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.S3 = S3(http_client=self.http_client)
        self.GCS = GCS(http_client=self.http_client)
        self.Azure = Azure(http_client=self.http_client)
        self.FTP = FTP(http_client=self.http_client)
        self.SFTP = SFTP(http_client=self.http_client)
