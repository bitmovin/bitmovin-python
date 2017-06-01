from .id3_tag_service import ID3TagService
from .raw_id3_tag_service import RawID3
from .plain_text_id3_tag_service import PlainTextID3
from .frame_id_id3_tag_service import FrameIdID3


class ProgressiveTSID3Service(ID3TagService):

    MUXING_TYPE_URL = 'progressive-ts'

    def __init__(self, http_client):
        super().__init__(http_client=http_client)
        self.Raw = RawID3(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.FrameId = FrameIdID3(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.PlainText = PlainTextID3(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
