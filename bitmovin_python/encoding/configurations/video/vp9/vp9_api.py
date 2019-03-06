# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.vp9_video_configuration import Vp9VideoConfiguration
from bitmovin_python.encoding.configurations.video.vp9.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.configurations.video.vp9.vp9_video_configurations_list_query_params import Vp9VideoConfigurationsListQueryParams


class Vp9Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Vp9Api, self).__init__(
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

    def create(self, vp9_video_configuration=None, **kwargs):
        """Create VP9 Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/video/vp9',
            vp9_video_configuration,
            type=Vp9VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete VP9 Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/video/vp9/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """VP9 Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/video/vp9/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Vp9VideoConfiguration,
            **kwargs
        )

    def list(self, query_params: Vp9VideoConfigurationsListQueryParams = None, **kwargs):
        """List VP9 Codec Configurations"""

        return self.api_client.get(
            '/encoding/configurations/video/vp9',
            query_params=query_params,
            pagination_response=True,
            type=Vp9VideoConfiguration,
            **kwargs
        )
