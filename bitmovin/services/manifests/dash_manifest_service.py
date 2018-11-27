from urllib.parse import urljoin
from bitmovin.errors import FunctionalityNotAvailableError, InvalidTypeError, BitmovinApiError, InvalidStatusError
from bitmovin.resources import DashManifest, Period, ResourceResponse, Status, Response, AudioAdaptationSet, \
    VideoAdaptationSet, SubtitleAdaptationSet, FMP4Representation, DRMFMP4Representation, WebMRepresentation, \
    ContentProtection, DashMP4Representation, CustomXMLElement
from bitmovin.services.manifests.generic_manifest_service import GenericManifestService
from .manifest_control_service import ManifestControlService


class DASH(GenericManifestService, ManifestControlService):
    manifest_type = 'dash'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, manifest_type=self.manifest_type, resource_class=DashManifest)

    def retrieve_custom_data(self, id_):
        raise FunctionalityNotAvailableError('Retrieve Custom Data is not available for DASH Manifests')

    def add_period(self, object_, manifest_id):
        if not isinstance(object_, Period):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(Period.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods'.format(manifest_id))
        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=Period)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def add_audio_adaptation_set(self, object_, manifest_id, period_id):
        if not isinstance(object_, AudioAdaptationSet):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(AudioAdaptationSet.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/adaptationsets/audio'.format(manifest_id, period_id))
        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=AudioAdaptationSet)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def add_video_adaptation_set(self, object_, manifest_id, period_id):
        if not isinstance(object_, VideoAdaptationSet):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(VideoAdaptationSet.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/adaptationsets/video'.format(manifest_id, period_id))
        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=VideoAdaptationSet)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def add_subtitle_adaptation_set(self, object_, manifest_id, period_id):
        if not isinstance(object_, SubtitleAdaptationSet):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(SubtitleAdaptationSet.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/adaptationsets/subtitle'.format(manifest_id, period_id))
        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=SubtitleAdaptationSet)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def add_fmp4_representation(self, object_, manifest_id, period_id, adaptationset_id):
        if not isinstance(object_, FMP4Representation):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(FMP4Representation.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/adaptationsets/{}/representations/fmp4'.format(
            manifest_id, period_id, adaptationset_id))

        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=FMP4Representation)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def add_drm_fmp4_representation(self, object_, manifest_id, period_id, adaptationset_id):
        if not isinstance(object_, DRMFMP4Representation):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(DRMFMP4Representation.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/adaptationsets/{}/representations/fmp4/drm'.format(
            manifest_id, period_id, adaptationset_id))

        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=DRMFMP4Representation)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def add_webm_representation(self, object_, manifest_id, period_id, adaptationset_id):
        if not isinstance(object_, WebMRepresentation):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(WebMRepresentation.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/adaptationsets/{}/representations/webm'.format(
            manifest_id, period_id, adaptationset_id))

        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=WebMRepresentation)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def add_content_protection_to_adaptionset(self, object_, manifest_id, period_id, adaptationset_id):
        if not isinstance(object_, ContentProtection):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(ContentProtection.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/adaptationsets/{}/contentprotection'.format(
            manifest_id, period_id, adaptationset_id))

        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=ContentProtection)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def add_content_protection_to_fmp4_represenation(self, object_, manifest_id, period_id, adaptationset_id,
                                                     representation_id):
        if not isinstance(object_, ContentProtection):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(ContentProtection.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/adaptationsets/{}/representations/fmp4/{}/contentprotection'.format(
            manifest_id, period_id, adaptationset_id, representation_id))

        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=ContentProtection)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def add_content_protection_to_drm_fmp4_represenation(self, object_, manifest_id, period_id, adaptationset_id,
                                                         representation_id):
        if not isinstance(object_, ContentProtection):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(ContentProtection.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/adaptationsets/{}/representations/fmp4/drm/{}/contentprotection'.format(
            manifest_id, period_id, adaptationset_id, representation_id))

        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=ContentProtection)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))
    
    def add_mp4_representation(self, object_, manifest_id, period_id, adaptationset_id):
        if not isinstance(object_, DashMP4Representation):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(DashMP4Representation.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/adaptationsets/{}/representations/mp4'.format(
            manifest_id, period_id, adaptationset_id))

        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=DashMP4Representation)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def add_custom_xml_element_to_period(self, object_, manifest_id, period_id):
        if not isinstance(object_, CustomXMLElement):
            raise InvalidTypeError('object_ has to be an instance of {}'.format(CustomXMLElement.__name__))

        url = self.relative_url
        if not url.endswith('/'):
            url += '/'

        url = urljoin(url, '{}/periods/{}/custom-xml-elements'.format(
            manifest_id, period_id))

        response = self.http_client.post(url, object_)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful: {}'.format(response.raw_response), response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=CustomXMLElement)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))
