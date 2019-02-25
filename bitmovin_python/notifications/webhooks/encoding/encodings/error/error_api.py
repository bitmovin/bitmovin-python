# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.webhook import Webhook
from bitmovin_python.notifications.webhooks.encoding.encodings.error.customdata.customdata_api import CustomdataApi
from bitmovin_python.notifications.webhooks.encoding.encodings.error.webhooks_list_query_params import WebhooksListQueryParams
from bitmovin_python.notifications.webhooks.encoding.encodings.error.webhooks_list_by_encoding_id_query_params import WebhooksListByEncodingIdQueryParams


class ErrorApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(ErrorApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, webhook=None, **kwargs):
        """Add Encoding Error Webhook"""

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/error',
            webhook,
            type=Webhook,
            **kwargs
        )

    def createbyEncodingId(self, encoding_id, webhook=None, **kwargs):
        """Add Encoding Error Webhook for specific Encoding Resource"""

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error',
            webhook,
            path_params={'encoding_id': encoding_id},
            type=Webhook,
            **kwargs
        )

    def deleteByEncodingIdAndWebhookId(self, encoding_id, webhook_id, **kwargs):
        """Delete Encoding Error Webhook for specific Encoding Resource"""

        return self.api_client.delete(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error/{webhook_id}',
            path_params={'encoding_id': encoding_id, 'webhook_id': webhook_id},
            type=BitmovinResponse,
            **kwargs
        )

    def deleteByWebhookId(self, webhook_id, **kwargs):
        """Delete Encoding Error Webhook"""

        return self.api_client.delete(
            '/notifications/webhooks/encoding/encodings/error/{webhook_id}',
            path_params={'webhook_id': webhook_id},
            type=BitmovinResponse,
            **kwargs
        )

    def getByEncodingIdAndWebhookId(self, encoding_id, webhook_id, **kwargs):
        """Encoding Error Webhook Details for specific Encoding Resource"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error/{webhook_id}',
            path_params={'encoding_id': encoding_id, 'webhook_id': webhook_id},
            type=Webhook,
            **kwargs
        )

    def getByWebhookId(self, webhook_id, **kwargs):
        """Encoding Error Webhook Details"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/error/{webhook_id}',
            path_params={'webhook_id': webhook_id},
            type=Webhook,
            **kwargs
        )

    def list(self, query_params: WebhooksListQueryParams = None, **kwargs):
        """List Encoding Error Webhooks"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/error',
            query_params=query_params,
            pagination_response=True,
            type=Webhook,
            **kwargs
        )

    def list(self, encoding_id, query_params: WebhooksListByEncodingIdQueryParams = None, **kwargs):
        """List Encoding Error Webhooks for specific Encoding Resource"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Webhook,
            **kwargs
        )
