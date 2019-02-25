# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class AnalyticsImpressionDetails(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AnalyticsImpressionDetails, self).openapi_types
        types.update({
            'ad': 'int',
            'analytics_version': 'str',
            'asn': 'int',
            'audio_bitrate': 'int',
            'autoplay': 'bool',
            'browser': 'str',
            'browser_version_major': 'str',
            'browser_version_minor': 'str',
            'buffered': 'int',
            'cdn_provider': 'str',
            'city': 'str',
            'client_time': 'int',
            'country': 'str',
            'custom_user_id': 'str',
            'custom_data1': 'str',
            'custom_data2': 'str',
            'custom_data3': 'str',
            'custom_data4': 'str',
            'custom_data5': 'str',
            'device_type': 'str',
            'domain': 'str',
            'drm_load_time': 'int',
            'drm_type': 'str',
            'dropped_frames': 'int',
            'duration': 'int',
            'error_code': 'int',
            'error_message': 'str',
            'experiment_name': 'str',
            'impression_id': 'str',
            'ip_address': 'str',
            'is_casting': 'bool',
            'is_live': 'bool',
            'is_muted': 'bool',
            'isp': 'str',
            'language': 'str',
            'license_key': 'str',
            'operating_system': 'str',
            'operating_system_version_major': 'str',
            'operating_system_version_minor': 'str',
            'page_load_time': 'int',
            'page_load_type': 'int',
            'path': 'str',
            'paused': 'int',
            'platform': 'str',
            'played': 'int',
            'player': 'str',
            'player_key': 'str',
            'player_startuptime': 'int',
            'player_tech': 'str',
            'player_version': 'str',
            'region': 'str',
            'screen_height': 'int',
            'screen_width': 'int',
            'seeked': 'int',
            'sequence_number': 'int',
            'size': 'str',
            'startup_time': 'int',
            'state': 'str',
            'stream_format': 'str',
            'time': 'int',
            'user_id': 'str',
            'video_bitrate': 'int',
            'video_duration': 'int',
            'video_id': 'str',
            'video_title': 'str',
            'video_playback_height': 'int',
            'video_playback_width': 'int',
            'video_startup_time': 'int',
            'videotime_end': 'int',
            'videotime_start': 'int',
            'video_window_height': 'int',
            'video_window_width': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AnalyticsImpressionDetails, self).attribute_map
        attributes.update({
            'ad': 'ad',
            'analytics_version': 'analyticsVersion',
            'asn': 'asn',
            'audio_bitrate': 'audioBitrate',
            'autoplay': 'autoplay',
            'browser': 'browser',
            'browser_version_major': 'browserVersionMajor',
            'browser_version_minor': 'browserVersionMinor',
            'buffered': 'buffered',
            'cdn_provider': 'cdnProvider',
            'city': 'city',
            'client_time': 'clientTime',
            'country': 'country',
            'custom_user_id': 'customUserId',
            'custom_data1': 'customData1',
            'custom_data2': 'customData2',
            'custom_data3': 'customData3',
            'custom_data4': 'customData4',
            'custom_data5': 'customData5',
            'device_type': 'deviceType',
            'domain': 'domain',
            'drm_load_time': 'drmLoadTime',
            'drm_type': 'drmType',
            'dropped_frames': 'droppedFrames',
            'duration': 'duration',
            'error_code': 'errorCode',
            'error_message': 'errorMessage',
            'experiment_name': 'experimentName',
            'impression_id': 'impressionId',
            'ip_address': 'ipAddress',
            'is_casting': 'isCasting',
            'is_live': 'isLive',
            'is_muted': 'isMuted',
            'isp': 'isp',
            'language': 'language',
            'license_key': 'licenseKey',
            'operating_system': 'operatingSystem',
            'operating_system_version_major': 'operatingSystemVersionMajor',
            'operating_system_version_minor': 'operatingSystemVersionMinor',
            'page_load_time': 'pageLoadTime',
            'page_load_type': 'pageLoadType',
            'path': 'path',
            'paused': 'paused',
            'platform': 'platform',
            'played': 'played',
            'player': 'player',
            'player_key': 'playerKey',
            'player_startuptime': 'playerStartuptime',
            'player_tech': 'playerTech',
            'player_version': 'playerVersion',
            'region': 'region',
            'screen_height': 'screenHeight',
            'screen_width': 'screenWidth',
            'seeked': 'seeked',
            'sequence_number': 'sequenceNumber',
            'size': 'size',
            'startup_time': 'startupTime',
            'state': 'state',
            'stream_format': 'streamFormat',
            'time': 'time',
            'user_id': 'userId',
            'video_bitrate': 'videoBitrate',
            'video_duration': 'videoDuration',
            'video_id': 'videoId',
            'video_title': 'videoTitle',
            'video_playback_height': 'videoPlaybackHeight',
            'video_playback_width': 'videoPlaybackWidth',
            'video_startup_time': 'videoStartupTime',
            'videotime_end': 'videotimeEnd',
            'videotime_start': 'videotimeStart',
            'video_window_height': 'videoWindowHeight',
            'video_window_width': 'videoWindowWidth'
        })
        return attributes

    def __init__(self, ad=None, analytics_version=None, asn=None, audio_bitrate=None, autoplay=None, browser=None, browser_version_major=None, browser_version_minor=None, buffered=None, cdn_provider=None, city=None, client_time=None, country=None, custom_user_id=None, custom_data1=None, custom_data2=None, custom_data3=None, custom_data4=None, custom_data5=None, device_type=None, domain=None, drm_load_time=None, drm_type=None, dropped_frames=None, duration=None, error_code=None, error_message=None, experiment_name=None, impression_id=None, ip_address=None, is_casting=None, is_live=None, is_muted=None, isp=None, language=None, license_key=None, operating_system=None, operating_system_version_major=None, operating_system_version_minor=None, page_load_time=None, page_load_type=None, path=None, paused=None, platform=None, played=None, player=None, player_key=None, player_startuptime=None, player_tech=None, player_version=None, region=None, screen_height=None, screen_width=None, seeked=None, sequence_number=None, size=None, startup_time=None, state=None, stream_format=None, time=None, user_id=None, video_bitrate=None, video_duration=None, video_id=None, video_title=None, video_playback_height=None, video_playback_width=None, video_startup_time=None, videotime_end=None, videotime_start=None, video_window_height=None, video_window_width=None, *args, **kwargs):
        super(AnalyticsImpressionDetails, self).__init__(*args, **kwargs)

        self._ad = None
        self._analytics_version = None
        self._asn = None
        self._audio_bitrate = None
        self._autoplay = None
        self._browser = None
        self._browser_version_major = None
        self._browser_version_minor = None
        self._buffered = None
        self._cdn_provider = None
        self._city = None
        self._client_time = None
        self._country = None
        self._custom_user_id = None
        self._custom_data1 = None
        self._custom_data2 = None
        self._custom_data3 = None
        self._custom_data4 = None
        self._custom_data5 = None
        self._device_type = None
        self._domain = None
        self._drm_load_time = None
        self._drm_type = None
        self._dropped_frames = None
        self._duration = None
        self._error_code = None
        self._error_message = None
        self._experiment_name = None
        self._impression_id = None
        self._ip_address = None
        self._is_casting = None
        self._is_live = None
        self._is_muted = None
        self._isp = None
        self._language = None
        self._license_key = None
        self._operating_system = None
        self._operating_system_version_major = None
        self._operating_system_version_minor = None
        self._page_load_time = None
        self._page_load_type = None
        self._path = None
        self._paused = None
        self._platform = None
        self._played = None
        self._player = None
        self._player_key = None
        self._player_startuptime = None
        self._player_tech = None
        self._player_version = None
        self._region = None
        self._screen_height = None
        self._screen_width = None
        self._seeked = None
        self._sequence_number = None
        self._size = None
        self._startup_time = None
        self._state = None
        self._stream_format = None
        self._time = None
        self._user_id = None
        self._video_bitrate = None
        self._video_duration = None
        self._video_id = None
        self._video_title = None
        self._video_playback_height = None
        self._video_playback_width = None
        self._video_startup_time = None
        self._videotime_end = None
        self._videotime_start = None
        self._video_window_height = None
        self._video_window_width = None
        self.discriminator = None

        if ad is not None:
            self.ad = ad
        if analytics_version is not None:
            self.analytics_version = analytics_version
        if asn is not None:
            self.asn = asn
        if audio_bitrate is not None:
            self.audio_bitrate = audio_bitrate
        if autoplay is not None:
            self.autoplay = autoplay
        if browser is not None:
            self.browser = browser
        if browser_version_major is not None:
            self.browser_version_major = browser_version_major
        if browser_version_minor is not None:
            self.browser_version_minor = browser_version_minor
        if buffered is not None:
            self.buffered = buffered
        if cdn_provider is not None:
            self.cdn_provider = cdn_provider
        if city is not None:
            self.city = city
        if client_time is not None:
            self.client_time = client_time
        if country is not None:
            self.country = country
        if custom_user_id is not None:
            self.custom_user_id = custom_user_id
        if custom_data1 is not None:
            self.custom_data1 = custom_data1
        if custom_data2 is not None:
            self.custom_data2 = custom_data2
        if custom_data3 is not None:
            self.custom_data3 = custom_data3
        if custom_data4 is not None:
            self.custom_data4 = custom_data4
        if custom_data5 is not None:
            self.custom_data5 = custom_data5
        if device_type is not None:
            self.device_type = device_type
        if domain is not None:
            self.domain = domain
        if drm_load_time is not None:
            self.drm_load_time = drm_load_time
        if drm_type is not None:
            self.drm_type = drm_type
        if dropped_frames is not None:
            self.dropped_frames = dropped_frames
        if duration is not None:
            self.duration = duration
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if experiment_name is not None:
            self.experiment_name = experiment_name
        self.impression_id = impression_id
        if ip_address is not None:
            self.ip_address = ip_address
        if is_casting is not None:
            self.is_casting = is_casting
        if is_live is not None:
            self.is_live = is_live
        if is_muted is not None:
            self.is_muted = is_muted
        if isp is not None:
            self.isp = isp
        if language is not None:
            self.language = language
        if license_key is not None:
            self.license_key = license_key
        if operating_system is not None:
            self.operating_system = operating_system
        if operating_system_version_major is not None:
            self.operating_system_version_major = operating_system_version_major
        if operating_system_version_minor is not None:
            self.operating_system_version_minor = operating_system_version_minor
        if page_load_time is not None:
            self.page_load_time = page_load_time
        if page_load_type is not None:
            self.page_load_type = page_load_type
        if path is not None:
            self.path = path
        if paused is not None:
            self.paused = paused
        if platform is not None:
            self.platform = platform
        if played is not None:
            self.played = played
        if player is not None:
            self.player = player
        if player_key is not None:
            self.player_key = player_key
        if player_startuptime is not None:
            self.player_startuptime = player_startuptime
        if player_tech is not None:
            self.player_tech = player_tech
        if player_version is not None:
            self.player_version = player_version
        if region is not None:
            self.region = region
        if screen_height is not None:
            self.screen_height = screen_height
        if screen_width is not None:
            self.screen_width = screen_width
        if seeked is not None:
            self.seeked = seeked
        if sequence_number is not None:
            self.sequence_number = sequence_number
        if size is not None:
            self.size = size
        if startup_time is not None:
            self.startup_time = startup_time
        if state is not None:
            self.state = state
        if stream_format is not None:
            self.stream_format = stream_format
        if time is not None:
            self.time = time
        if user_id is not None:
            self.user_id = user_id
        if video_bitrate is not None:
            self.video_bitrate = video_bitrate
        if video_duration is not None:
            self.video_duration = video_duration
        if video_id is not None:
            self.video_id = video_id
        if video_title is not None:
            self.video_title = video_title
        if video_playback_height is not None:
            self.video_playback_height = video_playback_height
        if video_playback_width is not None:
            self.video_playback_width = video_playback_width
        if video_startup_time is not None:
            self.video_startup_time = video_startup_time
        if videotime_end is not None:
            self.videotime_end = videotime_end
        if videotime_start is not None:
            self.videotime_start = videotime_start
        if video_window_height is not None:
            self.video_window_height = video_window_height
        if video_window_width is not None:
            self.video_window_width = video_window_width

    @property
    def ad(self):
        """Gets the ad of this AnalyticsImpressionDetails.

        Is an ad playing. 0 indicates no, 1 indicates yes

        :return: The ad of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """Sets the ad of this AnalyticsImpressionDetails.

        Is an ad playing. 0 indicates no, 1 indicates yes

        :param ad: The ad of this AnalyticsImpressionDetails.
        :type: int
        """

        if ad is not None:
            if not isinstance(ad, int):
                raise TypeError("Invalid type for `ad`, type has to be `int`")

            self._ad = ad


    @property
    def analytics_version(self):
        """Gets the analytics_version of this AnalyticsImpressionDetails.

        Collector version

        :return: The analytics_version of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._analytics_version

    @analytics_version.setter
    def analytics_version(self, analytics_version):
        """Sets the analytics_version of this AnalyticsImpressionDetails.

        Collector version

        :param analytics_version: The analytics_version of this AnalyticsImpressionDetails.
        :type: str
        """

        if analytics_version is not None:
            if not isinstance(analytics_version, str):
                raise TypeError("Invalid type for `analytics_version`, type has to be `str`")

            self._analytics_version = analytics_version


    @property
    def asn(self):
        """Gets the asn of this AnalyticsImpressionDetails.

        Autonomous System Number inferred from the IP address

        :return: The asn of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this AnalyticsImpressionDetails.

        Autonomous System Number inferred from the IP address

        :param asn: The asn of this AnalyticsImpressionDetails.
        :type: int
        """

        if asn is not None:
            if not isinstance(asn, int):
                raise TypeError("Invalid type for `asn`, type has to be `int`")

            self._asn = asn


    @property
    def audio_bitrate(self):
        """Gets the audio_bitrate of this AnalyticsImpressionDetails.

        Audio Bitrate

        :return: The audio_bitrate of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._audio_bitrate

    @audio_bitrate.setter
    def audio_bitrate(self, audio_bitrate):
        """Sets the audio_bitrate of this AnalyticsImpressionDetails.

        Audio Bitrate

        :param audio_bitrate: The audio_bitrate of this AnalyticsImpressionDetails.
        :type: int
        """

        if audio_bitrate is not None:
            if not isinstance(audio_bitrate, int):
                raise TypeError("Invalid type for `audio_bitrate`, type has to be `int`")

            self._audio_bitrate = audio_bitrate


    @property
    def autoplay(self):
        """Gets the autoplay of this AnalyticsImpressionDetails.

        Autoplay enabled

        :return: The autoplay of this AnalyticsImpressionDetails.
        :rtype: bool
        """
        return self._autoplay

    @autoplay.setter
    def autoplay(self, autoplay):
        """Sets the autoplay of this AnalyticsImpressionDetails.

        Autoplay enabled

        :param autoplay: The autoplay of this AnalyticsImpressionDetails.
        :type: bool
        """

        if autoplay is not None:
            if not isinstance(autoplay, bool):
                raise TypeError("Invalid type for `autoplay`, type has to be `bool`")

            self._autoplay = autoplay


    @property
    def browser(self):
        """Gets the browser of this AnalyticsImpressionDetails.

        Browser name

        :return: The browser of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """Sets the browser of this AnalyticsImpressionDetails.

        Browser name

        :param browser: The browser of this AnalyticsImpressionDetails.
        :type: str
        """

        if browser is not None:
            if not isinstance(browser, str):
                raise TypeError("Invalid type for `browser`, type has to be `str`")

            self._browser = browser


    @property
    def browser_version_major(self):
        """Gets the browser_version_major of this AnalyticsImpressionDetails.

        Browser version major

        :return: The browser_version_major of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._browser_version_major

    @browser_version_major.setter
    def browser_version_major(self, browser_version_major):
        """Sets the browser_version_major of this AnalyticsImpressionDetails.

        Browser version major

        :param browser_version_major: The browser_version_major of this AnalyticsImpressionDetails.
        :type: str
        """

        if browser_version_major is not None:
            if not isinstance(browser_version_major, str):
                raise TypeError("Invalid type for `browser_version_major`, type has to be `str`")

            self._browser_version_major = browser_version_major


    @property
    def browser_version_minor(self):
        """Gets the browser_version_minor of this AnalyticsImpressionDetails.

        Browser version minor

        :return: The browser_version_minor of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._browser_version_minor

    @browser_version_minor.setter
    def browser_version_minor(self, browser_version_minor):
        """Sets the browser_version_minor of this AnalyticsImpressionDetails.

        Browser version minor

        :param browser_version_minor: The browser_version_minor of this AnalyticsImpressionDetails.
        :type: str
        """

        if browser_version_minor is not None:
            if not isinstance(browser_version_minor, str):
                raise TypeError("Invalid type for `browser_version_minor`, type has to be `str`")

            self._browser_version_minor = browser_version_minor


    @property
    def buffered(self):
        """Gets the buffered of this AnalyticsImpressionDetails.

        Millisecond the player buffered

        :return: The buffered of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._buffered

    @buffered.setter
    def buffered(self, buffered):
        """Sets the buffered of this AnalyticsImpressionDetails.

        Millisecond the player buffered

        :param buffered: The buffered of this AnalyticsImpressionDetails.
        :type: int
        """

        if buffered is not None:
            if not isinstance(buffered, int):
                raise TypeError("Invalid type for `buffered`, type has to be `int`")

            self._buffered = buffered


    @property
    def cdn_provider(self):
        """Gets the cdn_provider of this AnalyticsImpressionDetails.

        CDN Provider

        :return: The cdn_provider of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._cdn_provider

    @cdn_provider.setter
    def cdn_provider(self, cdn_provider):
        """Sets the cdn_provider of this AnalyticsImpressionDetails.

        CDN Provider

        :param cdn_provider: The cdn_provider of this AnalyticsImpressionDetails.
        :type: str
        """

        if cdn_provider is not None:
            if not isinstance(cdn_provider, str):
                raise TypeError("Invalid type for `cdn_provider`, type has to be `str`")

            self._cdn_provider = cdn_provider


    @property
    def city(self):
        """Gets the city of this AnalyticsImpressionDetails.

        City

        :return: The city of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AnalyticsImpressionDetails.

        City

        :param city: The city of this AnalyticsImpressionDetails.
        :type: str
        """

        if city is not None:
            if not isinstance(city, str):
                raise TypeError("Invalid type for `city`, type has to be `str`")

            self._city = city


    @property
    def client_time(self):
        """Gets the client_time of this AnalyticsImpressionDetails.

        Current time of the client

        :return: The client_time of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._client_time

    @client_time.setter
    def client_time(self, client_time):
        """Sets the client_time of this AnalyticsImpressionDetails.

        Current time of the client

        :param client_time: The client_time of this AnalyticsImpressionDetails.
        :type: int
        """

        if client_time is not None:
            if not isinstance(client_time, int):
                raise TypeError("Invalid type for `client_time`, type has to be `int`")

            self._client_time = client_time


    @property
    def country(self):
        """Gets the country of this AnalyticsImpressionDetails.

        Country

        :return: The country of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AnalyticsImpressionDetails.

        Country

        :param country: The country of this AnalyticsImpressionDetails.
        :type: str
        """

        if country is not None:
            if not isinstance(country, str):
                raise TypeError("Invalid type for `country`, type has to be `str`")

            self._country = country


    @property
    def custom_user_id(self):
        """Gets the custom_user_id of this AnalyticsImpressionDetails.

        Custom user ID

        :return: The custom_user_id of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._custom_user_id

    @custom_user_id.setter
    def custom_user_id(self, custom_user_id):
        """Sets the custom_user_id of this AnalyticsImpressionDetails.

        Custom user ID

        :param custom_user_id: The custom_user_id of this AnalyticsImpressionDetails.
        :type: str
        """

        if custom_user_id is not None:
            if not isinstance(custom_user_id, str):
                raise TypeError("Invalid type for `custom_user_id`, type has to be `str`")

            self._custom_user_id = custom_user_id


    @property
    def custom_data1(self):
        """Gets the custom_data1 of this AnalyticsImpressionDetails.

        Free form data set via the customData1 field in the analytics collector configuration

        :return: The custom_data1 of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._custom_data1

    @custom_data1.setter
    def custom_data1(self, custom_data1):
        """Sets the custom_data1 of this AnalyticsImpressionDetails.

        Free form data set via the customData1 field in the analytics collector configuration

        :param custom_data1: The custom_data1 of this AnalyticsImpressionDetails.
        :type: str
        """

        if custom_data1 is not None:
            if not isinstance(custom_data1, str):
                raise TypeError("Invalid type for `custom_data1`, type has to be `str`")

            self._custom_data1 = custom_data1


    @property
    def custom_data2(self):
        """Gets the custom_data2 of this AnalyticsImpressionDetails.

        Free form data set via the customData2 field in the analytics collector configuration

        :return: The custom_data2 of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._custom_data2

    @custom_data2.setter
    def custom_data2(self, custom_data2):
        """Sets the custom_data2 of this AnalyticsImpressionDetails.

        Free form data set via the customData2 field in the analytics collector configuration

        :param custom_data2: The custom_data2 of this AnalyticsImpressionDetails.
        :type: str
        """

        if custom_data2 is not None:
            if not isinstance(custom_data2, str):
                raise TypeError("Invalid type for `custom_data2`, type has to be `str`")

            self._custom_data2 = custom_data2


    @property
    def custom_data3(self):
        """Gets the custom_data3 of this AnalyticsImpressionDetails.

        Free form data set via the customData3 field in the analytics collector configuration

        :return: The custom_data3 of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._custom_data3

    @custom_data3.setter
    def custom_data3(self, custom_data3):
        """Sets the custom_data3 of this AnalyticsImpressionDetails.

        Free form data set via the customData3 field in the analytics collector configuration

        :param custom_data3: The custom_data3 of this AnalyticsImpressionDetails.
        :type: str
        """

        if custom_data3 is not None:
            if not isinstance(custom_data3, str):
                raise TypeError("Invalid type for `custom_data3`, type has to be `str`")

            self._custom_data3 = custom_data3


    @property
    def custom_data4(self):
        """Gets the custom_data4 of this AnalyticsImpressionDetails.

        Free form data set via the customData4 field in the analytics collector configuration

        :return: The custom_data4 of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._custom_data4

    @custom_data4.setter
    def custom_data4(self, custom_data4):
        """Sets the custom_data4 of this AnalyticsImpressionDetails.

        Free form data set via the customData4 field in the analytics collector configuration

        :param custom_data4: The custom_data4 of this AnalyticsImpressionDetails.
        :type: str
        """

        if custom_data4 is not None:
            if not isinstance(custom_data4, str):
                raise TypeError("Invalid type for `custom_data4`, type has to be `str`")

            self._custom_data4 = custom_data4


    @property
    def custom_data5(self):
        """Gets the custom_data5 of this AnalyticsImpressionDetails.

        Free form data set via the customData5 field in the analytics collector configuration

        :return: The custom_data5 of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._custom_data5

    @custom_data5.setter
    def custom_data5(self, custom_data5):
        """Sets the custom_data5 of this AnalyticsImpressionDetails.

        Free form data set via the customData5 field in the analytics collector configuration

        :param custom_data5: The custom_data5 of this AnalyticsImpressionDetails.
        :type: str
        """

        if custom_data5 is not None:
            if not isinstance(custom_data5, str):
                raise TypeError("Invalid type for `custom_data5`, type has to be `str`")

            self._custom_data5 = custom_data5


    @property
    def device_type(self):
        """Gets the device_type of this AnalyticsImpressionDetails.

        Type of the device detected via User Agent

        :return: The device_type of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this AnalyticsImpressionDetails.

        Type of the device detected via User Agent

        :param device_type: The device_type of this AnalyticsImpressionDetails.
        :type: str
        """

        if device_type is not None:
            if not isinstance(device_type, str):
                raise TypeError("Invalid type for `device_type`, type has to be `str`")

            self._device_type = device_type


    @property
    def domain(self):
        """Gets the domain of this AnalyticsImpressionDetails.

        Domain the player was loaded on (.www is stripped away)

        :return: The domain of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AnalyticsImpressionDetails.

        Domain the player was loaded on (.www is stripped away)

        :param domain: The domain of this AnalyticsImpressionDetails.
        :type: str
        """

        if domain is not None:
            if not isinstance(domain, str):
                raise TypeError("Invalid type for `domain`, type has to be `str`")

            self._domain = domain


    @property
    def drm_load_time(self):
        """Gets the drm_load_time of this AnalyticsImpressionDetails.

        Time in milliseconds it took the DRM server to respond

        :return: The drm_load_time of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._drm_load_time

    @drm_load_time.setter
    def drm_load_time(self, drm_load_time):
        """Sets the drm_load_time of this AnalyticsImpressionDetails.

        Time in milliseconds it took the DRM server to respond

        :param drm_load_time: The drm_load_time of this AnalyticsImpressionDetails.
        :type: int
        """

        if drm_load_time is not None:
            if not isinstance(drm_load_time, int):
                raise TypeError("Invalid type for `drm_load_time`, type has to be `int`")

            self._drm_load_time = drm_load_time


    @property
    def drm_type(self):
        """Gets the drm_type of this AnalyticsImpressionDetails.

        DRM system used for this impression

        :return: The drm_type of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._drm_type

    @drm_type.setter
    def drm_type(self, drm_type):
        """Sets the drm_type of this AnalyticsImpressionDetails.

        DRM system used for this impression

        :param drm_type: The drm_type of this AnalyticsImpressionDetails.
        :type: str
        """

        if drm_type is not None:
            if not isinstance(drm_type, str):
                raise TypeError("Invalid type for `drm_type`, type has to be `str`")

            self._drm_type = drm_type


    @property
    def dropped_frames(self):
        """Gets the dropped_frames of this AnalyticsImpressionDetails.

        Dropped frames during playback

        :return: The dropped_frames of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._dropped_frames

    @dropped_frames.setter
    def dropped_frames(self, dropped_frames):
        """Sets the dropped_frames of this AnalyticsImpressionDetails.

        Dropped frames during playback

        :param dropped_frames: The dropped_frames of this AnalyticsImpressionDetails.
        :type: int
        """

        if dropped_frames is not None:
            if not isinstance(dropped_frames, int):
                raise TypeError("Invalid type for `dropped_frames`, type has to be `int`")

            self._dropped_frames = dropped_frames


    @property
    def duration(self):
        """Gets the duration of this AnalyticsImpressionDetails.

        Duration of the sample in milliseconds

        :return: The duration of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AnalyticsImpressionDetails.

        Duration of the sample in milliseconds

        :param duration: The duration of this AnalyticsImpressionDetails.
        :type: int
        """

        if duration is not None:
            if not isinstance(duration, int):
                raise TypeError("Invalid type for `duration`, type has to be `int`")

            self._duration = duration


    @property
    def error_code(self):
        """Gets the error_code of this AnalyticsImpressionDetails.

        Error code

        :return: The error_code of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AnalyticsImpressionDetails.

        Error code

        :param error_code: The error_code of this AnalyticsImpressionDetails.
        :type: int
        """

        if error_code is not None:
            if not isinstance(error_code, int):
                raise TypeError("Invalid type for `error_code`, type has to be `int`")

            self._error_code = error_code


    @property
    def error_message(self):
        """Gets the error_message of this AnalyticsImpressionDetails.

        Error message

        :return: The error_message of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this AnalyticsImpressionDetails.

        Error message

        :param error_message: The error_message of this AnalyticsImpressionDetails.
        :type: str
        """

        if error_message is not None:
            if not isinstance(error_message, str):
                raise TypeError("Invalid type for `error_message`, type has to be `str`")

            self._error_message = error_message


    @property
    def experiment_name(self):
        """Gets the experiment_name of this AnalyticsImpressionDetails.

        A/B test experiment name

        :return: The experiment_name of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        """Sets the experiment_name of this AnalyticsImpressionDetails.

        A/B test experiment name

        :param experiment_name: The experiment_name of this AnalyticsImpressionDetails.
        :type: str
        """

        if experiment_name is not None:
            if not isinstance(experiment_name, str):
                raise TypeError("Invalid type for `experiment_name`, type has to be `str`")

            self._experiment_name = experiment_name


    @property
    def impression_id(self):
        """Gets the impression_id of this AnalyticsImpressionDetails.

        Random UUID that is used to identify a sessions

        :return: The impression_id of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._impression_id

    @impression_id.setter
    def impression_id(self, impression_id):
        """Sets the impression_id of this AnalyticsImpressionDetails.

        Random UUID that is used to identify a sessions

        :param impression_id: The impression_id of this AnalyticsImpressionDetails.
        :type: str
        """

        if impression_id is not None:
            if not isinstance(impression_id, str):
                raise TypeError("Invalid type for `impression_id`, type has to be `str`")

            self._impression_id = impression_id


    @property
    def ip_address(self):
        """Gets the ip_address of this AnalyticsImpressionDetails.

        IP Address of the client

        :return: The ip_address of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this AnalyticsImpressionDetails.

        IP Address of the client

        :param ip_address: The ip_address of this AnalyticsImpressionDetails.
        :type: str
        """

        if ip_address is not None:
            if not isinstance(ip_address, str):
                raise TypeError("Invalid type for `ip_address`, type has to be `str`")

            self._ip_address = ip_address


    @property
    def is_casting(self):
        """Gets the is_casting of this AnalyticsImpressionDetails.

        Is chromecast active

        :return: The is_casting of this AnalyticsImpressionDetails.
        :rtype: bool
        """
        return self._is_casting

    @is_casting.setter
    def is_casting(self, is_casting):
        """Sets the is_casting of this AnalyticsImpressionDetails.

        Is chromecast active

        :param is_casting: The is_casting of this AnalyticsImpressionDetails.
        :type: bool
        """

        if is_casting is not None:
            if not isinstance(is_casting, bool):
                raise TypeError("Invalid type for `is_casting`, type has to be `bool`")

            self._is_casting = is_casting


    @property
    def is_live(self):
        """Gets the is_live of this AnalyticsImpressionDetails.

        Is the stream live or VoD

        :return: The is_live of this AnalyticsImpressionDetails.
        :rtype: bool
        """
        return self._is_live

    @is_live.setter
    def is_live(self, is_live):
        """Sets the is_live of this AnalyticsImpressionDetails.

        Is the stream live or VoD

        :param is_live: The is_live of this AnalyticsImpressionDetails.
        :type: bool
        """

        if is_live is not None:
            if not isinstance(is_live, bool):
                raise TypeError("Invalid type for `is_live`, type has to be `bool`")

            self._is_live = is_live


    @property
    def is_muted(self):
        """Gets the is_muted of this AnalyticsImpressionDetails.

        Is the player muted

        :return: The is_muted of this AnalyticsImpressionDetails.
        :rtype: bool
        """
        return self._is_muted

    @is_muted.setter
    def is_muted(self, is_muted):
        """Sets the is_muted of this AnalyticsImpressionDetails.

        Is the player muted

        :param is_muted: The is_muted of this AnalyticsImpressionDetails.
        :type: bool
        """

        if is_muted is not None:
            if not isinstance(is_muted, bool):
                raise TypeError("Invalid type for `is_muted`, type has to be `bool`")

            self._is_muted = is_muted


    @property
    def isp(self):
        """Gets the isp of this AnalyticsImpressionDetails.

        The users Internet Service Provider inferred via the IP address

        :return: The isp of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this AnalyticsImpressionDetails.

        The users Internet Service Provider inferred via the IP address

        :param isp: The isp of this AnalyticsImpressionDetails.
        :type: str
        """

        if isp is not None:
            if not isinstance(isp, str):
                raise TypeError("Invalid type for `isp`, type has to be `str`")

            self._isp = isp


    @property
    def language(self):
        """Gets the language of this AnalyticsImpressionDetails.

        Language set in the browser

        :return: The language of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AnalyticsImpressionDetails.

        Language set in the browser

        :param language: The language of this AnalyticsImpressionDetails.
        :type: str
        """

        if language is not None:
            if not isinstance(language, str):
                raise TypeError("Invalid type for `language`, type has to be `str`")

            self._language = language


    @property
    def license_key(self):
        """Gets the license_key of this AnalyticsImpressionDetails.

        Analytics license key

        :return: The license_key of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this AnalyticsImpressionDetails.

        Analytics license key

        :param license_key: The license_key of this AnalyticsImpressionDetails.
        :type: str
        """

        if license_key is not None:
            if not isinstance(license_key, str):
                raise TypeError("Invalid type for `license_key`, type has to be `str`")

            self._license_key = license_key


    @property
    def operating_system(self):
        """Gets the operating_system of this AnalyticsImpressionDetails.

        Operating system

        :return: The operating_system of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this AnalyticsImpressionDetails.

        Operating system

        :param operating_system: The operating_system of this AnalyticsImpressionDetails.
        :type: str
        """

        if operating_system is not None:
            if not isinstance(operating_system, str):
                raise TypeError("Invalid type for `operating_system`, type has to be `str`")

            self._operating_system = operating_system


    @property
    def operating_system_version_major(self):
        """Gets the operating_system_version_major of this AnalyticsImpressionDetails.

        Operating system version major

        :return: The operating_system_version_major of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._operating_system_version_major

    @operating_system_version_major.setter
    def operating_system_version_major(self, operating_system_version_major):
        """Sets the operating_system_version_major of this AnalyticsImpressionDetails.

        Operating system version major

        :param operating_system_version_major: The operating_system_version_major of this AnalyticsImpressionDetails.
        :type: str
        """

        if operating_system_version_major is not None:
            if not isinstance(operating_system_version_major, str):
                raise TypeError("Invalid type for `operating_system_version_major`, type has to be `str`")

            self._operating_system_version_major = operating_system_version_major


    @property
    def operating_system_version_minor(self):
        """Gets the operating_system_version_minor of this AnalyticsImpressionDetails.

        Operating system version minor

        :return: The operating_system_version_minor of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._operating_system_version_minor

    @operating_system_version_minor.setter
    def operating_system_version_minor(self, operating_system_version_minor):
        """Sets the operating_system_version_minor of this AnalyticsImpressionDetails.

        Operating system version minor

        :param operating_system_version_minor: The operating_system_version_minor of this AnalyticsImpressionDetails.
        :type: str
        """

        if operating_system_version_minor is not None:
            if not isinstance(operating_system_version_minor, str):
                raise TypeError("Invalid type for `operating_system_version_minor`, type has to be `str`")

            self._operating_system_version_minor = operating_system_version_minor


    @property
    def page_load_time(self):
        """Gets the page_load_time of this AnalyticsImpressionDetails.

        Time in milliseconds the page took to load

        :return: The page_load_time of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._page_load_time

    @page_load_time.setter
    def page_load_time(self, page_load_time):
        """Sets the page_load_time of this AnalyticsImpressionDetails.

        Time in milliseconds the page took to load

        :param page_load_time: The page_load_time of this AnalyticsImpressionDetails.
        :type: int
        """

        if page_load_time is not None:
            if not isinstance(page_load_time, int):
                raise TypeError("Invalid type for `page_load_time`, type has to be `int`")

            self._page_load_time = page_load_time


    @property
    def page_load_type(self):
        """Gets the page_load_type of this AnalyticsImpressionDetails.

        Player load type. 1 = Foreground, 2 = Background

        :return: The page_load_type of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._page_load_type

    @page_load_type.setter
    def page_load_type(self, page_load_type):
        """Sets the page_load_type of this AnalyticsImpressionDetails.

        Player load type. 1 = Foreground, 2 = Background

        :param page_load_type: The page_load_type of this AnalyticsImpressionDetails.
        :type: int
        """

        if page_load_type is not None:
            if not isinstance(page_load_type, int):
                raise TypeError("Invalid type for `page_load_type`, type has to be `int`")

            self._page_load_type = page_load_type


    @property
    def path(self):
        """Gets the path of this AnalyticsImpressionDetails.

        path on the website

        :return: The path of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this AnalyticsImpressionDetails.

        path on the website

        :param path: The path of this AnalyticsImpressionDetails.
        :type: str
        """

        if path is not None:
            if not isinstance(path, str):
                raise TypeError("Invalid type for `path`, type has to be `str`")

            self._path = path


    @property
    def paused(self):
        """Gets the paused of this AnalyticsImpressionDetails.

        Milliseconds the player was paused

        :return: The paused of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this AnalyticsImpressionDetails.

        Milliseconds the player was paused

        :param paused: The paused of this AnalyticsImpressionDetails.
        :type: int
        """

        if paused is not None:
            if not isinstance(paused, int):
                raise TypeError("Invalid type for `paused`, type has to be `int`")

            self._paused = paused


    @property
    def platform(self):
        """Gets the platform of this AnalyticsImpressionDetails.

        Platform the player is running on (web, android, ios)

        :return: The platform of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this AnalyticsImpressionDetails.

        Platform the player is running on (web, android, ios)

        :param platform: The platform of this AnalyticsImpressionDetails.
        :type: str
        """

        if platform is not None:
            if not isinstance(platform, str):
                raise TypeError("Invalid type for `platform`, type has to be `str`")

            self._platform = platform


    @property
    def played(self):
        """Gets the played of this AnalyticsImpressionDetails.

        Milliseconds the player played

        :return: The played of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._played

    @played.setter
    def played(self, played):
        """Sets the played of this AnalyticsImpressionDetails.

        Milliseconds the player played

        :param played: The played of this AnalyticsImpressionDetails.
        :type: int
        """

        if played is not None:
            if not isinstance(played, int):
                raise TypeError("Invalid type for `played`, type has to be `int`")

            self._played = played


    @property
    def player(self):
        """Gets the player of this AnalyticsImpressionDetails.

        Video player being used for this session

        :return: The player of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this AnalyticsImpressionDetails.

        Video player being used for this session

        :param player: The player of this AnalyticsImpressionDetails.
        :type: str
        """

        if player is not None:
            if not isinstance(player, str):
                raise TypeError("Invalid type for `player`, type has to be `str`")

            self._player = player


    @property
    def player_key(self):
        """Gets the player_key of this AnalyticsImpressionDetails.

        Player license key

        :return: The player_key of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._player_key

    @player_key.setter
    def player_key(self, player_key):
        """Sets the player_key of this AnalyticsImpressionDetails.

        Player license key

        :param player_key: The player_key of this AnalyticsImpressionDetails.
        :type: str
        """

        if player_key is not None:
            if not isinstance(player_key, str):
                raise TypeError("Invalid type for `player_key`, type has to be `str`")

            self._player_key = player_key


    @property
    def player_startuptime(self):
        """Gets the player_startuptime of this AnalyticsImpressionDetails.

        Time in milliseconds the player took to start up

        :return: The player_startuptime of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._player_startuptime

    @player_startuptime.setter
    def player_startuptime(self, player_startuptime):
        """Sets the player_startuptime of this AnalyticsImpressionDetails.

        Time in milliseconds the player took to start up

        :param player_startuptime: The player_startuptime of this AnalyticsImpressionDetails.
        :type: int
        """

        if player_startuptime is not None:
            if not isinstance(player_startuptime, int):
                raise TypeError("Invalid type for `player_startuptime`, type has to be `int`")

            self._player_startuptime = player_startuptime


    @property
    def player_tech(self):
        """Gets the player_tech of this AnalyticsImpressionDetails.

        HTML or native playback

        :return: The player_tech of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._player_tech

    @player_tech.setter
    def player_tech(self, player_tech):
        """Sets the player_tech of this AnalyticsImpressionDetails.

        HTML or native playback

        :param player_tech: The player_tech of this AnalyticsImpressionDetails.
        :type: str
        """

        if player_tech is not None:
            if not isinstance(player_tech, str):
                raise TypeError("Invalid type for `player_tech`, type has to be `str`")

            self._player_tech = player_tech


    @property
    def player_version(self):
        """Gets the player_version of this AnalyticsImpressionDetails.

        Player software version

        :return: The player_version of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._player_version

    @player_version.setter
    def player_version(self, player_version):
        """Sets the player_version of this AnalyticsImpressionDetails.

        Player software version

        :param player_version: The player_version of this AnalyticsImpressionDetails.
        :type: str
        """

        if player_version is not None:
            if not isinstance(player_version, str):
                raise TypeError("Invalid type for `player_version`, type has to be `str`")

            self._player_version = player_version


    @property
    def region(self):
        """Gets the region of this AnalyticsImpressionDetails.

        Geographic region (ISO 3166-2 code)

        :return: The region of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AnalyticsImpressionDetails.

        Geographic region (ISO 3166-2 code)

        :param region: The region of this AnalyticsImpressionDetails.
        :type: str
        """

        if region is not None:
            if not isinstance(region, str):
                raise TypeError("Invalid type for `region`, type has to be `str`")

            self._region = region


    @property
    def screen_height(self):
        """Gets the screen_height of this AnalyticsImpressionDetails.

        Screen as reported by the browser

        :return: The screen_height of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._screen_height

    @screen_height.setter
    def screen_height(self, screen_height):
        """Sets the screen_height of this AnalyticsImpressionDetails.

        Screen as reported by the browser

        :param screen_height: The screen_height of this AnalyticsImpressionDetails.
        :type: int
        """

        if screen_height is not None:
            if not isinstance(screen_height, int):
                raise TypeError("Invalid type for `screen_height`, type has to be `int`")

            self._screen_height = screen_height


    @property
    def screen_width(self):
        """Gets the screen_width of this AnalyticsImpressionDetails.

        Screen as reported by the browser

        :return: The screen_width of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._screen_width

    @screen_width.setter
    def screen_width(self, screen_width):
        """Sets the screen_width of this AnalyticsImpressionDetails.

        Screen as reported by the browser

        :param screen_width: The screen_width of this AnalyticsImpressionDetails.
        :type: int
        """

        if screen_width is not None:
            if not isinstance(screen_width, int):
                raise TypeError("Invalid type for `screen_width`, type has to be `int`")

            self._screen_width = screen_width


    @property
    def seeked(self):
        """Gets the seeked of this AnalyticsImpressionDetails.

        Milliseconds it took the player to seek

        :return: The seeked of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._seeked

    @seeked.setter
    def seeked(self, seeked):
        """Sets the seeked of this AnalyticsImpressionDetails.

        Milliseconds it took the player to seek

        :param seeked: The seeked of this AnalyticsImpressionDetails.
        :type: int
        """

        if seeked is not None:
            if not isinstance(seeked, int):
                raise TypeError("Invalid type for `seeked`, type has to be `int`")

            self._seeked = seeked


    @property
    def sequence_number(self):
        """Gets the sequence_number of this AnalyticsImpressionDetails.

        Sequence number of the sample in which it occured in the session

        :return: The sequence_number of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this AnalyticsImpressionDetails.

        Sequence number of the sample in which it occured in the session

        :param sequence_number: The sequence_number of this AnalyticsImpressionDetails.
        :type: int
        """

        if sequence_number is not None:
            if not isinstance(sequence_number, int):
                raise TypeError("Invalid type for `sequence_number`, type has to be `int`")

            self._sequence_number = sequence_number


    @property
    def size(self):
        """Gets the size of this AnalyticsImpressionDetails.

        Video size (FULLSCREEN or WINDOW)

        :return: The size of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this AnalyticsImpressionDetails.

        Video size (FULLSCREEN or WINDOW)

        :param size: The size of this AnalyticsImpressionDetails.
        :type: str
        """

        if size is not None:
            if not isinstance(size, str):
                raise TypeError("Invalid type for `size`, type has to be `str`")

            self._size = size


    @property
    def startup_time(self):
        """Gets the startup_time of this AnalyticsImpressionDetails.

        Combination of player- and videoStartuptime

        :return: The startup_time of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._startup_time

    @startup_time.setter
    def startup_time(self, startup_time):
        """Sets the startup_time of this AnalyticsImpressionDetails.

        Combination of player- and videoStartuptime

        :param startup_time: The startup_time of this AnalyticsImpressionDetails.
        :type: int
        """

        if startup_time is not None:
            if not isinstance(startup_time, int):
                raise TypeError("Invalid type for `startup_time`, type has to be `int`")

            self._startup_time = startup_time


    @property
    def state(self):
        """Gets the state of this AnalyticsImpressionDetails.

        Internal state of the analytics state machine

        :return: The state of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AnalyticsImpressionDetails.

        Internal state of the analytics state machine

        :param state: The state of this AnalyticsImpressionDetails.
        :type: str
        """

        if state is not None:
            if not isinstance(state, str):
                raise TypeError("Invalid type for `state`, type has to be `str`")

            self._state = state


    @property
    def stream_format(self):
        """Gets the stream_format of this AnalyticsImpressionDetails.

        Format of the stream (HLS, DASH, Progressive MP4)

        :return: The stream_format of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._stream_format

    @stream_format.setter
    def stream_format(self, stream_format):
        """Sets the stream_format of this AnalyticsImpressionDetails.

        Format of the stream (HLS, DASH, Progressive MP4)

        :param stream_format: The stream_format of this AnalyticsImpressionDetails.
        :type: str
        """

        if stream_format is not None:
            if not isinstance(stream_format, str):
                raise TypeError("Invalid type for `stream_format`, type has to be `str`")

            self._stream_format = stream_format


    @property
    def time(self):
        """Gets the time of this AnalyticsImpressionDetails.

        Current time in milliseconds

        :return: The time of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this AnalyticsImpressionDetails.

        Current time in milliseconds

        :param time: The time of this AnalyticsImpressionDetails.
        :type: int
        """

        if time is not None:
            if not isinstance(time, int):
                raise TypeError("Invalid type for `time`, type has to be `int`")

            self._time = time


    @property
    def user_id(self):
        """Gets the user_id of this AnalyticsImpressionDetails.

        ID that is persisted across sessions to identify a browser

        :return: The user_id of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AnalyticsImpressionDetails.

        ID that is persisted across sessions to identify a browser

        :param user_id: The user_id of this AnalyticsImpressionDetails.
        :type: str
        """

        if user_id is not None:
            if not isinstance(user_id, str):
                raise TypeError("Invalid type for `user_id`, type has to be `str`")

            self._user_id = user_id


    @property
    def video_bitrate(self):
        """Gets the video_bitrate of this AnalyticsImpressionDetails.

        Bitrate of the played back video rendition

        :return: The video_bitrate of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._video_bitrate

    @video_bitrate.setter
    def video_bitrate(self, video_bitrate):
        """Sets the video_bitrate of this AnalyticsImpressionDetails.

        Bitrate of the played back video rendition

        :param video_bitrate: The video_bitrate of this AnalyticsImpressionDetails.
        :type: int
        """

        if video_bitrate is not None:
            if not isinstance(video_bitrate, int):
                raise TypeError("Invalid type for `video_bitrate`, type has to be `int`")

            self._video_bitrate = video_bitrate


    @property
    def video_duration(self):
        """Gets the video_duration of this AnalyticsImpressionDetails.

        Length of the video in milliseconds

        :return: The video_duration of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._video_duration

    @video_duration.setter
    def video_duration(self, video_duration):
        """Sets the video_duration of this AnalyticsImpressionDetails.

        Length of the video in milliseconds

        :param video_duration: The video_duration of this AnalyticsImpressionDetails.
        :type: int
        """

        if video_duration is not None:
            if not isinstance(video_duration, int):
                raise TypeError("Invalid type for `video_duration`, type has to be `int`")

            self._video_duration = video_duration


    @property
    def video_id(self):
        """Gets the video_id of this AnalyticsImpressionDetails.

        ID of the video as configured via the analytics config

        :return: The video_id of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this AnalyticsImpressionDetails.

        ID of the video as configured via the analytics config

        :param video_id: The video_id of this AnalyticsImpressionDetails.
        :type: str
        """

        if video_id is not None:
            if not isinstance(video_id, str):
                raise TypeError("Invalid type for `video_id`, type has to be `str`")

            self._video_id = video_id


    @property
    def video_title(self):
        """Gets the video_title of this AnalyticsImpressionDetails.

        Free form human readable video title as configured in the analytics config

        :return: The video_title of this AnalyticsImpressionDetails.
        :rtype: str
        """
        return self._video_title

    @video_title.setter
    def video_title(self, video_title):
        """Sets the video_title of this AnalyticsImpressionDetails.

        Free form human readable video title as configured in the analytics config

        :param video_title: The video_title of this AnalyticsImpressionDetails.
        :type: str
        """

        if video_title is not None:
            if not isinstance(video_title, str):
                raise TypeError("Invalid type for `video_title`, type has to be `str`")

            self._video_title = video_title


    @property
    def video_playback_height(self):
        """Gets the video_playback_height of this AnalyticsImpressionDetails.

        Resolution of the played back Video Rendition

        :return: The video_playback_height of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._video_playback_height

    @video_playback_height.setter
    def video_playback_height(self, video_playback_height):
        """Sets the video_playback_height of this AnalyticsImpressionDetails.

        Resolution of the played back Video Rendition

        :param video_playback_height: The video_playback_height of this AnalyticsImpressionDetails.
        :type: int
        """

        if video_playback_height is not None:
            if not isinstance(video_playback_height, int):
                raise TypeError("Invalid type for `video_playback_height`, type has to be `int`")

            self._video_playback_height = video_playback_height


    @property
    def video_playback_width(self):
        """Gets the video_playback_width of this AnalyticsImpressionDetails.

        Resolution of the played back Video Rendition

        :return: The video_playback_width of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._video_playback_width

    @video_playback_width.setter
    def video_playback_width(self, video_playback_width):
        """Sets the video_playback_width of this AnalyticsImpressionDetails.

        Resolution of the played back Video Rendition

        :param video_playback_width: The video_playback_width of this AnalyticsImpressionDetails.
        :type: int
        """

        if video_playback_width is not None:
            if not isinstance(video_playback_width, int):
                raise TypeError("Invalid type for `video_playback_width`, type has to be `int`")

            self._video_playback_width = video_playback_width


    @property
    def video_startup_time(self):
        """Gets the video_startup_time of this AnalyticsImpressionDetails.

        Time in milliseconds it took to start video playback

        :return: The video_startup_time of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._video_startup_time

    @video_startup_time.setter
    def video_startup_time(self, video_startup_time):
        """Sets the video_startup_time of this AnalyticsImpressionDetails.

        Time in milliseconds it took to start video playback

        :param video_startup_time: The video_startup_time of this AnalyticsImpressionDetails.
        :type: int
        """

        if video_startup_time is not None:
            if not isinstance(video_startup_time, int):
                raise TypeError("Invalid type for `video_startup_time`, type has to be `int`")

            self._video_startup_time = video_startup_time


    @property
    def videotime_end(self):
        """Gets the videotime_end of this AnalyticsImpressionDetails.

        End time of the sample in the video (milliseconds)

        :return: The videotime_end of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._videotime_end

    @videotime_end.setter
    def videotime_end(self, videotime_end):
        """Sets the videotime_end of this AnalyticsImpressionDetails.

        End time of the sample in the video (milliseconds)

        :param videotime_end: The videotime_end of this AnalyticsImpressionDetails.
        :type: int
        """

        if videotime_end is not None:
            if not isinstance(videotime_end, int):
                raise TypeError("Invalid type for `videotime_end`, type has to be `int`")

            self._videotime_end = videotime_end


    @property
    def videotime_start(self):
        """Gets the videotime_start of this AnalyticsImpressionDetails.

        Start time of the sample in the video (milliseconds)

        :return: The videotime_start of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._videotime_start

    @videotime_start.setter
    def videotime_start(self, videotime_start):
        """Sets the videotime_start of this AnalyticsImpressionDetails.

        Start time of the sample in the video (milliseconds)

        :param videotime_start: The videotime_start of this AnalyticsImpressionDetails.
        :type: int
        """

        if videotime_start is not None:
            if not isinstance(videotime_start, int):
                raise TypeError("Invalid type for `videotime_start`, type has to be `int`")

            self._videotime_start = videotime_start


    @property
    def video_window_height(self):
        """Gets the video_window_height of this AnalyticsImpressionDetails.

        Height of the video player on the page

        :return: The video_window_height of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._video_window_height

    @video_window_height.setter
    def video_window_height(self, video_window_height):
        """Sets the video_window_height of this AnalyticsImpressionDetails.

        Height of the video player on the page

        :param video_window_height: The video_window_height of this AnalyticsImpressionDetails.
        :type: int
        """

        if video_window_height is not None:
            if not isinstance(video_window_height, int):
                raise TypeError("Invalid type for `video_window_height`, type has to be `int`")

            self._video_window_height = video_window_height


    @property
    def video_window_width(self):
        """Gets the video_window_width of this AnalyticsImpressionDetails.

        Width of the video player on the page

        :return: The video_window_width of this AnalyticsImpressionDetails.
        :rtype: int
        """
        return self._video_window_width

    @video_window_width.setter
    def video_window_width(self, video_window_width):
        """Sets the video_window_width of this AnalyticsImpressionDetails.

        Width of the video player on the page

        :param video_window_width: The video_window_width of this AnalyticsImpressionDetails.
        :type: int
        """

        if video_window_width is not None:
            if not isinstance(video_window_width, int):
                raise TypeError("Invalid type for `video_window_width`, type has to be `int`")

            self._video_window_width = video_window_width

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AnalyticsImpressionDetails, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(AnalyticsImpressionDetails, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalyticsImpressionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
