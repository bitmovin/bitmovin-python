# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.vp8_video_configuration import Vp8VideoConfiguration
from bitmovin_python.encoding.configurations.video.vp8.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.configurations.video.vp8.vp8_video_configurations_list_query_params import Vp8VideoConfigurationsListQueryParams


class Vp8Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(Vp8Api, self).__init__(
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

    def create(self, vp8_video_configuration=None, **kwargs):
        """Create VP8 Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/video/vp8',
            vp8_video_configuration,
            type=Vp8VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete VP8 Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/video/vp8/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """VP8 Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/video/vp8/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Vp8VideoConfiguration,
            **kwargs
        )

    def list(self, query_params: Vp8VideoConfigurationsListQueryParams = None, **kwargs):
        """get_encoding_configurations_video_vp8"""

        return self.api_client.get(
            '/encoding/configurations/video/vp8',
            query_params=query_params,
            pagination_response=True,
            type=Vp8VideoConfiguration,
            **kwargs
        )
