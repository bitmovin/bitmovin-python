#!/usr/bin/env python

from bitmovin.utils import Serializable


class LiveDashManifest(Serializable):
    def __init__(self, manifest_id: str, time_shift: float = None, live_edge_offset: float = None):
        super().__init__()
        self.manifestId = manifest_id
        self.timeshift = time_shift
        self.liveEdgeOffset = live_edge_offset
