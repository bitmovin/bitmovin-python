# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.frame_id_id3_tag import FrameIdId3Tag
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.muxings.progressiveTs.id3.frameId.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.muxings.progressiveTs.id3.frameId.frame_id_id3_tags_list_query_params import FrameIdId3TagsListQueryParams


class FrameIdApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(FrameIdApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, frame_id_id3_tag=None, **kwargs):
        """Add Frame ID ID3 Tag to Progressive TS Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/frame-id',
            frame_id_id3_tag,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=FrameIdId3Tag,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, id3_tag_id, **kwargs):
        """Delete Frame ID ID3 Tag of Progressive TS Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/frame-id/{id3_tag_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'id3_tag_id': id3_tag_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, id3_tag_id, **kwargs):
        """Frame ID ID3 Tag Details of Progressive TS Muxing"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/frame-id/{id3_tag_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'id3_tag_id': id3_tag_id},
            type=FrameIdId3Tag,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: FrameIdId3TagsListQueryParams = None, **kwargs):
        """List Frame ID ID3 Tags of Progressive TS Muxing"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/frame-id',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=FrameIdId3Tag,
            **kwargs
        )
