# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.generic_s3_output import GenericS3Output
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.outputs.genericS3.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.outputs.genericS3.generic_s3_outputs_list_query_params import GenericS3OutputsListQueryParams


class GenericS3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(GenericS3Api, self).__init__(
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

    def create(self, generic_s3_output=None, **kwargs):
        """Create Generic S3 Output"""

        return self.api_client.post(
            '/encoding/outputs/generic-s3',
            generic_s3_output,
            type=GenericS3Output,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete Generic S3 Output"""

        return self.api_client.delete(
            '/encoding/outputs/generic-s3/{output_id}',
            path_params={'output_id': output_id},
            type=GenericS3Output,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """Generic S3 Output Details"""

        return self.api_client.get(
            '/encoding/outputs/generic-s3/{output_id}',
            path_params={'output_id': output_id},
            type=GenericS3Output,
            **kwargs
        )

    def list(self, query_params: GenericS3OutputsListQueryParams = None, **kwargs):
        """List Generic S3 Outputs"""

        return self.api_client.get(
            '/encoding/outputs/generic-s3',
            query_params=query_params,
            pagination_response=True,
            type=GenericS3Output,
            **kwargs
        )
