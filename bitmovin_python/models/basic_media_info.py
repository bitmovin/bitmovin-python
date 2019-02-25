# coding: utf-8

from bitmovin_python.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from enum import Enum


class BasicMediaInfo(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(BasicMediaInfo, self).openapi_types
        types.update({
            'group_id': 'str',
            'language': 'str',
            'assoc_language': 'str',
            'name': 'str',
            'is_default': 'bool',
            'autoselect': 'bool',
            'characteristics': 'list[str]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(BasicMediaInfo, self).attribute_map
        attributes.update({
            'group_id': 'groupId',
            'language': 'language',
            'assoc_language': 'assocLanguage',
            'name': 'name',
            'is_default': 'isDefault',
            'autoselect': 'autoselect',
            'characteristics': 'characteristics'
        })
        return attributes

    def __init__(self, group_id=None, language=None, assoc_language=None, name=None, is_default=None, autoselect=None, characteristics=None, *args, **kwargs):
        super(BasicMediaInfo, self).__init__(*args, **kwargs)

        self._group_id = None
        self._language = None
        self._assoc_language = None
        self._name = None
        self._is_default = None
        self._autoselect = None
        self._characteristics = None
        self.discriminator = None

        self.group_id = group_id
        if language is not None:
            self.language = language
        if assoc_language is not None:
            self.assoc_language = assoc_language
        self.name = name
        if is_default is not None:
            self.is_default = is_default
        if autoselect is not None:
            self.autoselect = autoselect
        if characteristics is not None:
            self.characteristics = characteristics

    @property
    def group_id(self):
        """Gets the group_id of this BasicMediaInfo.

        The value is a quoted-string which specifies the group to which the Rendition belongs.

        :return: The group_id of this BasicMediaInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this BasicMediaInfo.

        The value is a quoted-string which specifies the group to which the Rendition belongs.

        :param group_id: The group_id of this BasicMediaInfo.
        :type: str
        """

        if group_id is not None:
            if not isinstance(group_id, str):
                raise TypeError("Invalid type for `group_id`, type has to be `str`")

            self._group_id = group_id


    @property
    def language(self):
        """Gets the language of this BasicMediaInfo.

        Primary language in the rendition.

        :return: The language of this BasicMediaInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this BasicMediaInfo.

        Primary language in the rendition.

        :param language: The language of this BasicMediaInfo.
        :type: str
        """

        if language is not None:
            if not isinstance(language, str):
                raise TypeError("Invalid type for `language`, type has to be `str`")

            self._language = language


    @property
    def assoc_language(self):
        """Gets the assoc_language of this BasicMediaInfo.

        Identifies a language that is associated with the Rendition.

        :return: The assoc_language of this BasicMediaInfo.
        :rtype: str
        """
        return self._assoc_language

    @assoc_language.setter
    def assoc_language(self, assoc_language):
        """Sets the assoc_language of this BasicMediaInfo.

        Identifies a language that is associated with the Rendition.

        :param assoc_language: The assoc_language of this BasicMediaInfo.
        :type: str
        """

        if assoc_language is not None:
            if not isinstance(assoc_language, str):
                raise TypeError("Invalid type for `assoc_language`, type has to be `str`")

            self._assoc_language = assoc_language


    @property
    def name(self):
        """Gets the name of this BasicMediaInfo.

        Human readable description of the rendition.

        :return: The name of this BasicMediaInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasicMediaInfo.

        Human readable description of the rendition.

        :param name: The name of this BasicMediaInfo.
        :type: str
        """

        if name is not None:
            if not isinstance(name, str):
                raise TypeError("Invalid type for `name`, type has to be `str`")

            self._name = name


    @property
    def is_default(self):
        """Gets the is_default of this BasicMediaInfo.

        If set to true, the client SHOULD play this Rendition of the content in the absence of information from the user.

        :return: The is_default of this BasicMediaInfo.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this BasicMediaInfo.

        If set to true, the client SHOULD play this Rendition of the content in the absence of information from the user.

        :param is_default: The is_default of this BasicMediaInfo.
        :type: bool
        """

        if is_default is not None:
            if not isinstance(is_default, bool):
                raise TypeError("Invalid type for `is_default`, type has to be `bool`")

            self._is_default = is_default


    @property
    def autoselect(self):
        """Gets the autoselect of this BasicMediaInfo.

        If set to true, the client MAY choose to play this Rendition in the absence of explicit user preference.

        :return: The autoselect of this BasicMediaInfo.
        :rtype: bool
        """
        return self._autoselect

    @autoselect.setter
    def autoselect(self, autoselect):
        """Sets the autoselect of this BasicMediaInfo.

        If set to true, the client MAY choose to play this Rendition in the absence of explicit user preference.

        :param autoselect: The autoselect of this BasicMediaInfo.
        :type: bool
        """

        if autoselect is not None:
            if not isinstance(autoselect, bool):
                raise TypeError("Invalid type for `autoselect`, type has to be `bool`")

            self._autoselect = autoselect


    @property
    def characteristics(self):
        """Gets the characteristics of this BasicMediaInfo.

        Contains Uniform Type Identifiers

        :return: The characteristics of this BasicMediaInfo.
        :rtype: list[str]
        """
        return self._characteristics

    @characteristics.setter
    def characteristics(self, characteristics):
        """Sets the characteristics of this BasicMediaInfo.

        Contains Uniform Type Identifiers

        :param characteristics: The characteristics of this BasicMediaInfo.
        :type: list[str]
        """

        if characteristics is not None:
            if not isinstance(characteristics, list):
                raise TypeError("Invalid type for `characteristics`, type has to be `list[str]`")

            self._characteristics = characteristics

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(BasicMediaInfo, self).to_dict()

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
            if issubclass(BasicMediaInfo, dict):
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
        if not isinstance(other, BasicMediaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
