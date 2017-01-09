import time
import json
from bitmovin.bitmovin_object import BitmovinObject
from bitmovin.errors import BitmovinApiError, InvalidStatusError
from bitmovin.rest import BitmovinHttpClient
from bitmovin.resources import ResourceResponse, Status, EncodingStatus, LiveStreamConfiguration
from bitmovin.services.parsing_utils import ParsingUtils
from bitmovin.utils import BitmovinJSONEncoder


class EncodingControlService(BitmovinObject):

    def __init__(self, http_client, relative_url):
        super().__init__()
        self.http_client = http_client  # type: BitmovinHttpClient
        self.parsing_utils = ParsingUtils()
        self.relative_url = relative_url

    def start(self, encoding_id):
        self.parsing_utils.check_arg_valid_uuid(encoding_id)
        url = self.relative_url + '/{}/start'.format(encoding_id)
        response = self.http_client.post_empty_body(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)
        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_minimal_model_from_response(response=response)
            return ResourceResponse(response=response, resource=created_resource)
        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def stop(self, encoding_id):
        self.parsing_utils.check_arg_valid_uuid(encoding_id)
        url = self.relative_url + '/{}/stop'.format(encoding_id)
        response = self.http_client.post_empty_body(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)
        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_minimal_model_from_response(response=response)
            return ResourceResponse(response=response, resource=created_resource)
        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def start_live(self, encoding_id, live_stream_configuration: LiveStreamConfiguration):
        self.parsing_utils.check_arg_valid_uuid(encoding_id)
        self.parsing_utils.check_not_none(live_stream_configuration)
        self.parsing_utils.check_not_blank(live_stream_configuration.streamKey)

        url = self.relative_url + '/{}/live/start'.format(encoding_id)

        response = self.http_client.post(url, live_stream_configuration)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)
        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_minimal_model_from_response(response=response)
            return ResourceResponse(response=response, resource=created_resource)
        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def stop_live(self, encoding_id):
        self.parsing_utils.check_arg_valid_uuid(encoding_id)
        url = self.relative_url + '/{}/live/stop'.format(encoding_id)
        response = self.http_client.post_empty_body(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)
        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_minimal_model_from_response(response=response)
            return ResourceResponse(response=response, resource=created_resource)
        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def status(self, encoding_id):
        self.parsing_utils.check_arg_valid_uuid(encoding_id)
        url = self.relative_url + '/{}/status'.format(encoding_id)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)
        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_resource_from_response(response=response,
                                                                                        class_=EncodingStatus)
            return ResourceResponse(response=response, resource=created_resource)
        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def wait_until_finished(self, encoding_id, check_interval=5):
        status_response = None
        encoding_status = EncodingStatus(None)

        while encoding_status.status != 'FINISHED' and encoding_status.status != 'ERROR':
            status_response = self.status(encoding_id=encoding_id)
            encoding_status = status_response.resource  # type: EncodingStatus
            self.logger.info("Encoding status: {}".format(encoding_status.status))
            self.logger.info("Will check again in {} seconds...".format(check_interval))
            time.sleep(check_interval)

        self.logger.info("Encoding Status: {}".format(json.dumps(obj=encoding_status, cls=BitmovinJSONEncoder)))

        if encoding_status.status == 'FINISHED':
            return True

        raise BitmovinApiError("Encoding with ID '{}' was not successfull! Status: {}".format(
            encoding_id, encoding_status.status), status_response)


    def wait_until_running(self, encoding_id, check_interval=5):
        status_response = None
        encoding_status = EncodingStatus(None)

        while encoding_status.status != 'RUNNING' and encoding_status.status != 'ERROR':
            status_response = self.status(encoding_id=encoding_id)
            encoding_status = status_response.resource  # type: EncodingStatus
            self.logger.info("Encoding status: {}".format(encoding_status.status))
            self.logger.info("Will check again in {} seconds...".format(check_interval))
            time.sleep(check_interval)

        self.logger.info("Encoding Status: {}".format(json.dumps(obj=encoding_status, cls=BitmovinJSONEncoder)))

        if encoding_status.status == 'RUNNING':
            return True

        raise BitmovinApiError("Encoding with ID '{}' was not successfull! Status: {}".format(
            encoding_id, encoding_status.status), status_response)
