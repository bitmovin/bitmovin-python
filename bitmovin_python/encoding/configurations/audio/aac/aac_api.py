# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.aac_audio_configuration import AacAudioConfiguration
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.configurations.audio.aac.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.configurations.audio.aac.aac_audio_configurations_list_query_params import AacAudioConfigurationsListQueryParams


class AacApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AacApi, self).__init__(
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

    def create(self, aac_audio_configuration=None, **kwargs):
        """Create AAC Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/audio/aac',
            aac_audio_configuration,
            type=AacAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete AAC Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/audio/aac/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """AAC Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/audio/aac/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=AacAudioConfiguration,
            **kwargs
        )

    def list(self, query_params: AacAudioConfigurationsListQueryParams = None, **kwargs):
        """List AAC Configurations"""

        return self.api_client.get(
            '/encoding/configurations/audio/aac',
            query_params=query_params,
            pagination_response=True,
            type=AacAudioConfiguration,
            **kwargs
        )
