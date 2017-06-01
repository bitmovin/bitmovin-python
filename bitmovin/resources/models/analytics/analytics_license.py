from bitmovin.resources.models import AbstractModel
from bitmovin.errors import InvalidTypeError
from .analytics_domain import AnalyticsDomain


class AnalyticsLicense(AbstractModel):
    def __init__(self, name=None, license_key=None, datapoints=None, max_datapoints=None, domains=None,
                 id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self._domains = None

        self.name = name
        self.licenseKey = license_key
        self.datapoints = datapoints
        self.maxDatapoints = max_datapoints
        self.domains = domains

    @property
    def domains(self):
        return self._domains

    @domains.setter
    def domains(self, new_value):
        if new_value is None:
            return

        if not isinstance(new_value, list):
            raise InvalidTypeError('domains is expected to be a list of Domain strings')

        if all(isinstance(domain, dict) for domain in new_value):
            analytics_domains = []
            for domain in new_value:
                domain_id = domain.get('id')
                domain_url = domain.get('url')
                analytics_domain = AnalyticsDomain(id_=domain_id, url=domain_url)
                analytics_domains.append(analytics_domain)
            self._domains = analytics_domains
        else:
            self._domains = new_value

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        name = json_object.get('name')
        custom_data = json_object.get('customData')
        license_key = json_object.get('licenseKey')
        datapoints = json_object.get('datapoints')
        max_datapoints = json_object.get('maxDatapoints')
        domains = json_object.get('domains')

        analytics_license = AnalyticsLicense(id_=id_, custom_data=custom_data, name=name, license_key=license_key,
                                             datapoints=datapoints, max_datapoints=max_datapoints, domains=domains)
        return analytics_license
