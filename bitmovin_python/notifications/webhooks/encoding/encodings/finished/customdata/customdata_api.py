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

    def getCustomDataByEncodingIdAndWebhookId(self, encoding_id, webhook_id, **kwargs):
        """Encoding Finished Webhook Custom Data for specific Encoding Resource"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/finished/{webhook_id}/customData',
            path_params={'encoding_id': encoding_id, 'webhook_id': webhook_id},
            type=CustomData,
            **kwargs
        )

    def getCustomDataByWebhookId(self, webhook_id, **kwargs):
        """Encoding Finished Webhook Custom Data"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/finished/{webhook_id}/customData',
            path_params={'webhook_id': webhook_id},
            type=CustomData,
            **kwargs
        )
