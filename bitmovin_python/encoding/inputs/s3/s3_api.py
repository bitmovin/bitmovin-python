# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.s3_input import S3Input
from bitmovin_python.encoding.inputs.s3.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.inputs.s3.s3_inputs_list_query_params import S3InputsListQueryParams


class S3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(S3Api, self).__init__(
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

    def create(self, s3_input=None, **kwargs):
        """Create S3 Input"""

        return self.api_client.post(
            '/encoding/inputs/s3',
            s3_input,
            type=S3Input,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete S3 Input"""

        return self.api_client.delete(
            '/encoding/inputs/s3/{input_id}',
            path_params={'input_id': input_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """S3 Input Details"""

        return self.api_client.get(
            '/encoding/inputs/s3/{input_id}',
            path_params={'input_id': input_id},
            type=S3Input,
            **kwargs
        )

    def list(self, query_params: S3InputsListQueryParams = None, **kwargs):
        """List S3 Inputs"""

        return self.api_client.get(
            '/encoding/inputs/s3',
            query_params=query_params,
            pagination_response=True,
            type=S3Input,
            **kwargs
        )
