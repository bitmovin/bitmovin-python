from bitmovin.resources.models import AbstractModel
from bitmovin.resources import AbstractNameDescriptionResource


class AbstractStreamCondition(AbstractNameDescriptionResource, AbstractModel):

    def __init__(self, id_, name=None, description=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)

