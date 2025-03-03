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


class Workspaces(object):
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
        'links': 'object',
        'workspaces': 'list[Workspace]'
    }

    attribute_map = {
        'links': 'links',
        'workspaces': 'workspaces'
    }

    def __init__(self, links=None, workspaces=None, _configuration=None):  # noqa: E501
        """Workspaces - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._workspaces = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def links(self):
        """Gets the links of this Workspaces.  # noqa: E501


        :return: The links of this Workspaces.  # noqa: E501
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Workspaces.


        :param links: The links of this Workspaces.  # noqa: E501
        :type: object
        """

        self._links = links

    @property
    def workspaces(self):
        """Gets the workspaces of this Workspaces.  # noqa: E501


        :return: The workspaces of this Workspaces.  # noqa: E501
        :rtype: list[Workspace]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this Workspaces.


        :param workspaces: The workspaces of this Workspaces.  # noqa: E501
        :type: list[Workspace]
        """

        self._workspaces = workspaces

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
        if issubclass(Workspaces, dict):
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
        if not isinstance(other, Workspaces):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Workspaces):
            return True

        return self.to_dict() != other.to_dict()
