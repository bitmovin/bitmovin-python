from bitmovin.resources.models import AbstractModel
from bitmovin.resources import AbstractNameDescriptionResource


class AbstractOutput(AbstractNameDescriptionResource, AbstractModel):

    def __init__(self, id_, name, custom_data=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)

