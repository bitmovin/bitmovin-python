from bitmovin.resources.models import AbstractModel


class AnalyticsDomain(AbstractModel):
    def __init__(self, url, id_=None):
        super().__init__(id_=id_)
        self.url = url

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        url = json_object.get('url')
        return AnalyticsDomain(id_=id_, url=url)
