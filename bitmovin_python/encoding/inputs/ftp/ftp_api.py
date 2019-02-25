# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.ftp_input import FtpInput
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.inputs.ftp.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.inputs.ftp.ftp_inputs_list_query_params import FtpInputsListQueryParams


class FtpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(FtpApi, self).__init__(
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

    def create(self, ftp_input=None, **kwargs):
        """Create FTP Input"""

        return self.api_client.post(
            '/encoding/inputs/ftp',
            ftp_input,
            type=FtpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete FTP Input"""

        return self.api_client.delete(
            '/encoding/inputs/ftp/{input_id}',
            path_params={'input_id': input_id},
            type=FtpInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """FTP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/ftp/{input_id}',
            path_params={'input_id': input_id},
            type=FtpInput,
            **kwargs
        )

    def list(self, query_params: FtpInputsListQueryParams = None, **kwargs):
        """List FTP Inputs"""

        return self.api_client.get(
            '/encoding/inputs/ftp',
            query_params=query_params,
            pagination_response=True,
            type=FtpInput,
            **kwargs
        )
