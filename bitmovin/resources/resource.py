import abc


class Resource:
    __metaclass__ = abc.ABCMeta

    def __init__(self, **kwargs):
        super().__init__()
