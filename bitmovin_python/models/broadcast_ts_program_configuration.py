# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class BroadcastTsProgramConfiguration(object):
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
            'program_number': 'int',
            'pid_for_pmt': 'int',
            'insert_program_clock_ref_on_pes': 'bool'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'program_number': 'programNumber',
            'pid_for_pmt': 'pidForPMT',
            'insert_program_clock_ref_on_pes': 'insertProgramClockRefOnPes'
        }
        return attributes

    def __init__(self, program_number=None, pid_for_pmt=None, insert_program_clock_ref_on_pes=None, *args, **kwargs):

        self._program_number = None
        self._pid_for_pmt = None
        self._insert_program_clock_ref_on_pes = None
        self.discriminator = None

        if program_number is not None:
            self.program_number = program_number
        if pid_for_pmt is not None:
            self.pid_for_pmt = pid_for_pmt
        if insert_program_clock_ref_on_pes is not None:
            self.insert_program_clock_ref_on_pes = insert_program_clock_ref_on_pes

    @property
    def program_number(self):
        """Gets the program_number of this BroadcastTsProgramConfiguration.

        An integer value. Value for program_number field in Program Map Table (PMT). The value zero is reserved for the NIT PID entry in the PAT.

        :return: The program_number of this BroadcastTsProgramConfiguration.
        :rtype: int
        """
        return self._program_number

    @program_number.setter
    def program_number(self, program_number):
        """Sets the program_number of this BroadcastTsProgramConfiguration.

        An integer value. Value for program_number field in Program Map Table (PMT). The value zero is reserved for the NIT PID entry in the PAT.

        :param program_number: The program_number of this BroadcastTsProgramConfiguration.
        :type: int
        """

        if program_number is not None:
            if program_number is not None and program_number > 65535:
                raise ValueError("Invalid value for `program_number`, must be a value less than or equal to `65535`")
            if program_number is not None and program_number < 1:
                raise ValueError("Invalid value for `program_number`, must be a value greater than or equal to `1`")
            if not isinstance(program_number, int):
                raise TypeError("Invalid type for `program_number`, type has to be `int`")

            self._program_number = program_number


    @property
    def pid_for_pmt(self):
        """Gets the pid_for_pmt of this BroadcastTsProgramConfiguration.

        An integer value. Packet identifier (PID) to use for Program Map Table (PMT). Recommended value is 2 x programNumber.

        :return: The pid_for_pmt of this BroadcastTsProgramConfiguration.
        :rtype: int
        """
        return self._pid_for_pmt

    @pid_for_pmt.setter
    def pid_for_pmt(self, pid_for_pmt):
        """Sets the pid_for_pmt of this BroadcastTsProgramConfiguration.

        An integer value. Packet identifier (PID) to use for Program Map Table (PMT). Recommended value is 2 x programNumber.

        :param pid_for_pmt: The pid_for_pmt of this BroadcastTsProgramConfiguration.
        :type: int
        """

        if pid_for_pmt is not None:
            if pid_for_pmt is not None and pid_for_pmt > 8190:
                raise ValueError("Invalid value for `pid_for_pmt`, must be a value less than or equal to `8190`")
            if pid_for_pmt is not None and pid_for_pmt < 10:
                raise ValueError("Invalid value for `pid_for_pmt`, must be a value greater than or equal to `10`")
            if not isinstance(pid_for_pmt, int):
                raise TypeError("Invalid type for `pid_for_pmt`, type has to be `int`")

            self._pid_for_pmt = pid_for_pmt


    @property
    def insert_program_clock_ref_on_pes(self):
        """Gets the insert_program_clock_ref_on_pes of this BroadcastTsProgramConfiguration.

        Insert Program Clock References (PCRs) on all packetized elemementary stream packets. When false, indicates that PCRs should be inserted on every PES header. This parameter is effective only when the PCR packet identifier is the same as a video or audio elementary stream.

        :return: The insert_program_clock_ref_on_pes of this BroadcastTsProgramConfiguration.
        :rtype: bool
        """
        return self._insert_program_clock_ref_on_pes

    @insert_program_clock_ref_on_pes.setter
    def insert_program_clock_ref_on_pes(self, insert_program_clock_ref_on_pes):
        """Sets the insert_program_clock_ref_on_pes of this BroadcastTsProgramConfiguration.

        Insert Program Clock References (PCRs) on all packetized elemementary stream packets. When false, indicates that PCRs should be inserted on every PES header. This parameter is effective only when the PCR packet identifier is the same as a video or audio elementary stream.

        :param insert_program_clock_ref_on_pes: The insert_program_clock_ref_on_pes of this BroadcastTsProgramConfiguration.
        :type: bool
        """

        if insert_program_clock_ref_on_pes is not None:
            if not isinstance(insert_program_clock_ref_on_pes, bool):
                raise TypeError("Invalid type for `insert_program_clock_ref_on_pes`, type has to be `bool`")

            self._insert_program_clock_ref_on_pes = insert_program_clock_ref_on_pes

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
            if issubclass(BroadcastTsProgramConfiguration, dict):
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
        if not isinstance(other, BroadcastTsProgramConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
