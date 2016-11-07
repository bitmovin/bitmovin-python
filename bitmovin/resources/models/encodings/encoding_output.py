from bitmovin.errors import InvalidTypeError
from bitmovin.resources import AbstractIdResource
from bitmovin.utils import Serializable
from .acl_entry import ACLEntry


class EncodingOutput(AbstractIdResource, Serializable):

    def __init__(self, output_id, output_path=None, acl=None, id_=None):
        super().__init__(id_=id_)
        self._acl = None
        self.outputId = output_id
        self.outputPath = output_path
        self.acl = acl

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        output_id = json_object['outputId']
        output_path = json_object.get('outputPath')
        acl = json_object.get('acl')

        encoding_output = EncodingOutput(output_id=output_id, output_path=output_path, acl=acl, id_=id_)
        return encoding_output

    @property
    def acl(self):
        return self._acl

    @acl.setter
    def acl(self, new_acl):
        if new_acl is None:
            return

        if not isinstance(new_acl, list):
            raise InvalidTypeError('new_acl has to be a list of ACLEntry objects')

        if all(isinstance(acl_entry, ACLEntry) for acl_entry in new_acl):
            self._acl = new_acl
        else:
            acl_entries = []
            for json_object in new_acl:
                acl_entry = ACLEntry.parse_from_json_object(json_object)
                acl_entries.append(acl_entry)
            self._acl = acl_entries

    def serialize(self):
        serialized = super().serialize()
        serialized['acl'] = self.acl
        return serialized
