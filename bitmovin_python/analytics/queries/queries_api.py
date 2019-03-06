# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except
from bitmovin_python.analytics.queries.count.count_api import CountApi
from bitmovin_python.analytics.queries.sum.sum_api import SumApi
from bitmovin_python.analytics.queries.avg.avg_api import AvgApi
from bitmovin_python.analytics.queries.min.min_api import MinApi
from bitmovin_python.analytics.queries.max.max_api import MaxApi
from bitmovin_python.analytics.queries.stddev.stddev_api import StddevApi
from bitmovin_python.analytics.queries.percentile.percentile_api import PercentileApi
from bitmovin_python.analytics.queries.variance.variance_api import VarianceApi
from bitmovin_python.analytics.queries.median.median_api import MedianApi


class QueriesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(QueriesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.count = CountApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.sum = SumApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.avg = AvgApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.min = MinApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.max = MaxApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.stddev = StddevApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.percentile = PercentileApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.variance = VarianceApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.median = MedianApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
