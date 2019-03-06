# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.media_info_type_response import MediaInfoTypeResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError


class TypeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TypeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, manifest_id, media_id, **kwargs):
        """HLS Media Type"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/{media_id}/type',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=MediaInfoTypeResponse,
            **kwargs
        )
