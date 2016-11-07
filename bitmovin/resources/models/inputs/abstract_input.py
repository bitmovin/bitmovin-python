from bitmovin.resources.models import AbstractModel


class AbstractInput(AbstractModel):

    def __init__(self, id_, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)

