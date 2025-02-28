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


class DashboardWidgetSettings(object):
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
        'display_type': 'str'
    }

    attribute_map = {
        'display_type': 'display_type'
    }

    def __init__(self, display_type=None, _configuration=None):  # noqa: E501
        """DashboardWidgetSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_type = None
        self.discriminator = None

        if display_type is not None:
            self.display_type = display_type

    @property
    def display_type(self):
        """Gets the display_type of this DashboardWidgetSettings.  # noqa: E501


        :return: The display_type of this DashboardWidgetSettings.  # noqa: E501
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        """Sets the display_type of this DashboardWidgetSettings.


        :param display_type: The display_type of this DashboardWidgetSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["table", "chart"]  # noqa: E501
        if (self._configuration.client_side_validation and
                display_type not in allowed_values):
            raise ValueError(
                "Invalid value for `display_type` ({0}), must be one of {1}"  # noqa: E501
                .format(display_type, allowed_values)
            )

        self._display_type = display_type

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
        if issubclass(DashboardWidgetSettings, dict):
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
        if not isinstance(other, DashboardWidgetSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardWidgetSettings):
            return True

        return self.to_dict() != other.to_dict()
