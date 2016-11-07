from bitmovin.resources import AbstractIdResource


class ManifestStatus(AbstractIdResource):

    def __init__(self, status=None, eta=None, progress=None, messages=None, subtasks=None, id_=None):
        super().__init__(id_=id_)
        self.status = status
        self.eta = eta
        self.progress = progress
        self.messages = messages
        self.subtasks = subtasks

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        status = json_object['status']
        eta = json_object.get('eta')
        progress = json_object.get('progress')
        messages = json_object.get('messages')
        subtasks = json_object.get('subtasks')

        manifest_status = ManifestStatus(status=status, eta=eta, progress=progress, messages=messages,
                                         subtasks=subtasks, id_=id_)
        return manifest_status
