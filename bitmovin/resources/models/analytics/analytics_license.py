from bitmovin.resources.models import AbstractModel
from .domain import AnalyticsDomain


class AnalyticsLicense(AbstractModel):
    def __init__(self, id_, name, licenseKey, domains=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.name = name
        self.licenseKey = licenseKey
        self.domains = domains

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        name = json_object['name']
        domains = []
        for domain in json_object['domains']:
            domains.append(AnalyticsDomain(id_=domain['id'], url=domain['url']))
        licenseKey = json_object['licenseKey']
        return AnalyticsLicense(id_=id_, name=name, domains=domains,licenseKey=licenseKey)

