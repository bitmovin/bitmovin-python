# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.s3_output import S3Output
from bitmovin_python.encoding.outputs.s3.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.outputs.s3.s3_outputs_list_query_params import S3OutputsListQueryParams


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

    def create(self, s3_output=None, **kwargs):
        """Create S3 Output"""

        return self.api_client.post(
            '/encoding/outputs/s3',
            s3_output,
            type=S3Output,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete S3 Output"""

        return self.api_client.delete(
            '/encoding/outputs/s3/{output_id}',
            path_params={'output_id': output_id},
            type=S3Output,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """S3 Output Details"""

        return self.api_client.get(
            '/encoding/outputs/s3/{output_id}',
            path_params={'output_id': output_id},
            type=S3Output,
            **kwargs
        )

    def list(self, query_params: S3OutputsListQueryParams = None, **kwargs):
        """List S3 Outputs"""

        return self.api_client.get(
            '/encoding/outputs/s3',
            query_params=query_params,
            pagination_response=True,
            type=S3Output,
            **kwargs
        )
