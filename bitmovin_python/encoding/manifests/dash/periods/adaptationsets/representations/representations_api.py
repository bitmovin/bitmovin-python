# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.representations.vtt.vtt_api import VttApi
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.representations.sidecar.sidecar_api import SidecarApi
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.representations.fmp4.fmp4_api import Fmp4Api
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.representations.mp4.mp4_api import Mp4Api
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.representations.webm.webm_api import WebmApi


class RepresentationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(RepresentationsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.vtt = VttApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.sidecar = SidecarApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.fmp4 = Fmp4Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mp4 = Mp4Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.webm = WebmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
