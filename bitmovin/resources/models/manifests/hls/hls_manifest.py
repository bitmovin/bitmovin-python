from ..abstract_manifest import AbstractManifest
from bitmovin.resources.enums.hls_version import HlsVersion


class HlsManifest(AbstractManifest):

    def __init__(self, manifest_name, outputs, name=None, description=None, id_=None, custom_data=None,
                 hls_media_playlist_version=None, hls_master_playlist_version=None):
        super().__init__(id_=id_, custom_data=custom_data, manifest_name=manifest_name, outputs=outputs,
                         name=name, description=description)

        self._hlsMediaPlaylistVersion = None
        self.hlsMediaPlaylistVersion = hls_media_playlist_version
        self._hlsMasterPlaylistVersion = None
        self.hlsMasterPlaylistVersion = hls_master_playlist_version

    @property
    def hlsMediaPlaylistVersion(self):
        return self._hlsMediaPlaylistVersion

    @hlsMediaPlaylistVersion.setter
    def hlsMediaPlaylistVersion(self, new_hls_media_playlist_version):
        if new_hls_media_playlist_version is None:
            self._hlsMediaPlaylistVersion = None
        elif isinstance(new_hls_media_playlist_version, HlsVersion):
            self._hlsMediaPlaylistVersion = new_hls_media_playlist_version.value
        elif isinstance(new_hls_media_playlist_version, int):
            self._hlsMediaPlaylistVersion = new_hls_media_playlist_version
        else:
            raise InvalidTypeError('hlsMediaPlaylistVersion has to be of type HlsVersion')

    @property
    def hlsMasterPlaylistVersion(self):
        return self._hlsMasterPlaylistVersion

    @hlsMasterPlaylistVersion.setter
    def hlsMasterPlaylistVersion(self, new_hls_master_playlist_version):
        if new_hls_master_playlist_version is None:
            self._hlsMasterPlaylistVersion = None
        elif isinstance(new_hls_master_playlist_version, HlsVersion):
            self._hlsMasterPlaylistVersion = new_hls_master_playlist_version.value
        elif isinstance(new_hls_master_playlist_version, int):
            self._hlsMasterPlaylistVersion = new_hls_master_playlist_version
        else:
            raise InvalidTypeError('hlsMasterPlaylistVersion has to be of type HlsVersion')

    @classmethod
    def parse_from_json_object(cls, json_object):
        manifest = AbstractManifest.parse_from_json_object(json_object=json_object)
        id_ = manifest.id
        manifest_name = manifest.manifestName
        name = manifest.name
        description = manifest.description
        custom_data = manifest.customData
        outputs = manifest.outputs
        hls_media_playlist_version = json_object.get('hlsMediaPlaylistVersion')
        hls_master_playlist_version = json_object.get('hlsMasterPlaylistVersion')

        hls_manifest = HlsManifest(id_=id_, manifest_name=manifest_name, custom_data=custom_data,
                                   outputs=outputs, name=name, description=description,
                                   hls_media_playlist_version=hls_media_playlist_version,
                                   hls_master_playlist_version=hls_master_playlist_version)

        return hls_manifest

    def serialize(self):
        serialized = super().serialize()
        serialized['hlsMediaPlaylistVersion'] = self.hlsMediaPlaylistVersion
        serialized['hlsMasterPlaylistVersion'] = self.hlsMasterPlaylistVersion

        return serialized
