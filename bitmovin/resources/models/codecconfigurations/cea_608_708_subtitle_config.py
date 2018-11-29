from bitmovin.utils import Serializable


class Cea608708SubtitleConfig(Serializable):
    def __init__(self, passthrough_activated=None):
        super().__init__()

        self.passthroughActivated = passthrough_activated

    @classmethod
    def parse_from_json_object(cls, json_object):
        passthrough_activated = json_object['passthroughActivated']

        return Cea608708SubtitleConfig(passthrough_activated=passthrough_activated)
