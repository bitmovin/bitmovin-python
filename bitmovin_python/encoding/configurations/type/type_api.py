# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.codec_config_type_response import CodecConfigTypeResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope


class TypeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(TypeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """Get Codec Configuration Type"""

        return self.api_client.get(
            '/encoding/configurations/{configuration_id}/type',
            path_params={'configuration_id': configuration_id},
            type=CodecConfigTypeResponse,
            **kwargs
        )
