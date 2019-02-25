# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.email_notification_with_stream_conditions import EmailNotificationWithStreamConditions
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.notifications.emails.encoding.encodings.liveInputStreamChanged.live_input_stream_changed_api import LiveInputStreamChangedApi
from bitmovin_python.notifications.emails.encoding.encodings.error.error_api import ErrorApi
from bitmovin_python.notifications.emails.encoding.encodings.email_notification_with_stream_conditionss_list_query_params import EmailNotificationWithStreamConditionssListQueryParams


class EncodingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(EncodingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.liveInputStreamChanged = LiveInputStreamChangedApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.error = ErrorApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def list(self, encoding_id, query_params: EmailNotificationWithStreamConditionssListQueryParams = None, **kwargs):
        """List Email Notifications (Specific Encoding)"""

        return self.api_client.get(
            '/notifications/emails/encoding/encodings/{encoding_id}',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=EmailNotificationWithStreamConditions,
            **kwargs
        )
