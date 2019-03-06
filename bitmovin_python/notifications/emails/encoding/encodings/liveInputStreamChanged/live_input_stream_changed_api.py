# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.email_notification_with_stream_conditions import EmailNotificationWithStreamConditions
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError


class LiveInputStreamChangedApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(LiveInputStreamChangedApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, email_notification_with_stream_conditions=None, **kwargs):
        """Add Live Input Stream Changed Email Notification (All Encodings)"""

        return self.api_client.post(
            '/notifications/emails/encoding/encodings/live-input-stream-changed',
            email_notification_with_stream_conditions,
            type=EmailNotificationWithStreamConditions,
            **kwargs
        )

    def createByEncodingId(self, encoding_id, email_notification_with_stream_conditions=None, **kwargs):
        """Add Live Input Stream Changed Email Notification (Specific Encoding)"""

        return self.api_client.post(
            '/notifications/emails/encoding/encodings/{encoding_id}/live-input-stream-changed',
            email_notification_with_stream_conditions,
            path_params={'encoding_id': encoding_id},
            type=EmailNotificationWithStreamConditions,
            **kwargs
        )

    def put_notifications_emails_encoding_encodings_live_input_stream_changed_by_input_id(self, notification_id, email_notification_with_stream_conditions=None, **kwargs):
        """Replace Live Input Stream Changed Email Notification"""

        return self.api_client.put(
            '/notifications/emails/encoding/encodings/live-input-stream-changed/{notification_id}',
            email_notification_with_stream_conditions,
            path_params={'notification_id': notification_id},
            type=EmailNotificationWithStreamConditions,
            **kwargs
        )
