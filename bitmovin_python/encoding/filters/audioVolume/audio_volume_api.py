# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.audio_volume_filter import AudioVolumeFilter
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.filters.audioVolume.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.filters.audioVolume.audio_volume_filters_list_query_params import AudioVolumeFiltersListQueryParams


class AudioVolumeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(AudioVolumeApi, self).__init__(
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

    def create(self, audio_volume_filter=None, **kwargs):
        """Create Audio Volume Filter"""

        return self.api_client.post(
            '/encoding/filters/audio-volume',
            audio_volume_filter,
            type=AudioVolumeFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Audio Volume Filter"""

        return self.api_client.delete(
            '/encoding/filters/audio-volume/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Audio Volume Filter Details"""

        return self.api_client.get(
            '/encoding/filters/audio-volume/{filter_id}',
            path_params={'filter_id': filter_id},
            type=AudioVolumeFilter,
            **kwargs
        )

    def list(self, query_params: AudioVolumeFiltersListQueryParams = None, **kwargs):
        """List Audio Volume Filters"""

        return self.api_client.get(
            '/encoding/filters/audio-volume',
            query_params=query_params,
            pagination_response=True,
            type=AudioVolumeFilter,
            **kwargs
        )
