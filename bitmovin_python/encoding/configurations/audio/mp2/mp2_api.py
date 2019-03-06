# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.mp2_audio_configuration import Mp2AudioConfiguration
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.configurations.audio.mp2.customdata.customdata_api import CustomdataApi


class Mp2Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Mp2Api, self).__init__(
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

    def create(self, mp2_audio_configuration=None, **kwargs):
        """Create MP2 Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/audio/mp2',
            mp2_audio_configuration,
            type=Mp2AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete MP2 Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/audio/mp2/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """MP2 Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/audio/mp2/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Mp2AudioConfiguration,
            **kwargs
        )
