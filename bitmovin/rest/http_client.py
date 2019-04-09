import json
import requests
from urllib.parse import urljoin

from bitmovin.package_information import NAME, VERSION
from bitmovin.bitmovin_object import BitmovinObject
from bitmovin.errors import MissingArgumentError, BitmovinApiError
from bitmovin.resources import Response
from bitmovin.utils import BitmovinJSONEncoder
from .utils import check_response_success, check_response_header_json
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


class BitmovinHttpClient(BitmovinObject):

    DEFAULT_PROTOCOL = "https://"
    API_BASE_URL = DEFAULT_PROTOCOL + "api.bitmovin.com/v1/"

    HTTP_HEADERS = {
        'Content-Type': 'application/json',
        'X-Api-Client': NAME,
        'X-Api-Client-Version': VERSION
    }

    API_KEY_HTTP_HEADER_NAME = 'X-Api-Key'
    TENANT_ORG_ID_HTTP_HEADER_NAME = 'X-Tenant-Org-Id'

    def __init__(self, api_key, base_url=None, tenant_org_id=None):
        super().__init__()

        if base_url:
            self.base_url = base_url
        else:
            self.base_url = self.API_BASE_URL

        if not api_key:
            raise MissingArgumentError("api_key has to be set when instantiating BitmovinRestClient.")

        self.http_headers = self.HTTP_HEADERS.copy()
        self.http_headers.update({self.API_KEY_HTTP_HEADER_NAME: api_key})
        if tenant_org_id is not None:
            self.http_headers.update({self.TENANT_ORG_ID_HTTP_HEADER_NAME: tenant_org_id})

    def post_empty_body(self, relative_url):
        self._log_request('POST', relative_url)
        url = urljoin(self.base_url, relative_url)
        response = requests.post(url, headers=self.http_headers)
        parsed_response = self._parse_response(response)
        return parsed_response

    def post(self, relative_url, payload):
        self._log_request('POST', relative_url, payload)
        url = urljoin(self.base_url, relative_url)
        response = requests.post(url, data=self._serialize(payload), headers=self.http_headers)
        parsed_response = self._parse_response(response)
        return parsed_response

    def get(self, relative_url):
        self._log_request('GET', relative_url)
        url = urljoin(self.base_url, relative_url)
        session = requests.Session()
        retries = Retry(total=10, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
        session.mount('https://', HTTPAdapter(max_retries=retries))
        response = session.get(url, headers=self.http_headers)
        parsed_response = self._parse_response(response)
        return parsed_response

    def delete(self, relative_url):
        self._log_request('DELETE', relative_url)
        url = urljoin(self.base_url, relative_url)
        response = requests.delete(url, headers=self.http_headers)
        parsed_response = self._parse_response(response)
        return parsed_response

    def put(self, relative_url, payload):
        self._log_request('PUT', relative_url, payload)
        url = urljoin(self.base_url, relative_url)
        response = requests.put(url, data=self._serialize(payload), headers=self.http_headers)
        parsed_response = self._parse_response(response)
        return parsed_response

    def patch(self, relative_url, payload):
        self._log_request('PATCH', relative_url, payload)
        url = urljoin(self.base_url, relative_url)
        response = requests.patch(url, data=self._serialize(payload), headers=self.http_headers)
        parsed_response = self._parse_response(response)
        return parsed_response

    def _parse_response(self, response):
        if not check_response_header_json(response):
            self.logger.error('Response: {}'.format(response.text))
            raise BitmovinApiError('Response was not in JSON format -> [{}]: {}'.format(
                response.status_code, response.text), response)

        success = check_response_success(response)
        json_response = response.json()

        if success:
            parsed_response = self._parse_success_response(json_response)
        else:
            self.logger.error('Response had status {}: {}'.format(response.status_code, response.text))
            parsed_response = self._parse_error_response(json_response)

        return parsed_response

    def _parse_success_response(self, response):
        parsed_response = Response.parse_from_json_object(response)
        return parsed_response

    def _parse_error_response(self, response: dict):
        self.logger.info('Parsing error response ...')

        if response.get('status') is None:
            raise BitmovinApiError('Retrieved invalid response from API: {}'.format(json.dumps(response)))

        parsed_response = Response.parse_from_json_object(response)

        return parsed_response

    def _serialize(self, object_):
        serialized = json.dumps(object_, cls=BitmovinJSONEncoder)
        self.logger.info('Serialized object: {}'.format(serialized))
        return serialized

    def _log_request(self, method, url, payload=None):
        log_line = 'REQUEST: {} {}'.format(method, url)
        if payload:
            log_line += '  --> {}'.format(json.dumps(payload, cls=BitmovinJSONEncoder))
        self.logger.info(log_line)
