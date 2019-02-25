# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.dvb_subtitle_sidecar_details import DvbSubtitleSidecarDetails
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.encoding.encodings.subtitles.dvbsub.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.subtitles.dvbsub.dvb_subtitle_sidecar_detailss_list_query_params import DvbSubtitleSidecarDetailssListQueryParams


class DvbsubApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(DvbsubApi, self).__init__(
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

    def create(self, encoding_id, dvb_subtitle_sidecar_details=None, **kwargs):
        """Extract DVB-SUB Subtitle"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/subtitles/dvbsub',
            dvb_subtitle_sidecar_details,
            path_params={'encoding_id': encoding_id},
            type=DvbSubtitleSidecarDetails,
            **kwargs
        )

    def delete(self, encoding_id, subtitle_id, **kwargs):
        """Delete DVB-SUB Subtitle"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/subtitles/dvbsub/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'subtitle_id': subtitle_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, subtitle_id, **kwargs):
        """Subtitle DVB-SUB Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/subtitles/dvbsub/{subtitle_id}',
            path_params={'encoding_id': encoding_id, 'subtitle_id': subtitle_id},
            type=DvbSubtitleSidecarDetails,
            **kwargs
        )

    def list(self, encoding_id, query_params: DvbSubtitleSidecarDetailssListQueryParams = None, **kwargs):
        """List DVB-SUB Subtitle"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/subtitles/dvbsub',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=DvbSubtitleSidecarDetails,
            **kwargs
        )
