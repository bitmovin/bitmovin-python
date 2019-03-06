# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.audio.audio_api import AudioApi
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.video.video_api import VideoApi
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.subtitle.subtitle_api import SubtitleApi
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.custom.custom_api import CustomApi
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.representations.representations_api import RepresentationsApi
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.contentprotection.contentprotection_api import ContentprotectionApi


class AdaptationsetsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AdaptationsetsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.audio = AudioApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.video = VideoApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.subtitle = SubtitleApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.custom = CustomApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.representations = RepresentationsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.contentprotection = ContentprotectionApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
