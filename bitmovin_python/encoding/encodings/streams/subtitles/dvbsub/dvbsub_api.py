# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.models.stream_dvb_sub_subtitle import StreamDvbSubSubtitle
from bitmovin_python.encoding.encodings.streams.subtitles.dvbsub.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.streams.subtitles.dvbsub.stream_dvb_sub_subtitles_list_query_params import StreamDvbSubSubtitlesListQueryParams


class DvbsubApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DvbsubApi, self).__init__(
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

    def create(self, encoding_id, stream_id, stream_dvb_sub_subtitle=None, **kwargs):
        """Burn-In DVB-SUB Subtitle into Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/subtitles/dvbsub',
            stream_dvb_sub_subtitle,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=StreamDvbSubSubtitle,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, subtitle_id, **kwargs):
        """Delete Specific DVB-SUB Subtitle from Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/subtitles/dvbsub/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'subtitle_id': subtitle_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, subtitle_id, **kwargs):
        """Subtitle DVB-SUB BurnIn Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/subtitles/dvbsub/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'subtitle_id': subtitle_id},
            type=StreamDvbSubSubtitle,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params: StreamDvbSubSubtitlesListQueryParams = None, **kwargs):
        """List the DVB-SUB subtitles of a stream"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/subtitles/dvbsub',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=StreamDvbSubSubtitle,
            **kwargs
        )
