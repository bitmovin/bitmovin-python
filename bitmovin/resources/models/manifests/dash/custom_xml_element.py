from bitmovin.resources.models import AbstractModel


class CustomXMLElement(AbstractModel):

    def __init__(self, data, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.data = data

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        data = json_object.get('data')

        custom_xml_element = CustomXMLElement(id_=id_, custom_data=custom_data, data=data)

        return custom_xml_element
