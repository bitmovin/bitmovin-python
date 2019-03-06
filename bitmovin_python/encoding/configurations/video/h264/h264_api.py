# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.h264_video_configuration import H264VideoConfiguration
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.configurations.video.h264.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.configurations.video.h264.h264_video_configurations_list_query_params import H264VideoConfigurationsListQueryParams


class H264Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(H264Api, self).__init__(
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

    def create(self, h264_video_configuration=None, **kwargs):
        """Create H264/AVC Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/video/h264',
            h264_video_configuration,
            type=H264VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete H264/AVC Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/video/h264/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """H264/AVC Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/video/h264/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=H264VideoConfiguration,
            **kwargs
        )

    def list(self, query_params: H264VideoConfigurationsListQueryParams = None, **kwargs):
        """List H264/AVC Codec Configurations"""

        return self.api_client.get(
            '/encoding/configurations/video/h264',
            query_params=query_params,
            pagination_response=True,
            type=H264VideoConfiguration,
            **kwargs
        )
