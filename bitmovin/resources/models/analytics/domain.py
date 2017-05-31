from bitmovin.utils import Serializable
from bitmovin.resources.models import AbstractModel

class AnalyticsDomain(AbstractModel):
    def __init__(self, id_, url):
        super().__init__(id_=id_)
        self.url = url
