# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.sftp_output import SftpOutput
from bitmovin_python.encoding.outputs.sftp.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.outputs.sftp.sftp_outputs_list_query_params import SftpOutputsListQueryParams


class SftpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(SftpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, sftp_output=None, **kwargs):
        """Create SFTP Output"""

        return self.api_client.post(
            '/encoding/outputs/sftp',
            sftp_output,
            type=SftpOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete SFTP Output"""

        return self.api_client.delete(
            '/encoding/outputs/sftp/{output_id}',
            path_params={'output_id': output_id},
            type=SftpOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """SFTP Output Details"""

        return self.api_client.get(
            '/encoding/outputs/sftp/{output_id}',
            path_params={'output_id': output_id},
            type=SftpOutput,
            **kwargs
        )

    def list(self, query_params: SftpOutputsListQueryParams = None, **kwargs):
        """List SFTP Outputs"""

        return self.api_client.get(
            '/encoding/outputs/sftp',
            query_params=query_params,
            pagination_response=True,
            type=SftpOutput,
            **kwargs
        )
