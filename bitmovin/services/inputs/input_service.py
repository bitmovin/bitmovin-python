from bitmovin.bitmovin_object import BitmovinObject
from .s3_input_service import S3
from .gcs_input_service import GCS
from .azure_input_service import Azure
from .ftp_input_service import FTP
from .sftp_input_service import SFTP
from .http_input_service import HTTP
from .https_input_service import HTTPS
from .aspera_input_service import Aspera
from .rtmp_input_service import RTMP
from .generic_s3_input_service import GenericS3
from .local_input_service import Local
from .zixi_input_service import Zixi


class InputService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.S3 = S3(http_client=self.http_client)
        self.GCS = GCS(http_client=self.http_client)
        self.Azure = Azure(http_client=self.http_client)
        self.FTP = FTP(http_client=self.http_client)
        self.SFTP = SFTP(http_client=self.http_client)
        self.HTTP = HTTP(http_client=self.http_client)
        self.HTTPS = HTTPS(http_client=self.http_client)
        self.Aspera = Aspera(http_client=self.http_client)
        self.RTMP = RTMP(http_client=self.http_client)
        self.GenericS3 = GenericS3(http_client=self.http_client)
        self.Local = Local(http_client=self.http_client)
        self.Zixi = Zixi(http_client=self.http_client)
