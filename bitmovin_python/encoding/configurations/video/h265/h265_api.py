# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.h265_video_configuration import H265VideoConfiguration
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.configurations.video.h265.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.configurations.video.h265.h265_video_configurations_list_query_params import H265VideoConfigurationsListQueryParams


class H265Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(H265Api, self).__init__(
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

    def create(self, h265_video_configuration=None, **kwargs):
        """Create H265/HEVC Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/video/h265',
            h265_video_configuration,
            type=H265VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete H265/HEVC Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/video/h265/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """H265/HEVC Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/video/h265/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=H265VideoConfiguration,
            **kwargs
        )

    def list(self, query_params: H265VideoConfigurationsListQueryParams = None, **kwargs):
        """List H265/HEVC Codec Configurations"""

        return self.api_client.get(
            '/encoding/configurations/video/h265',
            query_params=query_params,
            pagination_response=True,
            type=H265VideoConfiguration,
            **kwargs
        )
