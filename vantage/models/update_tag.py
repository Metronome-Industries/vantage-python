# coding: utf-8

"""
    Vantage

    Vantage API  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@vantage.sh
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from vantage.configuration import Configuration


class UpdateTag(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tag_key': 'str',
        'tag_keys': 'list[str]',
        'hidden': 'bool'
    }

    attribute_map = {
        'tag_key': 'tag_key',
        'tag_keys': 'tag_keys',
        'hidden': 'hidden'
    }

    def __init__(self, tag_key=None, tag_keys=None, hidden=None, _configuration=None):  # noqa: E501
        """UpdateTag - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._tag_key = None
        self._tag_keys = None
        self._hidden = None
        self.discriminator = None

        if tag_key is not None:
            self.tag_key = tag_key
        if tag_keys is not None:
            self.tag_keys = tag_keys
        self.hidden = hidden

    @property
    def tag_key(self):
        """Gets the tag_key of this UpdateTag.  # noqa: E501


        :return: The tag_key of this UpdateTag.  # noqa: E501
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        """Sets the tag_key of this UpdateTag.


        :param tag_key: The tag_key of this UpdateTag.  # noqa: E501
        :type: str
        """

        self._tag_key = tag_key

    @property
    def tag_keys(self):
        """Gets the tag_keys of this UpdateTag.  # noqa: E501


        :return: The tag_keys of this UpdateTag.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_keys

    @tag_keys.setter
    def tag_keys(self, tag_keys):
        """Sets the tag_keys of this UpdateTag.


        :param tag_keys: The tag_keys of this UpdateTag.  # noqa: E501
        :type: list[str]
        """

        self._tag_keys = tag_keys

    @property
    def hidden(self):
        """Gets the hidden of this UpdateTag.  # noqa: E501

        Whether the Tag is hidden from the Vantage UI.  # noqa: E501

        :return: The hidden of this UpdateTag.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this UpdateTag.

        Whether the Tag is hidden from the Vantage UI.  # noqa: E501

        :param hidden: The hidden of this UpdateTag.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and hidden is None:
            raise ValueError("Invalid value for `hidden`, must not be `None`")  # noqa: E501

        self._hidden = hidden

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateTag, dict):
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
        if not isinstance(other, UpdateTag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTag):
            return True

        return self.to_dict() != other.to_dict()
