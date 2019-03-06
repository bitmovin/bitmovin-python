# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.he_aac_v2_audio_configuration import HeAacV2AudioConfiguration
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.configurations.audio.heAacV2.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.configurations.audio.heAacV2.he_aac_v2_audio_configurations_list_query_params import HeAacV2AudioConfigurationsListQueryParams


class HeAacV2Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(HeAacV2Api, self).__init__(
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

    def create(self, he_aac_v2_audio_configuration=None, **kwargs):
        """Create HE-AAC v2 Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/audio/he-aac-v2',
            he_aac_v2_audio_configuration,
            type=HeAacV2AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete HE-AAC v2 Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/audio/he-aac-v2/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """HE-AAC v2 Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/audio/he-aac-v2/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=HeAacV2AudioConfiguration,
            **kwargs
        )

    def list(self, query_params: HeAacV2AudioConfigurationsListQueryParams = None, **kwargs):
        """List HE-AAC v2 Configurations"""

        return self.api_client.get(
            '/encoding/configurations/audio/he-aac-v2',
            query_params=query_params,
            pagination_response=True,
            type=HeAacV2AudioConfiguration,
            **kwargs
        )
