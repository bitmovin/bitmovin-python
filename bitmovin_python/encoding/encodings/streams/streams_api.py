# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.stream import Stream
from bitmovin_python.encoding.encodings.streams.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.streams.input.input_api import InputApi
from bitmovin_python.encoding.encodings.streams.inputs.inputs_api import InputsApi
from bitmovin_python.encoding.encodings.streams.filters.filters_api import FiltersApi
from bitmovin_python.encoding.encodings.streams.subtitles.subtitles_api import SubtitlesApi
from bitmovin_python.encoding.encodings.streams.burnInSubtitles.burn_in_subtitles_api import BurnInSubtitlesApi
from bitmovin_python.encoding.encodings.streams.captions.captions_api import CaptionsApi
from bitmovin_python.encoding.encodings.streams.thumbnails.thumbnails_api import ThumbnailsApi
from bitmovin_python.encoding.encodings.streams.sprites.sprites_api import SpritesApi
from bitmovin_python.encoding.encodings.streams.streams_list_query_params import StreamsListQueryParams


class StreamsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(StreamsApi, self).__init__(
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

        self.input = InputApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.inputs = InputsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.filters = FiltersApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.subtitles = SubtitlesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.burnInSubtitles = BurnInSubtitlesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.captions = CaptionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.thumbnails = ThumbnailsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.sprites = SpritesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, encoding_id, stream=None, **kwargs):
        """Add Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams',
            stream,
            path_params={'encoding_id': encoding_id},
            type=Stream,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, **kwargs):
        """Delete Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, **kwargs):
        """Stream Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=Stream,
            **kwargs
        )

    def list(self, encoding_id, query_params: StreamsListQueryParams = None, **kwargs):
        """List Streams"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Stream,
            **kwargs
        )
