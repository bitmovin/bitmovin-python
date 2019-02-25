# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.player_version import PlayerVersion
from bitmovin_python.models.response_envelope import ResponseEnvelope


class LatestApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(LatestApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def get(self, channel_name, **kwargs):
        """Get Latest Player Version for Channel"""

        return self.api_client.get(
            '/player/channels/{channel_name}/versions/latest',
            path_params={'channel_name': channel_name},
            type=PlayerVersion,
            **kwargs
        )
