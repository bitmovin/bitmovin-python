#!/usr/bin/env python

from typing import List

from bitmovin.utils import Serializable
from .live_dash_manifest import LiveDashManifest
from .live_hls_manifest import LiveHlsManifest


class LiveStreamConfiguration(Serializable):
    def __init__(self, stream_key: str,
                 live_dash_manifests: List[LiveDashManifest] = None,
                 live_hls_manifests: List[LiveHlsManifest] = None):
        super().__init__()
        self.streamKey = stream_key
        self.dashManifests = live_dash_manifests
        self.hlsManifests = live_hls_manifests
