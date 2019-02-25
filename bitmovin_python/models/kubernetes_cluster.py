# coding: utf-8

from bitmovin_python.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from enum import Enum


class KubernetesCluster(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(KubernetesCluster, self).openapi_types
        types.update({
            'online': 'bool',
            'connected': 'bool',
            'agent_deployment_download_url': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(KubernetesCluster, self).attribute_map
        attributes.update({
            'online': 'online',
            'connected': 'connected',
            'agent_deployment_download_url': 'agentDeploymentDownloadUrl'
        })
        return attributes

    def __init__(self, online=None, connected=None, agent_deployment_download_url=None, *args, **kwargs):
        super(KubernetesCluster, self).__init__(*args, **kwargs)

        self._online = None
        self._connected = None
        self._agent_deployment_download_url = None
        self.discriminator = None

        self.online = online
        self.connected = connected
        self.agent_deployment_download_url = agent_deployment_download_url

    @property
    def online(self):
        """Gets the online of this KubernetesCluster.

        Shows if the Bitmovin Agent is alive

        :return: The online of this KubernetesCluster.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this KubernetesCluster.

        Shows if the Bitmovin Agent is alive

        :param online: The online of this KubernetesCluster.
        :type: bool
        """

        if online is not None:
            if not isinstance(online, bool):
                raise TypeError("Invalid type for `online`, type has to be `bool`")

            self._online = online


    @property
    def connected(self):
        """Gets the connected of this KubernetesCluster.

        Shows if the Kubernetes cluster is accessible by the Bitmovin Agent

        :return: The connected of this KubernetesCluster.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this KubernetesCluster.

        Shows if the Kubernetes cluster is accessible by the Bitmovin Agent

        :param connected: The connected of this KubernetesCluster.
        :type: bool
        """

        if connected is not None:
            if not isinstance(connected, bool):
                raise TypeError("Invalid type for `connected`, type has to be `bool`")

            self._connected = connected


    @property
    def agent_deployment_download_url(self):
        """Gets the agent_deployment_download_url of this KubernetesCluster.


        :return: The agent_deployment_download_url of this KubernetesCluster.
        :rtype: str
        """
        return self._agent_deployment_download_url

    @agent_deployment_download_url.setter
    def agent_deployment_download_url(self, agent_deployment_download_url):
        """Sets the agent_deployment_download_url of this KubernetesCluster.


        :param agent_deployment_download_url: The agent_deployment_download_url of this KubernetesCluster.
        :type: str
        """

        if agent_deployment_download_url is not None:
            if not isinstance(agent_deployment_download_url, str):
                raise TypeError("Invalid type for `agent_deployment_download_url`, type has to be `str`")

            self._agent_deployment_download_url = agent_deployment_download_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(KubernetesCluster, self).to_dict()

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
            if issubclass(KubernetesCluster, dict):
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
        if not isinstance(other, KubernetesCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
