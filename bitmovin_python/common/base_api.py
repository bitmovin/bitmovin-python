from bitmovin_python.common.api_client import ApiClient
from bitmovin_python.common.poscheck import poscheck_except


class BaseApi(object):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        self.api_client = ApiClient(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
