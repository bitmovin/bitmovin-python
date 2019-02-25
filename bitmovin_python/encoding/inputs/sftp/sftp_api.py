# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.sftp_input import SftpInput
from bitmovin_python.encoding.inputs.sftp.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.inputs.sftp.sftp_inputs_list_query_params import SftpInputsListQueryParams


class SftpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(SftpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, sftp_input=None, **kwargs):
        """Create SFTP Input"""

        return self.api_client.post(
            '/encoding/inputs/sftp',
            sftp_input,
            type=SftpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete SFTP Input"""

        return self.api_client.delete(
            '/encoding/inputs/sftp/{input_id}',
            path_params={'input_id': input_id},
            type=SftpInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """SFTP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/sftp/{input_id}',
            path_params={'input_id': input_id},
            type=SftpInput,
            **kwargs
        )

    def list(self, query_params: SftpInputsListQueryParams = None, **kwargs):
        """List SFTP Inputs"""

        return self.api_client.get(
            '/encoding/inputs/sftp',
            query_params=query_params,
            pagination_response=True,
            type=SftpInput,
            **kwargs
        )
