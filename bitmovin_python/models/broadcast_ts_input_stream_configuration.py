# coding: utf-8

from bitmovin_python.models.rai_unit import RaiUnit
import pprint
import six
from datetime import datetime
from enum import Enum


class BroadcastTsInputStreamConfiguration(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'stream_id': 'str',
            'packet_identifier': 'int',
            'start_with_discontinuity_indicator': 'bool',
            'align_pes': 'bool',
            'set_rai_on_au': 'RaiUnit'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_id': 'streamId',
            'packet_identifier': 'packetIdentifier',
            'start_with_discontinuity_indicator': 'startWithDiscontinuityIndicator',
            'align_pes': 'alignPes',
            'set_rai_on_au': 'setRaiOnAu'
        }
        return attributes

    def __init__(self, stream_id=None, packet_identifier=None, start_with_discontinuity_indicator=None, align_pes=None, set_rai_on_au=None, *args, **kwargs):

        self._stream_id = None
        self._packet_identifier = None
        self._start_with_discontinuity_indicator = None
        self._align_pes = None
        self._set_rai_on_au = None
        self.discriminator = None

        if stream_id is not None:
            self.stream_id = stream_id
        if packet_identifier is not None:
            self.packet_identifier = packet_identifier
        if start_with_discontinuity_indicator is not None:
            self.start_with_discontinuity_indicator = start_with_discontinuity_indicator
        if align_pes is not None:
            self.align_pes = align_pes
        if set_rai_on_au is not None:
            self.set_rai_on_au = set_rai_on_au

    @property
    def stream_id(self):
        """Gets the stream_id of this BroadcastTsInputStreamConfiguration.

        The UUID of the stream to which this configuration belongs to. This has to be a ID of a stream that has been added to the current muxing.

        :return: The stream_id of this BroadcastTsInputStreamConfiguration.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this BroadcastTsInputStreamConfiguration.

        The UUID of the stream to which this configuration belongs to. This has to be a ID of a stream that has been added to the current muxing.

        :param stream_id: The stream_id of this BroadcastTsInputStreamConfiguration.
        :type: str
        """

        if stream_id is not None:
            if not isinstance(stream_id, str):
                raise TypeError("Invalid type for `stream_id`, type has to be `str`")

            self._stream_id = stream_id


    @property
    def packet_identifier(self):
        """Gets the packet_identifier of this BroadcastTsInputStreamConfiguration.

        An integer value. Packet Identifier (PID) for this stream.

        :return: The packet_identifier of this BroadcastTsInputStreamConfiguration.
        :rtype: int
        """
        return self._packet_identifier

    @packet_identifier.setter
    def packet_identifier(self, packet_identifier):
        """Sets the packet_identifier of this BroadcastTsInputStreamConfiguration.

        An integer value. Packet Identifier (PID) for this stream.

        :param packet_identifier: The packet_identifier of this BroadcastTsInputStreamConfiguration.
        :type: int
        """

        if packet_identifier is not None:
            if packet_identifier is not None and packet_identifier > 8190:
                raise ValueError("Invalid value for `packet_identifier`, must be a value less than or equal to `8190`")
            if packet_identifier is not None and packet_identifier < 16:
                raise ValueError("Invalid value for `packet_identifier`, must be a value greater than or equal to `16`")
            if not isinstance(packet_identifier, int):
                raise TypeError("Invalid type for `packet_identifier`, type has to be `int`")

            self._packet_identifier = packet_identifier


    @property
    def start_with_discontinuity_indicator(self):
        """Gets the start_with_discontinuity_indicator of this BroadcastTsInputStreamConfiguration.

        Start stream with initial discontinuity indicator set to one. If true, set the discontinuity indicator in the first packet for this PID.

        :return: The start_with_discontinuity_indicator of this BroadcastTsInputStreamConfiguration.
        :rtype: bool
        """
        return self._start_with_discontinuity_indicator

    @start_with_discontinuity_indicator.setter
    def start_with_discontinuity_indicator(self, start_with_discontinuity_indicator):
        """Sets the start_with_discontinuity_indicator of this BroadcastTsInputStreamConfiguration.

        Start stream with initial discontinuity indicator set to one. If true, set the discontinuity indicator in the first packet for this PID.

        :param start_with_discontinuity_indicator: The start_with_discontinuity_indicator of this BroadcastTsInputStreamConfiguration.
        :type: bool
        """

        if start_with_discontinuity_indicator is not None:
            if not isinstance(start_with_discontinuity_indicator, bool):
                raise TypeError("Invalid type for `start_with_discontinuity_indicator`, type has to be `bool`")

            self._start_with_discontinuity_indicator = start_with_discontinuity_indicator


    @property
    def align_pes(self):
        """Gets the align_pes of this BroadcastTsInputStreamConfiguration.

        Align access units to PES packets. If true, align access units to PES packet headers. Uses adaptation field stuffing to position an access unit at the beginning of each PES packet.

        :return: The align_pes of this BroadcastTsInputStreamConfiguration.
        :rtype: bool
        """
        return self._align_pes

    @align_pes.setter
    def align_pes(self, align_pes):
        """Sets the align_pes of this BroadcastTsInputStreamConfiguration.

        Align access units to PES packets. If true, align access units to PES packet headers. Uses adaptation field stuffing to position an access unit at the beginning of each PES packet.

        :param align_pes: The align_pes of this BroadcastTsInputStreamConfiguration.
        :type: bool
        """

        if align_pes is not None:
            if not isinstance(align_pes, bool):
                raise TypeError("Invalid type for `align_pes`, type has to be `bool`")

            self._align_pes = align_pes


    @property
    def set_rai_on_au(self):
        """Gets the set_rai_on_au of this BroadcastTsInputStreamConfiguration.


        :return: The set_rai_on_au of this BroadcastTsInputStreamConfiguration.
        :rtype: RaiUnit
        """
        return self._set_rai_on_au

    @set_rai_on_au.setter
    def set_rai_on_au(self, set_rai_on_au):
        """Sets the set_rai_on_au of this BroadcastTsInputStreamConfiguration.


        :param set_rai_on_au: The set_rai_on_au of this BroadcastTsInputStreamConfiguration.
        :type: RaiUnit
        """

        if set_rai_on_au is not None:
            if not isinstance(set_rai_on_au, RaiUnit):
                raise TypeError("Invalid type for `set_rai_on_au`, type has to be `RaiUnit`")

            self._set_rai_on_au = set_rai_on_au

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
            if issubclass(BroadcastTsInputStreamConfiguration, dict):
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
        if not isinstance(other, BroadcastTsInputStreamConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
