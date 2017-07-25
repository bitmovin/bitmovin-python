from bitmovin.resources.models import AbstractModel


class Keyframe(AbstractModel):

    def __init__(self, time, segment_cut=None, id_=None):
        super().__init__(id_=id_)
        self.time = time
        self.segmentCut = segment_cut

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        time = json_object.get('time')
        segment_cut = json_object.get('segmentCut')

        keyframe = Keyframe(id_=id_, time=time, segment_cut=segment_cut)
        return keyframe
