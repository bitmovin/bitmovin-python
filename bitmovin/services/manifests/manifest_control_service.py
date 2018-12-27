import time
import json
from bitmovin.bitmovin_object import BitmovinObject
from bitmovin.errors import BitmovinApiError, InvalidStatusError
from bitmovin.rest import BitmovinHttpClient
from bitmovin.resources import ResourceResponse, Status, ManifestStatus
from bitmovin.services.parsing_utils import ParsingUtils
from bitmovin.utils import BitmovinJSONEncoder, TimeoutUtils


class ManifestControlService(BitmovinObject):

    def __init__(self, http_client, relative_url):
        super().__init__()
        self.http_client = http_client  # type: BitmovinHttpClient
        self.parsing_utils = ParsingUtils()
        self.relative_url = relative_url

    def start(self, manifest_id):
        self.parsing_utils.check_arg_valid_uuid(manifest_id)
        url = self.relative_url + '/{}/start'.format(manifest_id)
        response = self.http_client.post_empty_body(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)
        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_minimal_model_from_response(response=response)
            return ResourceResponse(response=response, resource=created_resource)
        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def stop(self, manifest_id):
        self.parsing_utils.check_arg_valid_uuid(manifest_id)
        url = self.relative_url + '/{}/stop'.format(manifest_id)
        response = self.http_client.post_empty_body(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)
        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_minimal_model_from_response(response=response)
            return ResourceResponse(response=response, resource=created_resource)
        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def status(self, manifest_id):
        self.parsing_utils.check_arg_valid_uuid(manifest_id)
        url = self.relative_url + '/{}/status'.format(manifest_id)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)
        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(response=response,
                                                                                        class_=ManifestStatus)
            return ResourceResponse(response=response, resource=created_resource)
        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def wait_until_finished(self, manifest_id, check_interval=5, timeout=-1):
        status_response = None
        manifest_status = ManifestStatus()

        start_time = time.time()

        while manifest_status.status != 'FINISHED' and manifest_status.status != 'ERROR':
            TimeoutUtils.raise_error_if_timeout_reached(start_time_in_seconds=start_time, timeout_in_seconds=timeout)
            status_response = self.status(manifest_id=manifest_id)
            manifest_status = status_response.resource  # type: ManifestStatus
            self.logger.info("Manifest status: {}".format(manifest_status.status))
            self.logger.info("Will check again in {} seconds...".format(check_interval))
            time.sleep(check_interval)

        self.logger.info("Manifest Status: {}".format(json.dumps(obj=manifest_status, cls=BitmovinJSONEncoder)))

        if manifest_status.status == 'FINISHED':
            return True

        raise BitmovinApiError("Manifest with ID '{}' was not successfull! Status: {}".format(
            manifest_id, manifest_status.status), status_response)
