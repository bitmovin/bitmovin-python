# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.notification import Notification
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.notifications.emails.encoding.encoding_api import EncodingApi
from bitmovin_python.notifications.emails.notifications_list_query_params import NotificationsListQueryParams


class EmailsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(EmailsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.encoding = EncodingApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def list(self, query_params: NotificationsListQueryParams = None, **kwargs):
        """List Email Notifications"""

        return self.api_client.get(
            '/notifications/emails',
            query_params=query_params,
            pagination_response=True,
            type=Notification,
            **kwargs
        )
