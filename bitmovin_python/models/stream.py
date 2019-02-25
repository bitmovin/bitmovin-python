# coding: utf-8

from bitmovin_python.models.abstract_condition import AbstractCondition
from bitmovin_python.models.applied_stream_settings import AppliedStreamSettings
from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.decoding_error_mode import DecodingErrorMode
from bitmovin_python.models.encoding_output import EncodingOutput
from bitmovin_python.models.ignoring import Ignoring
from bitmovin_python.models.input_stream import InputStream
from bitmovin_python.models.stream_metadata import StreamMetadata
from bitmovin_python.models.stream_mode import StreamMode
from bitmovin_python.models.stream_per_title_settings import StreamPerTitleSettings
import pprint
import six
from datetime import datetime
from enum import Enum


class Stream(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Stream, self).openapi_types
        types.update({
            'input_streams': 'list[InputStream]',
            'outputs': 'list[EncodingOutput]',
            'create_quality_meta_data': 'bool',
            'codec_config_id': 'str',
            'segments_encoded': 'int',
            'conditions': 'AbstractCondition',
            'ignored_by': 'list[Ignoring]',
            'mode': 'StreamMode',
            'per_title_settings': 'StreamPerTitleSettings',
            'metadata': 'StreamMetadata',
            'decoding_error_mode': 'DecodingErrorMode',
            'applied_settings': 'AppliedStreamSettings'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Stream, self).attribute_map
        attributes.update({
            'input_streams': 'inputStreams',
            'outputs': 'outputs',
            'create_quality_meta_data': 'createQualityMetaData',
            'codec_config_id': 'codecConfigId',
            'segments_encoded': 'segmentsEncoded',
            'conditions': 'conditions',
            'ignored_by': 'ignoredBy',
            'mode': 'mode',
            'per_title_settings': 'perTitleSettings',
            'metadata': 'metadata',
            'decoding_error_mode': 'decodingErrorMode',
            'applied_settings': 'appliedSettings'
        })
        return attributes

    def __init__(self, input_streams=None, outputs=None, create_quality_meta_data=None, codec_config_id=None, segments_encoded=None, conditions=None, ignored_by=None, mode=None, per_title_settings=None, metadata=None, decoding_error_mode=None, applied_settings=None, *args, **kwargs):
        super(Stream, self).__init__(*args, **kwargs)

        self._input_streams = None
        self._outputs = None
        self._create_quality_meta_data = None
        self._codec_config_id = None
        self._segments_encoded = None
        self._conditions = None
        self._ignored_by = None
        self._mode = None
        self._per_title_settings = None
        self._metadata = None
        self._decoding_error_mode = None
        self._applied_settings = None
        self.discriminator = None

        self.input_streams = input_streams
        if outputs is not None:
            self.outputs = outputs
        if create_quality_meta_data is not None:
            self.create_quality_meta_data = create_quality_meta_data
        self.codec_config_id = codec_config_id
        if segments_encoded is not None:
            self.segments_encoded = segments_encoded
        if conditions is not None:
            self.conditions = conditions
        if ignored_by is not None:
            self.ignored_by = ignored_by
        if mode is not None:
            self.mode = mode
        if per_title_settings is not None:
            self.per_title_settings = per_title_settings
        if metadata is not None:
            self.metadata = metadata
        if decoding_error_mode is not None:
            self.decoding_error_mode = decoding_error_mode
        if applied_settings is not None:
            self.applied_settings = applied_settings

    @property
    def input_streams(self):
        """Gets the input_streams of this Stream.


        :return: The input_streams of this Stream.
        :rtype: list[InputStream]
        """
        return self._input_streams

    @input_streams.setter
    def input_streams(self, input_streams):
        """Sets the input_streams of this Stream.


        :param input_streams: The input_streams of this Stream.
        :type: list[InputStream]
        """

        if input_streams is not None:
            if not isinstance(input_streams, list):
                raise TypeError("Invalid type for `input_streams`, type has to be `list[InputStream]`")

            self._input_streams = input_streams


    @property
    def outputs(self):
        """Gets the outputs of this Stream.


        :return: The outputs of this Stream.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this Stream.


        :param outputs: The outputs of this Stream.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

            self._outputs = outputs


    @property
    def create_quality_meta_data(self):
        """Gets the create_quality_meta_data of this Stream.

        Set true to create quality metadata for this stream

        :return: The create_quality_meta_data of this Stream.
        :rtype: bool
        """
        return self._create_quality_meta_data

    @create_quality_meta_data.setter
    def create_quality_meta_data(self, create_quality_meta_data):
        """Sets the create_quality_meta_data of this Stream.

        Set true to create quality metadata for this stream

        :param create_quality_meta_data: The create_quality_meta_data of this Stream.
        :type: bool
        """

        if create_quality_meta_data is not None:
            if not isinstance(create_quality_meta_data, bool):
                raise TypeError("Invalid type for `create_quality_meta_data`, type has to be `bool`")

            self._create_quality_meta_data = create_quality_meta_data


    @property
    def codec_config_id(self):
        """Gets the codec_config_id of this Stream.

        Id of the codec configuration

        :return: The codec_config_id of this Stream.
        :rtype: str
        """
        return self._codec_config_id

    @codec_config_id.setter
    def codec_config_id(self, codec_config_id):
        """Sets the codec_config_id of this Stream.

        Id of the codec configuration

        :param codec_config_id: The codec_config_id of this Stream.
        :type: str
        """

        if codec_config_id is not None:
            if not isinstance(codec_config_id, str):
                raise TypeError("Invalid type for `codec_config_id`, type has to be `str`")

            self._codec_config_id = codec_config_id


    @property
    def segments_encoded(self):
        """Gets the segments_encoded of this Stream.

        Number of encoded segments. Available after encoding finishes.

        :return: The segments_encoded of this Stream.
        :rtype: int
        """
        return self._segments_encoded

    @segments_encoded.setter
    def segments_encoded(self, segments_encoded):
        """Sets the segments_encoded of this Stream.

        Number of encoded segments. Available after encoding finishes.

        :param segments_encoded: The segments_encoded of this Stream.
        :type: int
        """

        if segments_encoded is not None:
            if not isinstance(segments_encoded, int):
                raise TypeError("Invalid type for `segments_encoded`, type has to be `int`")

            self._segments_encoded = segments_encoded


    @property
    def conditions(self):
        """Gets the conditions of this Stream.

        Conditions to evaluate before creating the stream. If this evaluation fails, the stream won't be created. All muxings that depend on the stream will also not be created.

        :return: The conditions of this Stream.
        :rtype: AbstractCondition
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this Stream.

        Conditions to evaluate before creating the stream. If this evaluation fails, the stream won't be created. All muxings that depend on the stream will also not be created.

        :param conditions: The conditions of this Stream.
        :type: AbstractCondition
        """

        if conditions is not None:
            if not isinstance(conditions, AbstractCondition):
                raise TypeError("Invalid type for `conditions`, type has to be `AbstractCondition`")

            self._conditions = conditions


    @property
    def ignored_by(self):
        """Gets the ignored_by of this Stream.

        If this is set and contains objects, then this stream has been ignored during the encoding process

        :return: The ignored_by of this Stream.
        :rtype: list[Ignoring]
        """
        return self._ignored_by

    @ignored_by.setter
    def ignored_by(self, ignored_by):
        """Sets the ignored_by of this Stream.

        If this is set and contains objects, then this stream has been ignored during the encoding process

        :param ignored_by: The ignored_by of this Stream.
        :type: list[Ignoring]
        """

        if ignored_by is not None:
            if not isinstance(ignored_by, list):
                raise TypeError("Invalid type for `ignored_by`, type has to be `list[Ignoring]`")

            self._ignored_by = ignored_by


    @property
    def mode(self):
        """Gets the mode of this Stream.

        Mode of the stream

        :return: The mode of this Stream.
        :rtype: StreamMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Stream.

        Mode of the stream

        :param mode: The mode of this Stream.
        :type: StreamMode
        """

        if mode is not None:
            if not isinstance(mode, StreamMode):
                raise TypeError("Invalid type for `mode`, type has to be `StreamMode`")

            self._mode = mode


    @property
    def per_title_settings(self):
        """Gets the per_title_settings of this Stream.

        Settings to configure Per-Title on stream level

        :return: The per_title_settings of this Stream.
        :rtype: StreamPerTitleSettings
        """
        return self._per_title_settings

    @per_title_settings.setter
    def per_title_settings(self, per_title_settings):
        """Sets the per_title_settings of this Stream.

        Settings to configure Per-Title on stream level

        :param per_title_settings: The per_title_settings of this Stream.
        :type: StreamPerTitleSettings
        """

        if per_title_settings is not None:
            if not isinstance(per_title_settings, StreamPerTitleSettings):
                raise TypeError("Invalid type for `per_title_settings`, type has to be `StreamPerTitleSettings`")

            self._per_title_settings = per_title_settings


    @property
    def metadata(self):
        """Gets the metadata of this Stream.


        :return: The metadata of this Stream.
        :rtype: StreamMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Stream.


        :param metadata: The metadata of this Stream.
        :type: StreamMetadata
        """

        if metadata is not None:
            if not isinstance(metadata, StreamMetadata):
                raise TypeError("Invalid type for `metadata`, type has to be `StreamMetadata`")

            self._metadata = metadata


    @property
    def decoding_error_mode(self):
        """Gets the decoding_error_mode of this Stream.

        Determines how to react to errors during decoding

        :return: The decoding_error_mode of this Stream.
        :rtype: DecodingErrorMode
        """
        return self._decoding_error_mode

    @decoding_error_mode.setter
    def decoding_error_mode(self, decoding_error_mode):
        """Sets the decoding_error_mode of this Stream.

        Determines how to react to errors during decoding

        :param decoding_error_mode: The decoding_error_mode of this Stream.
        :type: DecodingErrorMode
        """

        if decoding_error_mode is not None:
            if not isinstance(decoding_error_mode, DecodingErrorMode):
                raise TypeError("Invalid type for `decoding_error_mode`, type has to be `DecodingErrorMode`")

            self._decoding_error_mode = decoding_error_mode


    @property
    def applied_settings(self):
        """Gets the applied_settings of this Stream.

        Contains stream properties which may not have been defined in the configuration

        :return: The applied_settings of this Stream.
        :rtype: AppliedStreamSettings
        """
        return self._applied_settings

    @applied_settings.setter
    def applied_settings(self, applied_settings):
        """Sets the applied_settings of this Stream.

        Contains stream properties which may not have been defined in the configuration

        :param applied_settings: The applied_settings of this Stream.
        :type: AppliedStreamSettings
        """

        if applied_settings is not None:
            if not isinstance(applied_settings, AppliedStreamSettings):
                raise TypeError("Invalid type for `applied_settings`, type has to be `AppliedStreamSettings`")

            self._applied_settings = applied_settings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Stream, self).to_dict()

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
            if issubclass(Stream, dict):
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
        if not isinstance(other, Stream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
