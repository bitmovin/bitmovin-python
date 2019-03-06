# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.codec_configuration import CodecConfiguration
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.configurations.type.type_api import TypeApi
from bitmovin_python.encoding.configurations.video.video_api import VideoApi
from bitmovin_python.encoding.configurations.audio.audio_api import AudioApi
from bitmovin_python.encoding.configurations.codec_configurations_list_query_params import CodecConfigurationsListQueryParams


class ConfigurationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ConfigurationsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.type = TypeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.video = VideoApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.audio = AudioApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: CodecConfigurationsListQueryParams = None, **kwargs):
        """List all Codec Configurations"""

        return self.api_client.get(
            '/encoding/configurations',
            query_params=query_params,
            pagination_response=True,
            type=CodecConfiguration,
            **kwargs
        )
