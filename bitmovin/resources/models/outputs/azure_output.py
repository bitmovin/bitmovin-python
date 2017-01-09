from . import AbstractOutput


class AzureOutput(AbstractOutput):

    def __init__(self, account_name, account_key, container, id_=None, custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.accountName = account_name
        self.accountKey = account_key
        self.container = container

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        container = json_object['container']
        account_name = json_object.get('accountName')
        account_key = json_object.get('accountKey')
        name = json_object.get('name')
        description = json_object.get('description')
        azure_output = AzureOutput(
            account_name=account_name, account_key=account_key, container=container, id_=id_,
            name=name, description=description)
        return azure_output
