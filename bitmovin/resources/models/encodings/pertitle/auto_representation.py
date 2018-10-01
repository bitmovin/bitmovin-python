from bitmovin.utils import Serializable


class AutoRepresentation(Serializable):
    def __init__(self, adopt_configuration_threshold=None):
        self.adoptConfigurationThreshold = adopt_configuration_threshold
