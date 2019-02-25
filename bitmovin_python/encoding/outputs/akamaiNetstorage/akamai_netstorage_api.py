# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.akamai_net_storage_output import AkamaiNetStorageOutput
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.outputs.akamaiNetstorage.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.outputs.akamaiNetstorage.akamai_net_storage_outputs_list_query_params import AkamaiNetStorageOutputsListQueryParams


class AkamaiNetstorageApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(AkamaiNetstorageApi, self).__init__(
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

    def create(self, akamai_net_storage_output=None, **kwargs):
        """Create Akamai NetStorage Output"""

        return self.api_client.post(
            '/encoding/outputs/akamai-netstorage',
            akamai_net_storage_output,
            type=AkamaiNetStorageOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete Akamai NetStorage Output"""

        return self.api_client.delete(
            '/encoding/outputs/akamai-netstorage/{output_id}',
            path_params={'output_id': output_id},
            type=AkamaiNetStorageOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """Akamai NetStorage Output Details"""

        return self.api_client.get(
            '/encoding/outputs/akamai-netstorage/{output_id}',
            path_params={'output_id': output_id},
            type=AkamaiNetStorageOutput,
            **kwargs
        )

    def list(self, query_params: AkamaiNetStorageOutputsListQueryParams = None, **kwargs):
        """List Akamai NetStorage Outputs"""

        return self.api_client.get(
            '/encoding/outputs/akamai-netstorage',
            query_params=query_params,
            pagination_response=True,
            type=AkamaiNetStorageOutput,
            **kwargs
        )
