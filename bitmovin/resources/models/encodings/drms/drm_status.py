from bitmovin.resources import AbstractIdResource


class DRMStatus(AbstractIdResource):

    def __init__(self, status, id_=None):
        super().__init__(id_=id_)
        self.status = status

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        status = json_object['status']

        drm_status = DRMStatus(status=status, id_=id_)
        return drm_status
