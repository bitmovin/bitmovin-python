# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.email_notification import EmailNotification
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.notifications.emails.encoding.encodings.encodings_api import EncodingsApi
from bitmovin_python.notifications.emails.encoding.email_notifications_list_query_params import EmailNotificationsListQueryParams


class EncodingApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(EncodingApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.encodings = EncodingsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: EmailNotificationsListQueryParams = None, **kwargs):
        """List Email Notifications (All Encodings)"""

        return self.api_client.get(
            '/notifications/emails/encoding',
            query_params=query_params,
            pagination_response=True,
            type=EmailNotification,
            **kwargs
        )
