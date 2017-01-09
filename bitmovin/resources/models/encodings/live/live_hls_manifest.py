#!/usr/bin/env python

from bitmovin.utils import Serializable


class LiveHlsManifest(Serializable):
    def __init__(self, manifest_id: str, time_shift: float = None):
        super().__init__()
        self.manifestId = manifest_id
        self.timeshift = time_shift
