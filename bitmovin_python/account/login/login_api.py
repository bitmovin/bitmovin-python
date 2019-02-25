# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.account_information import AccountInformation
from bitmovin_python.models.login import Login
from bitmovin_python.models.response_envelope import ResponseEnvelope


class LoginApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(LoginApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, login=None, **kwargs):
        """Login"""

        return self.api_client.post(
            '/account/login',
            login,
            type=AccountInformation,
            **kwargs
        )
