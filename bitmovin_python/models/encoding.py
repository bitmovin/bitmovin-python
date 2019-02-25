# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
from bitmovin_python.models.cloud_region import CloudRegion
from bitmovin_python.models.infrastructure_settings import InfrastructureSettings
import pprint
import six
from datetime import datetime
from enum import Enum


class Encoding(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Encoding, self).openapi_types
        types.update({
            'cloud_region': 'CloudRegion',
            'encoder_version': 'str',
            'infrastructure_id': 'str',
            'infrastructure': 'InfrastructureSettings',
            'labels': 'list[str]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Encoding, self).attribute_map
        attributes.update({
            'cloud_region': 'cloudRegion',
            'encoder_version': 'encoderVersion',
            'infrastructure_id': 'infrastructureId',
            'infrastructure': 'infrastructure',
            'labels': 'labels'
        })
        return attributes

    def __init__(self, cloud_region=None, encoder_version=None, infrastructure_id=None, infrastructure=None, labels=None, *args, **kwargs):
        super(Encoding, self).__init__(*args, **kwargs)

        self._cloud_region = None
        self._encoder_version = None
        self._infrastructure_id = None
        self._infrastructure = None
        self._labels = None
        self.discriminator = None

        if cloud_region is not None:
            self.cloud_region = cloud_region
        if encoder_version is not None:
            self.encoder_version = encoder_version
        if infrastructure_id is not None:
            self.infrastructure_id = infrastructure_id
        if infrastructure is not None:
            self.infrastructure = infrastructure
        if labels is not None:
            self.labels = labels

    @property
    def cloud_region(self):
        """Gets the cloud_region of this Encoding.


        :return: The cloud_region of this Encoding.
        :rtype: CloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        """Sets the cloud_region of this Encoding.


        :param cloud_region: The cloud_region of this Encoding.
        :type: CloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, CloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `CloudRegion`")

            self._cloud_region = cloud_region


    @property
    def encoder_version(self):
        """Gets the encoder_version of this Encoding.

        Version of the encoder

        :return: The encoder_version of this Encoding.
        :rtype: str
        """
        return self._encoder_version

    @encoder_version.setter
    def encoder_version(self, encoder_version):
        """Sets the encoder_version of this Encoding.

        Version of the encoder

        :param encoder_version: The encoder_version of this Encoding.
        :type: str
        """

        if encoder_version is not None:
            if not isinstance(encoder_version, str):
                raise TypeError("Invalid type for `encoder_version`, type has to be `str`")

            self._encoder_version = encoder_version


    @property
    def infrastructure_id(self):
        """Gets the infrastructure_id of this Encoding.

        Define an external infrastructure to run the encoding on. Note If you set this value, the `cloudRegion` must be 'EXTERNAL'.

        :return: The infrastructure_id of this Encoding.
        :rtype: str
        """
        return self._infrastructure_id

    @infrastructure_id.setter
    def infrastructure_id(self, infrastructure_id):
        """Sets the infrastructure_id of this Encoding.

        Define an external infrastructure to run the encoding on. Note If you set this value, the `cloudRegion` must be 'EXTERNAL'.

        :param infrastructure_id: The infrastructure_id of this Encoding.
        :type: str
        """

        if infrastructure_id is not None:
            if not isinstance(infrastructure_id, str):
                raise TypeError("Invalid type for `infrastructure_id`, type has to be `str`")

            self._infrastructure_id = infrastructure_id


    @property
    def infrastructure(self):
        """Gets the infrastructure of this Encoding.


        :return: The infrastructure of this Encoding.
        :rtype: InfrastructureSettings
        """
        return self._infrastructure

    @infrastructure.setter
    def infrastructure(self, infrastructure):
        """Sets the infrastructure of this Encoding.


        :param infrastructure: The infrastructure of this Encoding.
        :type: InfrastructureSettings
        """

        if infrastructure is not None:
            if not isinstance(infrastructure, InfrastructureSettings):
                raise TypeError("Invalid type for `infrastructure`, type has to be `InfrastructureSettings`")

            self._infrastructure = infrastructure


    @property
    def labels(self):
        """Gets the labels of this Encoding.

        You may pass a list of groups associated with this encoding. This will enable you to group results in the statistics resource

        :return: The labels of this Encoding.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Encoding.

        You may pass a list of groups associated with this encoding. This will enable you to group results in the statistics resource

        :param labels: The labels of this Encoding.
        :type: list[str]
        """

        if labels is not None:
            if not isinstance(labels, list):
                raise TypeError("Invalid type for `labels`, type has to be `list[str]`")

            self._labels = labels

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Encoding, self).to_dict()

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
            if issubclass(Encoding, dict):
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
        if not isinstance(other, Encoding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
