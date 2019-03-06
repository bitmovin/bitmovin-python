# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.encoding_statistics_vod import EncodingStatisticsVod
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.statistics.encodings.vod.encoding_statistics_vods_list_by_date_range_query_params import EncodingStatisticsVodsListByDateRangeQueryParams
from bitmovin_python.encoding.statistics.encodings.vod.encoding_statistics_vods_list_query_params import EncodingStatisticsVodsListQueryParams


class VodApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(VodApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: EncodingStatisticsVodsListQueryParams = None, **kwargs):
        """List VOD Encoding Statistics"""

        return self.api_client.get(
            '/encoding/statistics/encodings/vod',
            query_params=query_params,
            pagination_response=True,
            type=EncodingStatisticsVod,
            **kwargs
        )

    def list(self, _from, to, query_params: EncodingStatisticsVodsListByDateRangeQueryParams = None, **kwargs):
        """List VOD Encoding Statistics Within Specific Dates"""

        return self.api_client.get(
            '/encoding/statistics/encodings/vod/{from}/{to}',
            path_params={'_from': _from, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=EncodingStatisticsVod,
            **kwargs
        )
