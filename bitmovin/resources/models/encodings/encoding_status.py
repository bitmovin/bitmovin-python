from bitmovin.resources import AbstractIdResource


class EncodingStatus(AbstractIdResource):

    def __init__(self, status, number_of_segments=None, id_=None, messages=None, subtasks=None,
                 created_at=None, queued_at=None, finished_at=None, error_at=None):
        super().__init__(id_=id_)

        self.status = status
        self.numberOfSegments = number_of_segments
        self.messages = messages
        self.subtasks = subtasks
        self.created_at = created_at
        self.queued_at = queued_at
        self.finished_at = finished_at
        self.error_at = error_at

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        status = json_object['status']
        messages = json_object.get('messages')
        subtasks = json_object.get('subtasks')
        created_at = json_object.get('createdAt')
        queued_at = json_object.get('queuedAt')
        finished_at = json_object.get('finishedAt')
        error_at = json_object.get('errorAt')
        number_of_segments = json_object.get('numberOfSegments')

        encoding_status = EncodingStatus(status=status, number_of_segments=number_of_segments, id_=id_,
                                         messages=messages, subtasks=subtasks, created_at=created_at,
                                         queued_at=queued_at, finished_at=finished_at, error_at=error_at)
        return encoding_status
