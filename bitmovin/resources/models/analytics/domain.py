from bitmovin.utils import Serializable
from bitmovin.resources.models import AbstractModel

class AnalyticsDomain(AbstractModel):
    def __init__(self, id_, url):
        super().__init__(id_=id_)
        self.url = url

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        url = json_object['url']
        return AnalyticsDomain(id_=id_, url=url)
