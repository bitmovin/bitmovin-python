# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.aws_account_region_settings import AwsAccountRegionSettings
from bitmovin_python.models.aws_cloud_region import AwsCloudRegion
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.infrastructure.aws.regions.aws_account_region_settingss_list_query_params import AwsAccountRegionSettingssListQueryParams


class RegionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(RegionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, infrastructure_id, region, aws_account_region_settings=None, **kwargs):
        """Add AWS Region Setting"""

        return self.api_client.post(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions/{region}',
            aws_account_region_settings,
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AwsAccountRegionSettings,
            **kwargs
        )

    def delete(self, infrastructure_id, region, **kwargs):
        """Delete AWS Region Settings"""

        return self.api_client.delete(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AwsAccountRegionSettings,
            **kwargs
        )

    def get(self, infrastructure_id, region, **kwargs):
        """AWS Region Settings Details"""

        return self.api_client.get(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AwsAccountRegionSettings,
            **kwargs
        )

    def list(self, infrastructure_id, query_params: AwsAccountRegionSettingssListQueryParams = None, **kwargs):
        """List AWS Region Settings"""

        return self.api_client.get(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions',
            path_params={'infrastructure_id': infrastructure_id},
            query_params=query_params,
            pagination_response=True,
            type=AwsAccountRegionSettings,
            **kwargs
        )
