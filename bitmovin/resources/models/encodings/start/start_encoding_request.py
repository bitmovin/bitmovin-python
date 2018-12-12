from bitmovin.resources.models.encodings.pertitle import PerTitle
from bitmovin.errors import InvalidTypeError
from bitmovin.resources.enums import EncodingMode
from bitmovin.utils import Serializable

from .start_encoding_trimming import StartEncodingTrimming
from .manifests import VodDashStartManifest, VodHlsStartManifest
from .scheduling import Scheduling
from .tweaks import Tweaks


class StartEncodingRequest(Serializable):
    def __init__(self, trimming=None, scheduling=None, encoding_mode=None, tweaks=None, per_title=None,
                 vod_dash_manifests=None, vod_hls_manifests=None):
        super().__init__()
        self._encoding_mode = None
        self._trimming = None
        self._scheduling = None
        self._tweaks = None
        self._vod_dash_manifests = None
        self._vod_hls_manifests = None
        self._per_title = None
        self.trimming = trimming
        self.scheduling = scheduling
        self.encodingMode = encoding_mode
        self.tweaks = tweaks
        self.vodDashManifests = vod_dash_manifests
        self.vodHlsManifests = vod_hls_manifests
        self.per_title = per_title

    @property
    def trimming(self):
        return self._trimming

    @trimming.setter
    def trimming(self, new_trimming):
        if new_trimming is None:
            self._trimming = None
            return

        if not isinstance(new_trimming, StartEncodingTrimming):
            raise InvalidTypeError(
                'Invalid type {} for trimming: must be StartEncodingTrimming!'.format(type(new_trimming)))

        self._trimming = new_trimming

    @property
    def per_title(self):
        return self._per_title

    @per_title.setter
    def per_title(self, new_per_title):
        if new_per_title is None:
            self._per_title = None
            return

        if not isinstance(new_per_title, PerTitle):
            raise InvalidTypeError(
                'Invalid type {} for per_title: must be PerTitle!'.format(type(new_per_title))
            )

        self._per_title = new_per_title

    @property
    def scheduling(self):
        return self._scheduling

    @scheduling.setter
    def scheduling(self, new_scheduling):
        if new_scheduling is None:
            self._scheduling = None
            return

        if not isinstance(new_scheduling, Scheduling):
            raise InvalidTypeError(
                'Invalid type {} for scheduling: must be an instance of Scheduling!'.format(
                    type(new_scheduling)
                )
            )

        self._scheduling = new_scheduling

    @property
    def encodingMode(self):
        return self._encoding_mode

    @encodingMode.setter
    def encodingMode(self, new_encoding_mode):
        if new_encoding_mode is None:
            self._encoding_mode = None
            return
        if isinstance(new_encoding_mode, str):
            self._encoding_mode = new_encoding_mode
        elif isinstance(new_encoding_mode, EncodingMode):
            self._encoding_mode = new_encoding_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for encodingMode: must be either str or EncodingMode!'.format(type(new_encoding_mode)))

    @property
    def tweaks(self):
        return self._tweaks

    @tweaks.setter
    def tweaks(self, new_tweaks):
        if new_tweaks is None:
            self._tweaks = None
            return

        if not isinstance(new_tweaks, Tweaks):
            raise InvalidTypeError(
                'Invalid type {} for tweaks: must be an instance of Tweaks!'.format(type(new_tweaks)))

        self._tweaks = new_tweaks

    @property
    def vodDashManifests(self):
        return self._vod_dash_manifests

    @vodDashManifests.setter
    def vodDashManifests(self, new_vod_dash_manifests):
        if new_vod_dash_manifests is None:
            self._vod_dash_manifests = None
            return

        if not isinstance(new_vod_dash_manifests, list):
            raise InvalidTypeError('new_vod_dash_manifests has to be a list of VodDashManifest objects')

        if all(isinstance(start_manifest, VodDashStartManifest) for start_manifest in new_vod_dash_manifests):
            self._vod_dash_manifests = new_vod_dash_manifests
        else:
            start_manifests = []
            for json_object in new_vod_dash_manifests:
                start_manifest = VodDashStartManifest.parse_from_json_object(json_object=json_object)
                start_manifests.append(start_manifest)
            self._vod_dash_manifests = start_manifests

    @property
    def vodHlsManifests(self):
        return self._vod_hls_manifests

    @vodHlsManifests.setter
    def vodHlsManifests(self, new_vod_hls_manifests):
        if new_vod_hls_manifests is None:
            self._vod_hls_manifests = None
            return

        if not isinstance(new_vod_hls_manifests, list):
            raise InvalidTypeError('new_vod_hls_manifests has to be a list of VodHlsManifest objects')

        if all(isinstance(start_manifest, VodHlsStartManifest) for start_manifest in new_vod_hls_manifests):
            self._vod_hls_manifests = new_vod_hls_manifests
        else:
            start_manifests = []
            for json_object in new_vod_hls_manifests:
                start_manifest = VodHlsStartManifest.parse_from_json_object(json_object=json_object)
                start_manifests.append(start_manifest)
            self._vod_hls_manifests = start_manifests

    def serialize(self):
        serialized = super().serialize()
        serialized['trimming'] = self.trimming
        serialized['scheduling'] = self.scheduling
        serialized['encodingMode'] = self.encodingMode
        serialized['tweaks'] = self.tweaks
        serialized['perTitle'] = self.per_title
        serialized['vodDashManifests'] = self.vodDashManifests
        serialized['vodHlsManifests'] = self.vodHlsManifests
        return serialized
