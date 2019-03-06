# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except
from bitmovin_python.encoding.configurations.audio.aac.aac_api import AacApi
from bitmovin_python.encoding.configurations.audio.heAacV1.he_aac_v1_api import HeAacV1Api
from bitmovin_python.encoding.configurations.audio.heAacV2.he_aac_v2_api import HeAacV2Api
from bitmovin_python.encoding.configurations.audio.vorbis.vorbis_api import VorbisApi
from bitmovin_python.encoding.configurations.audio.opus.opus_api import OpusApi
from bitmovin_python.encoding.configurations.audio.ac3.ac3_api import Ac3Api
from bitmovin_python.encoding.configurations.audio.eac3.eac3_api import Eac3Api
from bitmovin_python.encoding.configurations.audio.mp2.mp2_api import Mp2Api
from bitmovin_python.encoding.configurations.audio.mp3.mp3_api import Mp3Api


class AudioApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AudioApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.aac = AacApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.heAacV1 = HeAacV1Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.heAacV2 = HeAacV2Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.vorbis = VorbisApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.opus = OpusApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.ac3 = Ac3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.eac3 = Eac3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mp2 = Mp2Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mp3 = Mp3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
