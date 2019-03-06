# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.local_output import LocalOutput
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.outputs.local.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.outputs.local.local_outputs_list_query_params import LocalOutputsListQueryParams


class LocalApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(LocalApi, self).__init__(
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

    def create(self, local_output=None, **kwargs):
        """Create Local Output"""

        return self.api_client.post(
            '/encoding/outputs/local',
            local_output,
            type=LocalOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete Local Output"""

        return self.api_client.delete(
            '/encoding/outputs/local/{output_id}',
            path_params={'output_id': output_id},
            type=LocalOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """Local Output Details"""

        return self.api_client.get(
            '/encoding/outputs/local/{output_id}',
            path_params={'output_id': output_id},
            type=LocalOutput,
            **kwargs
        )

    def list(self, query_params: LocalOutputsListQueryParams = None, **kwargs):
        """List Local Outputs"""

        return self.api_client.get(
            '/encoding/outputs/local',
            query_params=query_params,
            pagination_response=True,
            type=LocalOutput,
            **kwargs
        )
