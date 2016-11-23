import json
import time
from bitmovin.bitmovin_object import BitmovinObject
from bitmovin.errors import BitmovinApiError, InvalidTypeError, InvalidStatusError
from bitmovin.rest import BitmovinHttpClient
from bitmovin.resources import ResourceResponse, Status, Response
from bitmovin.resources.models import CustomData
from bitmovin.resources.models.inputs.analysis import Analysis, AnalysisDetails, AnalysisStreamDetails, AnalysisStatus
from bitmovin.services.parsing_utils import ParsingUtils
from bitmovin.utils import BitmovinJSONEncoder


class AnalyzeService(BitmovinObject):

    def __init__(self, http_client, relative_url):
        super().__init__()
        self.http_client = http_client  # type: BitmovinHttpClient
        self.parsing_utils = ParsingUtils()
        self.relative_url = relative_url

    def analyze(self, input_id, analysis_object):
        if not isinstance(analysis_object, Analysis):
            raise InvalidTypeError('analysis_object has to be an instance of Analysis')

        response = self.http_client.post(
            self.relative_url + '/{}/analysis'.format(input_id), analysis_object)  # type: Response

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            created_resource = self.parsing_utils.parse_bitmovin_minimal_model_from_response(response=response)
            return ResourceResponse(response=response, resource=created_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def list_analyses(self, input_id, offset=0, limit=100):
        url = '{}/{}/analysis?offset={}&limit={}'.format(self.relative_url, input_id, offset, limit)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            details_list = self.parsing_utils.parse_bitmovin_resource_list_from_response(response=response,
                                                                                         class_=AnalysisDetails)
            return ResourceResponse(response=response, resource=details_list)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def retrieve_analysis_details(self, input_id, analysis_id):
        self.parsing_utils.check_arg_valid_uuid(argument=input_id)
        self.parsing_utils.check_arg_valid_uuid(argument=analysis_id)
        url = '{}/{}/analysis/{}'.format(self.relative_url, input_id, analysis_id)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=AnalysisDetails)
            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def retrieve_analysis_stream_details(self, input_id, analysis_id, stream_id):
        self.parsing_utils.check_arg_valid_uuid(argument=input_id)
        self.parsing_utils.check_arg_valid_uuid(argument=analysis_id)
        self.parsing_utils.check_arg_valid_uuid(argument=stream_id)
        url = '{}/{}/analysis/{}/{}'.format(self.relative_url, input_id, analysis_id, stream_id)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=AnalysisStreamDetails)
            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def retrieve_analysis_custom_data(self, input_id, analysis_id):
        self.parsing_utils.check_arg_valid_uuid(argument=input_id)
        self.parsing_utils.check_arg_valid_uuid(argument=analysis_id)
        url = '{}/{}/analysis/{}/customData'.format(self.relative_url, input_id, analysis_id)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=CustomData)
            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def retrieve_analysis_status(self, input_id, analysis_id):
        self.parsing_utils.check_arg_valid_uuid(argument=input_id)
        self.parsing_utils.check_arg_valid_uuid(argument=analysis_id)
        url = '{}/{}/analysis/{}/status'.format(self.relative_url, input_id, analysis_id)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            retrieved_resource = self.parsing_utils.parse_bitmovin_resource_from_response(
                response=response, class_=AnalysisStatus)
            return ResourceResponse(response=response, resource=retrieved_resource)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))

    def wait_until_analysis_finished(self, input_id, analysis_id, check_interval=5):
        status_response = None
        analysis_status = AnalysisStatus(None)

        while analysis_status.status != 'FINISHED' and analysis_status.status != 'ERROR':
            status_response = self.retrieve_analysis_status(input_id=input_id, analysis_id=analysis_id)
            analysis_status = status_response.resource  # type: AnalysisStatus
            self.logger.info("Analysis status: {}".format(analysis_status.status))
            self.logger.info("Will check again in {} seconds...".format(check_interval))
            time.sleep(check_interval)

        self.logger.info("Analysis Status: {}".format(json.dumps(obj=analysis_status, cls=BitmovinJSONEncoder)))

        if analysis_status.status == 'FINISHED':
            return True

        raise BitmovinApiError("Analysis with ID '{}' (Input {}) was not successfull! Status: {}".format(
            analysis_id, input_id, analysis_status.status), status_response)
