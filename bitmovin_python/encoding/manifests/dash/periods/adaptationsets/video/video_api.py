# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.adaptation_set import AdaptationSet
from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.video_adaptation_set import VideoAdaptationSet
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.video.video_adaptation_sets_list_query_params import VideoAdaptationSetsListQueryParams


class VideoApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(VideoApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, manifest_id, period_id, video_adaptation_set=None, **kwargs):
        """Add Video AdaptationSet"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/video',
            video_adaptation_set,
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=VideoAdaptationSet,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, **kwargs):
        """Delete Video AdaptationSet"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/video/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, **kwargs):
        """Video AdaptationSet Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/video/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=VideoAdaptationSet,
            **kwargs
        )

    def list(self, manifest_id, period_id, query_params: VideoAdaptationSetsListQueryParams = None, **kwargs):
        """List all Video AdaptationSets"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/video',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            query_params=query_params,
            pagination_response=True,
            type=VideoAdaptationSet,
            **kwargs
        )
