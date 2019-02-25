# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.s3_role_based_input import S3RoleBasedInput
from bitmovin_python.encoding.inputs.s3RoleBased.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.inputs.s3RoleBased.s3_role_based_inputs_list_query_params import S3RoleBasedInputsListQueryParams


class S3RoleBasedApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(S3RoleBasedApi, self).__init__(
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

    def create(self, s3_role_based_input=None, **kwargs):
        """Create S3 Role-based Input"""

        return self.api_client.post(
            '/encoding/inputs/s3-role-based',
            s3_role_based_input,
            type=S3RoleBasedInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete S3 Role-based Input"""

        return self.api_client.delete(
            '/encoding/inputs/s3-role-based/{input_id}',
            path_params={'input_id': input_id},
            type=S3RoleBasedInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """S3 Role-based Input Details"""

        return self.api_client.get(
            '/encoding/inputs/s3-role-based/{input_id}',
            path_params={'input_id': input_id},
            type=S3RoleBasedInput,
            **kwargs
        )

    def list(self, query_params: S3RoleBasedInputsListQueryParams = None, **kwargs):
        """List S3 Role-based Inputs"""

        return self.api_client.get(
            '/encoding/inputs/s3-role-based',
            query_params=query_params,
            pagination_response=True,
            type=S3RoleBasedInput,
            **kwargs
        )
