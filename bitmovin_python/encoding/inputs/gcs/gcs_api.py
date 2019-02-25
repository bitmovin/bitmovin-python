# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.gcs_input import GcsInput
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.inputs.gcs.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.inputs.gcs.gcs_inputs_list_query_params import GcsInputsListQueryParams


class GcsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(GcsApi, self).__init__(
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

    def create(self, gcs_input=None, **kwargs):
        """Create GCS Input"""

        return self.api_client.post(
            '/encoding/inputs/gcs',
            gcs_input,
            type=GcsInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete GCS Input"""

        return self.api_client.delete(
            '/encoding/inputs/gcs/{input_id}',
            path_params={'input_id': input_id},
            type=GcsInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """GCS Input Details"""

        return self.api_client.get(
            '/encoding/inputs/gcs/{input_id}',
            path_params={'input_id': input_id},
            type=GcsInput,
            **kwargs
        )

    def list(self, query_params: GcsInputsListQueryParams = None, **kwargs):
        """List GCS Inputs"""

        return self.api_client.get(
            '/encoding/inputs/gcs',
            query_params=query_params,
            pagination_response=True,
            type=GcsInput,
            **kwargs
        )
