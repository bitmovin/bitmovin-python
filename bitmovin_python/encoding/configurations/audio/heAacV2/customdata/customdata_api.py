# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.custom_data import CustomData
from bitmovin_python.models.response_envelope import ResponseEnvelope


class CustomdataApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(CustomdataApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def getCustomData(self, configuration_id, **kwargs):
        """HE-AAC v2 Codec Configuration Custom Data"""

        return self.api_client.get(
            '/encoding/configurations/audio/he-aac-v2/{configuration_id}/customData',
            path_params={'configuration_id': configuration_id},
            type=CustomData,
            **kwargs
        )
