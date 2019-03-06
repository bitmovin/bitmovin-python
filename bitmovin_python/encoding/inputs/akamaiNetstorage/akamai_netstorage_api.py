# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.akamai_net_storage_input import AkamaiNetStorageInput
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.inputs.akamaiNetstorage.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.inputs.akamaiNetstorage.akamai_net_storage_inputs_list_query_params import AkamaiNetStorageInputsListQueryParams


class AkamaiNetstorageApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AkamaiNetstorageApi, self).__init__(
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

    def create(self, akamai_net_storage_input=None, **kwargs):
        """Create Akamai NetStorage Input"""

        return self.api_client.post(
            '/encoding/inputs/akamai-netstorage',
            akamai_net_storage_input,
            type=AkamaiNetStorageInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete Akamai NetStorage Input"""

        return self.api_client.delete(
            '/encoding/inputs/akamai-netstorage/{input_id}',
            path_params={'input_id': input_id},
            type=AkamaiNetStorageInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """Akamai NetStorage Input Details"""

        return self.api_client.get(
            '/encoding/inputs/akamai-netstorage/{input_id}',
            path_params={'input_id': input_id},
            type=AkamaiNetStorageInput,
            **kwargs
        )

    def list(self, query_params: AkamaiNetStorageInputsListQueryParams = None, **kwargs):
        """List Akamai NetStorage Inputs"""

        return self.api_client.get(
            '/encoding/inputs/akamai-netstorage',
            query_params=query_params,
            pagination_response=True,
            type=AkamaiNetStorageInput,
            **kwargs
        )
