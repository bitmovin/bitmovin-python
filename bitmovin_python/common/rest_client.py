import json
import logging
import sys

import requests

from bitmovin_python.common.bitmovin_exception import RestException
from bitmovin_python.common.bitmovin_exception import MissingArgumentException


class RestClient(object):
    HTTP_HEADERS = {
        'Content-Type': 'application/json',
        'X-Api-Client': 'bitmovin-python',
        'X-Api-Client-Version': '3.1.1alpha0'
    }

    DELETE = 'DELETE'
    GET = 'GET'
    PATCH = 'PATCH'
    POST = 'POST'
    PUT = 'PUT'

    API_KEY_HTTP_HEADER_NAME = 'X-Api-Key'
    TENANT_ORG_ID_HTTP_HEADER_NAME = 'X-Tenant-Org-Id'

    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                *args, **kwargs):
        super().__init__()

        self.api_key = api_key
        self.tenant_org_id = tenant_org_id
        self.debug = debug
        self.logger = logger

        if base_url is None or base_url == '':
            self.base_url = 'https://api.bitmovin.com/v1'
        else:
            self.base_url = base_url

        if not self.api_key:
            raise MissingArgumentException("api_key has to be set")

        self.http_headers = self.HTTP_HEADERS.copy()
        self.http_headers.update({self.API_KEY_HTTP_HEADER_NAME: self.api_key})
        if self.tenant_org_id is not None and self.tenant_org_id != '':
            self.http_headers.update({self.TENANT_ORG_ID_HTTP_HEADER_NAME: self.tenant_org_id})

        if logger is None:
            self.logger = logging.getLogger(self.__class__.__module__ + "." + self.__class__.__name__)
            self._attach_console_logging_handler_if_not_existing()

    def request(self, method: str, relative_url: str, payload=None):
        url = self.urljoin(self.base_url, relative_url)
        self._log_request(method, url, payload)

        if payload is None:
            response = requests.request(method, url, headers=self.http_headers)
        else:
            response = requests.request(method, url, headers=self.http_headers, data=self._serialize(payload))

        RestClient._check_response_and_throw_exception_if_not_successful(response)
        parsed_response = self._parse_response(response)
        return parsed_response

    def delete(self, relative_url: str):
        return self.request(method=self.DELETE, relative_url=relative_url)

    def get(self, relative_url: str):
        return self.request(method=self.GET, relative_url=relative_url)

    def patch(self, relative_url: str, payload):
        return self.request(method=self.PATCH, relative_url=relative_url, payload=payload)

    def post(self, relative_url: str, payload=None):
        return self.request(method=self.POST, relative_url=relative_url, payload=payload)

    def put(self, relative_url: str, payload):
        return self.request(method=self.PUT, relative_url=relative_url, payload=payload)

    def _attach_console_logging_handler_if_not_existing(self):
        handlers = self.logger.handlers
        handler_already_exists = any(handler.name == 'bitmovin_console_handler' for handler in handlers)

        if handler_already_exists:
            return

        self.logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.name = 'bitmovin_console_handler'
        formatter = logging.Formatter('%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)

    def _parse_response(self, response):
        if not response.text:
            return dict()

        if not RestClient._check_response_header_json(response):
            self.logger.error('Response: {}'.format(response.text))
            raise RestException(response.status_code, 'Response was not in JSON format -> [{}]: {}'.format(
                response.status_code, response.text), response)
        return response.json()

    def _serialize(self, object_):
        if object_ is None:
            return None
        serialized = json.dumps(object_)
        self.logger.info('Serialized request object: {}'.format(serialized))
        return serialized

    def _log_request(self, method, url, payload=None):
        log_line = 'REQUEST: {} {}'.format(method, url)
        if payload:
            log_line += '  --> {}'.format(json.dumps(payload))
        self.logger.info(log_line)

    @staticmethod
    def _check_response_and_throw_exception_if_not_successful(response):
        if not RestClient._check_response_success(response):
            raise RestException(http_resp=response)

    @staticmethod
    def _check_response_success(response):
        status_code = response.status_code
        if 200 <= status_code <= 299:
            return True
        return False

    @staticmethod
    def _check_response_header_json(response):
        headers = response.headers
        content_type = headers.get('content-type')
        if content_type.startswith('application/json') or content_type.startswith('application/hal+json'):
            return True
        return False

    @staticmethod
    def urljoin(*args):
        return '/'.join(map(lambda x: str(x).strip('/'), args))
