from bitmovin.bitmovin_object import BitmovinObject
from bitmovin.resources.models.analytics import AnalyticsLicense
from bitmovin.errors import FunctionalityNotAvailableError
from bitmovin.resources import ResourceResponse, Status, Response
from ..rest_service import RestService

class AnalyticsLicenseService(RestService):
    BASE_ENDPOINT_URL = 'analytics/licenses'
    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AnalyticsLicense)

    def delete(self, id_):
        raise FunctionalityNotAvailableError()

    def add_domain(self, license, url):
        url = '{}/{}/domains'.format(self.relative_url, license.id)
        payload = dict(url=url)
        response = self.http_client.post(url, payload)

    def list(self, offset=None, limit=None):
        if not offset:
            offset = self.DEFAULT_LIST_OFFSET_PARAM
        if not limit:
            limit = self.DEFAULT_LIST_LIMIT_PARAM
        url = '{}?offset={}&limit={}'.format(self.relative_url, offset, limit)
        response = self.http_client.get(url)

        if response.status == Status.ERROR.value:
            raise BitmovinApiError('Response was not successful', response)

        if response.status == Status.SUCCESS.value:
            licenses = []
            list_ = response.data.result.get('items')
            for license in list_:
                full_license = self.retrieve(license['id'])
                licenses.append(full_license.resource)

            return ResourceResponse(response=response, resource=licenses)

        raise InvalidStatusError('Unknown status {} received'.format(response.status))
