# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.custom_data import CustomData
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError


class CustomdataApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CustomdataApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def getCustomData(self, input_id, **kwargs):
        """Zixi input Custom Data"""

        return self.api_client.get(
            '/encoding/inputs/zixi/{input_id}/customData',
            path_params={'input_id': input_id},
            type=CustomData,
            **kwargs
        )
