# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.input import Input
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.inputs.type.type_api import TypeApi
from bitmovin_python.encoding.inputs.rtmp.rtmp_api import RtmpApi
from bitmovin_python.encoding.inputs.redundantRtmp.redundant_rtmp_api import RedundantRtmpApi
from bitmovin_python.encoding.inputs.s3.s3_api import S3Api
from bitmovin_python.encoding.inputs.s3RoleBased.s3_role_based_api import S3RoleBasedApi
from bitmovin_python.encoding.inputs.genericS3.generic_s3_api import GenericS3Api
from bitmovin_python.encoding.inputs.local.local_api import LocalApi
from bitmovin_python.encoding.inputs.gcs.gcs_api import GcsApi
from bitmovin_python.encoding.inputs.azure.azure_api import AzureApi
from bitmovin_python.encoding.inputs.ftp.ftp_api import FtpApi
from bitmovin_python.encoding.inputs.sftp.sftp_api import SftpApi
from bitmovin_python.encoding.inputs.http.http_api import HttpApi
from bitmovin_python.encoding.inputs.https.https_api import HttpsApi
from bitmovin_python.encoding.inputs.aspera.aspera_api import AsperaApi
from bitmovin_python.encoding.inputs.akamaiNetstorage.akamai_netstorage_api import AkamaiNetstorageApi
from bitmovin_python.encoding.inputs.tcp.tcp_api import TcpApi
from bitmovin_python.encoding.inputs.udp.udp_api import UdpApi
from bitmovin_python.encoding.inputs.udpMulticast.udp_multicast_api import UdpMulticastApi
from bitmovin_python.encoding.inputs.zixi.zixi_api import ZixiApi
from bitmovin_python.encoding.inputs.inputs_list_query_params import InputsListQueryParams


class InputsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(InputsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.type = TypeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.rtmp = RtmpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.redundantRtmp = RedundantRtmpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.s3 = S3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.s3RoleBased = S3RoleBasedApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.genericS3 = GenericS3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.local = LocalApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.gcs = GcsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.azure = AzureApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.ftp = FtpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.sftp = SftpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.http = HttpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.https = HttpsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.aspera = AsperaApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.akamaiNetstorage = AkamaiNetstorageApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.tcp = TcpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.udp = UdpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.udpMulticast = UdpMulticastApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.zixi = ZixiApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: InputsListQueryParams = None, **kwargs):
        """List all Inputs"""

        return self.api_client.get(
            '/encoding/inputs',
            query_params=query_params,
            pagination_response=True,
            type=Input,
            **kwargs
        )
