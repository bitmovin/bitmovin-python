# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class KubernetesClusterConfiguration(object):
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
            'parallel_encodings': 'int',
            'workers_per_encoding': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'parallel_encodings': 'parallelEncodings',
            'workers_per_encoding': 'workersPerEncoding'
        }
        return attributes

    def __init__(self, parallel_encodings=None, workers_per_encoding=None, *args, **kwargs):

        self._parallel_encodings = None
        self._workers_per_encoding = None
        self.discriminator = None

        self.parallel_encodings = parallel_encodings
        self.workers_per_encoding = workers_per_encoding

    @property
    def parallel_encodings(self):
        """Gets the parallel_encodings of this KubernetesClusterConfiguration.

        Number of parallel scheduled encodings on the Kubernetes cluster

        :return: The parallel_encodings of this KubernetesClusterConfiguration.
        :rtype: int
        """
        return self._parallel_encodings

    @parallel_encodings.setter
    def parallel_encodings(self, parallel_encodings):
        """Sets the parallel_encodings of this KubernetesClusterConfiguration.

        Number of parallel scheduled encodings on the Kubernetes cluster

        :param parallel_encodings: The parallel_encodings of this KubernetesClusterConfiguration.
        :type: int
        """

        if parallel_encodings is not None:
            if not isinstance(parallel_encodings, int):
                raise TypeError("Invalid type for `parallel_encodings`, type has to be `int`")

            self._parallel_encodings = parallel_encodings


    @property
    def workers_per_encoding(self):
        """Gets the workers_per_encoding of this KubernetesClusterConfiguration.

        Number of worker nodes used for each encoding on the Kubernetes cluster

        :return: The workers_per_encoding of this KubernetesClusterConfiguration.
        :rtype: int
        """
        return self._workers_per_encoding

    @workers_per_encoding.setter
    def workers_per_encoding(self, workers_per_encoding):
        """Sets the workers_per_encoding of this KubernetesClusterConfiguration.

        Number of worker nodes used for each encoding on the Kubernetes cluster

        :param workers_per_encoding: The workers_per_encoding of this KubernetesClusterConfiguration.
        :type: int
        """

        if workers_per_encoding is not None:
            if not isinstance(workers_per_encoding, int):
                raise TypeError("Invalid type for `workers_per_encoding`, type has to be `int`")

            self._workers_per_encoding = workers_per_encoding

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
            if issubclass(KubernetesClusterConfiguration, dict):
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
        if not isinstance(other, KubernetesClusterConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
