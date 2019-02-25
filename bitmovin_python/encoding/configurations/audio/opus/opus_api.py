# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.opus_audio_configuration import OpusAudioConfiguration
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.configurations.audio.opus.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.configurations.audio.opus.opus_audio_configurations_list_query_params import OpusAudioConfigurationsListQueryParams


class OpusApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(OpusApi, self).__init__(
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

    def create(self, opus_audio_configuration=None, **kwargs):
        """Create Opus Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/audio/opus',
            opus_audio_configuration,
            type=OpusAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete Opus Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/audio/opus/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """Opus Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/audio/opus/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=OpusAudioConfiguration,
            **kwargs
        )

    def list(self, query_params: OpusAudioConfigurationsListQueryParams = None, **kwargs):
        """List Opus Configurations"""

        return self.api_client.get(
            '/encoding/configurations/audio/opus',
            query_params=query_params,
            pagination_response=True,
            type=OpusAudioConfiguration,
            **kwargs
        )
