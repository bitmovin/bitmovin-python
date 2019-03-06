# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.captions_cea import CaptionsCea
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.captions.cea.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.captions.cea.captions_ceas_list_query_params import CaptionsCeasListQueryParams


class CeaApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CeaApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, captions_cea=None, **kwargs):
        """Extract CEA 608/708 Captions"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/captions/cea',
            captions_cea,
            path_params={'encoding_id': encoding_id},
            type=CaptionsCea,
            **kwargs
        )

    def delete(self, encoding_id, captions_id, **kwargs):
        """Delete CEA 608/708 Captions"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/captions/cea/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=CaptionsCea,
            **kwargs
        )

    def get(self, encoding_id, captions_id, **kwargs):
        """CEA 608/708 Captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/cea/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=CaptionsCea,
            **kwargs
        )

    def list(self, encoding_id, query_params: CaptionsCeasListQueryParams = None, **kwargs):
        """List CEA 608/708 Captions"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/cea',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=CaptionsCea,
            **kwargs
        )
