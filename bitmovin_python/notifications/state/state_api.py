# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.notification_state_entry import NotificationStateEntry
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.notifications.state.notification_state_entrys_list_query_params import NotificationStateEntrysListQueryParams


class StateApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(StateApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def list(self, notification_id, resource_id, query_params: NotificationStateEntrysListQueryParams = None, **kwargs):
        """List Notification State History (Specific Resource)"""

        return self.api_client.get(
            '/notifications/{notification_id}/state/{resource_id}',
            path_params={'notification_id': notification_id, 'resource_id': resource_id},
            query_params=query_params,
            pagination_response=True,
            type=NotificationStateEntry,
            **kwargs
        )
