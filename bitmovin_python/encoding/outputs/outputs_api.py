# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.output import Output
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.outputs.type.type_api import TypeApi
from bitmovin_python.encoding.outputs.s3.s3_api import S3Api
from bitmovin_python.encoding.outputs.s3RoleBased.s3_role_based_api import S3RoleBasedApi
from bitmovin_python.encoding.outputs.genericS3.generic_s3_api import GenericS3Api
from bitmovin_python.encoding.outputs.local.local_api import LocalApi
from bitmovin_python.encoding.outputs.gcs.gcs_api import GcsApi
from bitmovin_python.encoding.outputs.azure.azure_api import AzureApi
from bitmovin_python.encoding.outputs.ftp.ftp_api import FtpApi
from bitmovin_python.encoding.outputs.sftp.sftp_api import SftpApi
from bitmovin_python.encoding.outputs.akamaiNetstorage.akamai_netstorage_api import AkamaiNetstorageApi
from bitmovin_python.encoding.outputs.outputs_list_query_params import OutputsListQueryParams


class OutputsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(OutputsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.type = TypeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.s3 = S3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.s3RoleBased = S3RoleBasedApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.genericS3 = GenericS3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.local = LocalApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.gcs = GcsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.azure = AzureApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.ftp = FtpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.sftp = SftpApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.akamaiNetstorage = AkamaiNetstorageApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def list(self, query_params: OutputsListQueryParams = None, **kwargs):
        """List all Outputs"""

        return self.api_client.get(
            '/encoding/outputs',
            query_params=query_params,
            pagination_response=True,
            type=Output,
            **kwargs
        )
