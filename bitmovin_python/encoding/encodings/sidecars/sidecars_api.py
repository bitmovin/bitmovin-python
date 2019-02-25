# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.sidecar_file import SidecarFile
from bitmovin_python.encoding.encodings.sidecars.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.sidecars.sidecar_files_list_query_params import SidecarFilesListQueryParams


class SidecarsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(SidecarsApi, self).__init__(
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

    def create(self, encoding_id, sidecar_file=None, **kwargs):
        """Add Sidecar"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/sidecars',
            sidecar_file,
            path_params={'encoding_id': encoding_id},
            type=SidecarFile,
            **kwargs
        )

    def delete(self, encoding_id, sidecar_id, **kwargs):
        """Delete Sidecar"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/sidecars/{sidecar_id}',
            path_params={'encoding_id': encoding_id, 'sidecar_id': sidecar_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, sidecar_id, **kwargs):
        """Sidecar Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/sidecars/{sidecar_id}',
            path_params={'encoding_id': encoding_id, 'sidecar_id': sidecar_id},
            type=SidecarFile,
            **kwargs
        )

    def list(self, encoding_id, query_params: SidecarFilesListQueryParams = None, **kwargs):
        """List Sidecars"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/sidecars',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=SidecarFile,
            **kwargs
        )
