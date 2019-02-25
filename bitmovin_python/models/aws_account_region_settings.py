# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class AwsAccountRegionSettings(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AwsAccountRegionSettings, self).openapi_types
        types.update({
            'limit_parallel_encodings': 'int',
            'maximum_amount_of_coordinators_and_workers_in_region': 'int',
            'max_money_to_spend_per_month': 'float',
            'security_group_id': 'str',
            'subnet_id': 'str',
            'machine_types': 'list[str]',
            'ssh_port': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AwsAccountRegionSettings, self).attribute_map
        attributes.update({
            'limit_parallel_encodings': 'limitParallelEncodings',
            'maximum_amount_of_coordinators_and_workers_in_region': 'maximumAmountOfCoordinatorsAndWorkersInRegion',
            'max_money_to_spend_per_month': 'maxMoneyToSpendPerMonth',
            'security_group_id': 'securityGroupId',
            'subnet_id': 'subnetId',
            'machine_types': 'machineTypes',
            'ssh_port': 'sshPort'
        })
        return attributes

    def __init__(self, limit_parallel_encodings=None, maximum_amount_of_coordinators_and_workers_in_region=None, max_money_to_spend_per_month=None, security_group_id=None, subnet_id=None, machine_types=None, ssh_port=None, *args, **kwargs):
        super(AwsAccountRegionSettings, self).__init__(*args, **kwargs)

        self._limit_parallel_encodings = None
        self._maximum_amount_of_coordinators_and_workers_in_region = None
        self._max_money_to_spend_per_month = None
        self._security_group_id = None
        self._subnet_id = None
        self._machine_types = None
        self._ssh_port = None
        self.discriminator = None

        if limit_parallel_encodings is not None:
            self.limit_parallel_encodings = limit_parallel_encodings
        if maximum_amount_of_coordinators_and_workers_in_region is not None:
            self.maximum_amount_of_coordinators_and_workers_in_region = maximum_amount_of_coordinators_and_workers_in_region
        if max_money_to_spend_per_month is not None:
            self.max_money_to_spend_per_month = max_money_to_spend_per_month
        self.security_group_id = security_group_id
        self.subnet_id = subnet_id
        if machine_types is not None:
            self.machine_types = machine_types
        if ssh_port is not None:
            self.ssh_port = ssh_port

    @property
    def limit_parallel_encodings(self):
        """Gets the limit_parallel_encodings of this AwsAccountRegionSettings.

        Limit for the amount of running encodings at a time. Leave empty for no limit.

        :return: The limit_parallel_encodings of this AwsAccountRegionSettings.
        :rtype: int
        """
        return self._limit_parallel_encodings

    @limit_parallel_encodings.setter
    def limit_parallel_encodings(self, limit_parallel_encodings):
        """Sets the limit_parallel_encodings of this AwsAccountRegionSettings.

        Limit for the amount of running encodings at a time. Leave empty for no limit.

        :param limit_parallel_encodings: The limit_parallel_encodings of this AwsAccountRegionSettings.
        :type: int
        """

        if limit_parallel_encodings is not None:
            if not isinstance(limit_parallel_encodings, int):
                raise TypeError("Invalid type for `limit_parallel_encodings`, type has to be `int`")

            self._limit_parallel_encodings = limit_parallel_encodings


    @property
    def maximum_amount_of_coordinators_and_workers_in_region(self):
        """Gets the maximum_amount_of_coordinators_and_workers_in_region of this AwsAccountRegionSettings.

        Maximum amount of encoding coordinators and workers allowed in this region at any time. Leave empty for no limit.

        :return: The maximum_amount_of_coordinators_and_workers_in_region of this AwsAccountRegionSettings.
        :rtype: int
        """
        return self._maximum_amount_of_coordinators_and_workers_in_region

    @maximum_amount_of_coordinators_and_workers_in_region.setter
    def maximum_amount_of_coordinators_and_workers_in_region(self, maximum_amount_of_coordinators_and_workers_in_region):
        """Sets the maximum_amount_of_coordinators_and_workers_in_region of this AwsAccountRegionSettings.

        Maximum amount of encoding coordinators and workers allowed in this region at any time. Leave empty for no limit.

        :param maximum_amount_of_coordinators_and_workers_in_region: The maximum_amount_of_coordinators_and_workers_in_region of this AwsAccountRegionSettings.
        :type: int
        """

        if maximum_amount_of_coordinators_and_workers_in_region is not None:
            if not isinstance(maximum_amount_of_coordinators_and_workers_in_region, int):
                raise TypeError("Invalid type for `maximum_amount_of_coordinators_and_workers_in_region`, type has to be `int`")

            self._maximum_amount_of_coordinators_and_workers_in_region = maximum_amount_of_coordinators_and_workers_in_region


    @property
    def max_money_to_spend_per_month(self):
        """Gets the max_money_to_spend_per_month of this AwsAccountRegionSettings.

        Limit the amount of money to spend in this region on this account. Leave empty for no limit.

        :return: The max_money_to_spend_per_month of this AwsAccountRegionSettings.
        :rtype: float
        """
        return self._max_money_to_spend_per_month

    @max_money_to_spend_per_month.setter
    def max_money_to_spend_per_month(self, max_money_to_spend_per_month):
        """Sets the max_money_to_spend_per_month of this AwsAccountRegionSettings.

        Limit the amount of money to spend in this region on this account. Leave empty for no limit.

        :param max_money_to_spend_per_month: The max_money_to_spend_per_month of this AwsAccountRegionSettings.
        :type: float
        """

        if max_money_to_spend_per_month is not None:
            if not isinstance(max_money_to_spend_per_month, float):
                raise TypeError("Invalid type for `max_money_to_spend_per_month`, type has to be `float`")

            self._max_money_to_spend_per_month = max_money_to_spend_per_month


    @property
    def security_group_id(self):
        """Gets the security_group_id of this AwsAccountRegionSettings.

        Id of the security group for encoding instances

        :return: The security_group_id of this AwsAccountRegionSettings.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this AwsAccountRegionSettings.

        Id of the security group for encoding instances

        :param security_group_id: The security_group_id of this AwsAccountRegionSettings.
        :type: str
        """

        if security_group_id is not None:
            if not isinstance(security_group_id, str):
                raise TypeError("Invalid type for `security_group_id`, type has to be `str`")

            self._security_group_id = security_group_id


    @property
    def subnet_id(self):
        """Gets the subnet_id of this AwsAccountRegionSettings.

        Id of the subnet for encoding instances

        :return: The subnet_id of this AwsAccountRegionSettings.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this AwsAccountRegionSettings.

        Id of the subnet for encoding instances

        :param subnet_id: The subnet_id of this AwsAccountRegionSettings.
        :type: str
        """

        if subnet_id is not None:
            if not isinstance(subnet_id, str):
                raise TypeError("Invalid type for `subnet_id`, type has to be `str`")

            self._subnet_id = subnet_id


    @property
    def machine_types(self):
        """Gets the machine_types of this AwsAccountRegionSettings.

        Which machine types are allowed to be deployed. Leave empty for no machine type restrictions.

        :return: The machine_types of this AwsAccountRegionSettings.
        :rtype: list[str]
        """
        return self._machine_types

    @machine_types.setter
    def machine_types(self, machine_types):
        """Sets the machine_types of this AwsAccountRegionSettings.

        Which machine types are allowed to be deployed. Leave empty for no machine type restrictions.

        :param machine_types: The machine_types of this AwsAccountRegionSettings.
        :type: list[str]
        """

        if machine_types is not None:
            if not isinstance(machine_types, list):
                raise TypeError("Invalid type for `machine_types`, type has to be `list[str]`")

            self._machine_types = machine_types


    @property
    def ssh_port(self):
        """Gets the ssh_port of this AwsAccountRegionSettings.

        Custom SSH port. Valid values: 1 - 65535. Leave empty if the default SSH port 22 is OK.

        :return: The ssh_port of this AwsAccountRegionSettings.
        :rtype: int
        """
        return self._ssh_port

    @ssh_port.setter
    def ssh_port(self, ssh_port):
        """Sets the ssh_port of this AwsAccountRegionSettings.

        Custom SSH port. Valid values: 1 - 65535. Leave empty if the default SSH port 22 is OK.

        :param ssh_port: The ssh_port of this AwsAccountRegionSettings.
        :type: int
        """

        if ssh_port is not None:
            if ssh_port is not None and ssh_port > 65535:
                raise ValueError("Invalid value for `ssh_port`, must be a value less than or equal to `65535`")
            if ssh_port is not None and ssh_port < 1:
                raise ValueError("Invalid value for `ssh_port`, must be a value greater than or equal to `1`")
            if not isinstance(ssh_port, int):
                raise TypeError("Invalid type for `ssh_port`, type has to be `int`")

            self._ssh_port = ssh_port

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AwsAccountRegionSettings, self).to_dict()

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
            if issubclass(AwsAccountRegionSettings, dict):
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
        if not isinstance(other, AwsAccountRegionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
