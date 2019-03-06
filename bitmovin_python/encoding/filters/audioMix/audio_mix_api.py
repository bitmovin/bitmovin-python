# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.audio_mix_filter import AudioMixFilter
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.filters.audioMix.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.filters.audioMix.audio_mix_filters_list_query_params import AudioMixFiltersListQueryParams


class AudioMixApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AudioMixApi, self).__init__(
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

    def create(self, audio_mix_filter=None, **kwargs):
        """Create Audio Mix Filter"""

        return self.api_client.post(
            '/encoding/filters/audio-mix',
            audio_mix_filter,
            type=AudioMixFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Audio Mix Filter"""

        return self.api_client.delete(
            '/encoding/filters/audio-mix/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Audio Mix Filter Details"""

        return self.api_client.get(
            '/encoding/filters/audio-mix/{filter_id}',
            path_params={'filter_id': filter_id},
            type=AudioMixFilter,
            **kwargs
        )

    def list(self, query_params: AudioMixFiltersListQueryParams = None, **kwargs):
        """List Audio Mix Filters"""

        return self.api_client.get(
            '/encoding/filters/audio-mix',
            query_params=query_params,
            pagination_response=True,
            type=AudioMixFilter,
            **kwargs
        )
