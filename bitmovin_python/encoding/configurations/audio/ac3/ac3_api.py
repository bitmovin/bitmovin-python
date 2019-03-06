# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.ac3_audio_configuration import Ac3AudioConfiguration
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.configurations.audio.ac3.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.configurations.audio.ac3.ac3_audio_configurations_list_query_params import Ac3AudioConfigurationsListQueryParams


class Ac3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Ac3Api, self).__init__(
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

    def create(self, ac3_audio_configuration=None, **kwargs):
        """Create AC3 Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/audio/ac3',
            ac3_audio_configuration,
            type=Ac3AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete AC3 Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/audio/ac3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """AC3 Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/audio/ac3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Ac3AudioConfiguration,
            **kwargs
        )

    def list(self, query_params: Ac3AudioConfigurationsListQueryParams = None, **kwargs):
        """List AC3 Configurations"""

        return self.api_client.get(
            '/encoding/configurations/audio/ac3',
            query_params=query_params,
            pagination_response=True,
            type=Ac3AudioConfiguration,
            **kwargs
        )
