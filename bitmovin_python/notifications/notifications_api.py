# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.notification import Notification
from bitmovin_python.models.notification_state_entry import NotificationStateEntry
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.notifications.webhooks.webhooks_api import WebhooksApi
from bitmovin_python.notifications.state.state_api import StateApi
from bitmovin_python.notifications.emails.emails_api import EmailsApi
from bitmovin_python.notifications.notifications_list_query_params import NotificationsListQueryParams
from bitmovin_python.notifications.notification_state_entrys_list_by_notification_id_query_params import NotificationStateEntrysListByNotificationIdQueryParams


class NotificationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(NotificationsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.webhooks = WebhooksApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.state = StateApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.emails = EmailsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def delete(self, notification_id, **kwargs):
        """Delete Notification"""

        return self.api_client.delete(
            '/notifications/{notification_id}',
            path_params={'notification_id': notification_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, notification_id, **kwargs):
        """Get Notification"""

        return self.api_client.get(
            '/notifications/{notification_id}',
            path_params={'notification_id': notification_id},
            type=Notification,
            **kwargs
        )

    def list(self, query_params: NotificationsListQueryParams = None, **kwargs):
        """List Notifications"""

        return self.api_client.get(
            '/notifications',
            query_params=query_params,
            pagination_response=True,
            type=Notification,
            **kwargs
        )

    def list(self, notification_id, query_params: NotificationStateEntrysListByNotificationIdQueryParams = None, **kwargs):
        """List Notification State History (All Resources)"""

        return self.api_client.get(
            '/notifications/{notification_id}/state',
            path_params={'notification_id': notification_id},
            query_params=query_params,
            pagination_response=True,
            type=NotificationStateEntry,
            **kwargs
        )

    def mute(self, notification_id, **kwargs):
        """Mute Notification"""

        return self.api_client.post(
            '/notifications/{notification_id}/mute',
            path_params={'notification_id': notification_id},
            type=BitmovinResponse,
            **kwargs
        )

    def unmute(self, notification_id, **kwargs):
        """Unmute Notification"""

        return self.api_client.post(
            '/notifications/{notification_id}/unmute',
            path_params={'notification_id': notification_id},
            type=BitmovinResponse,
            **kwargs
        )
