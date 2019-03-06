import re
from urllib.parse import urlencode

from bitmovin_python.common.bitmovin_exception import BitmovinException
from bitmovin_python.common.bitmovin_exception import MissingArgumentException
from bitmovin_python.common.bitmovin_exception import RestException
from bitmovin_python.common.rest_client import RestClient
from bitmovin_python.common.bitmovin_json_decoder import BitmovinJsonDecoder
from bitmovin_python.common.poscheck import poscheck, poscheck_except
from bitmovin_python.models import BitmovinResponse, ResponseErrorData


class ApiClient(object):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        self.rest_client = RestClient(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    @staticmethod
    def remove_none_values_from_dict(dict_to_remove_from: dict):
        return dict((k, v) for k, v in dict_to_remove_from.items() if v is not None)

    def prepare_url(self, relative_url, **kwargs):
        if 'query_params' in kwargs and kwargs['query_params'] is not None:
            query_params = self.remove_none_values_from_dict(kwargs['query_params'].__dict__)
            relative_url += '?' + urlencode(query_params)

        if not self.check_url_contains_placeholders(relative_url):
            return relative_url

        if 'path_params' not in kwargs:
            raise MissingArgumentException()

        path_params = kwargs['path_params']
        if not isinstance(path_params, dict):
            raise MissingArgumentException()

        for k in path_params:
            relative_url = relative_url.replace(
                '{%s}' % k,
                path_params[k]
            )

        if self.check_url_contains_placeholders(url=relative_url):
            raise Exception('url {} does contain placeholders after replacing'.format(relative_url))

        return relative_url

    @staticmethod
    def check_url_contains_placeholders(url):
        found = re.search(r'({.*})', url)
        return found is not None

    def request(self, method: str, relative_url: str, payload=None, raw_response: bool = False, **kwargs):
        url = self.prepare_url(relative_url, **kwargs)

        try:
            response = self.rest_client.request(method=method, payload=payload, relative_url=url)
            return response if raw_response else self.map_response_to_model(response, **kwargs)
        except RestException as e:
            self.handle_error(e)

    def delete(self, relative_url, **kwargs):
        if 'type' not in kwargs or kwargs['type'] is None:
            kwargs['type'] = BitmovinResponse

        return self.request('DELETE', relative_url=relative_url, **kwargs)

    def get(self, relative_url, **kwargs):
        raw_response = False
        if 'type' not in kwargs or kwargs['type'] is None:
            raw_response = True

        return self.request('GET', relative_url=relative_url, raw_response=raw_response,  **kwargs)

    def post(self, relative_url, payload, **kwargs):
        if 'type' not in kwargs or kwargs['type'] is None:
            raise MissingArgumentException('type must be given')

        if payload is not None:
                if type(payload) != list:
                    return self.request('POST', relative_url=relative_url, payload=payload.to_dict(), **kwargs)
                else:
                    return self.request('POST', relative_url=relative_url, payload=payload, **kwargs)
        elif payload is None:
            return self.request('POST', relative_url=relative_url, **kwargs)

    def put(self, relative_url, payload, **kwargs):
        if 'type' not in kwargs or kwargs['type'] is None:
            raise MissingArgumentException('type must be given')

        return self.request('PUT', relative_url=relative_url, payload=payload.to_dict(), **kwargs)

    @staticmethod
    def map_response_to_model(response, **kwargs):
        if 'status' in response and response['status'] == 'SUCCESS':
            if 'data' in response and 'result' in response['data']:
                response_success = response['data']['result']
                if 'pagination_response' in kwargs and kwargs['pagination_response']:
                    return BitmovinJsonDecoder.map_dict_to_pagination_response(response_success, kwargs['type'])
                else:
                    return BitmovinJsonDecoder.map_dict_to_model(response_success, kwargs['type'])
            else:
                return BitmovinJsonDecoder.map_dict_to_model(response['data'], kwargs['type'])

    @staticmethod
    def handle_error(e: RestException):
        error_body = e.body
        if error_body is None or not isinstance(error_body, dict):
            raise e

        if 'status' in error_body and error_body['status'] == 'ERROR':
            if 'data' in error_body:
                error_data = BitmovinJsonDecoder.map_dict_to_model(error_body['data'], ResponseErrorData)
                raise BitmovinException(error_data=error_data, status=e.status, reason=e.reason)
            else:
                raise e
