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


class FinancialCommitments(object):
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
        'financial_commitments': 'list[FinancialCommitment]'
    }

    attribute_map = {
        'links': 'links',
        'financial_commitments': 'financial_commitments'
    }

    def __init__(self, links=None, financial_commitments=None, _configuration=None):  # noqa: E501
        """FinancialCommitments - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._financial_commitments = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if financial_commitments is not None:
            self.financial_commitments = financial_commitments

    @property
    def links(self):
        """Gets the links of this FinancialCommitments.  # noqa: E501


        :return: The links of this FinancialCommitments.  # noqa: E501
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FinancialCommitments.


        :param links: The links of this FinancialCommitments.  # noqa: E501
        :type: object
        """

        self._links = links

    @property
    def financial_commitments(self):
        """Gets the financial_commitments of this FinancialCommitments.  # noqa: E501


        :return: The financial_commitments of this FinancialCommitments.  # noqa: E501
        :rtype: list[FinancialCommitment]
        """
        return self._financial_commitments

    @financial_commitments.setter
    def financial_commitments(self, financial_commitments):
        """Sets the financial_commitments of this FinancialCommitments.


        :param financial_commitments: The financial_commitments of this FinancialCommitments.  # noqa: E501
        :type: list[FinancialCommitment]
        """

        self._financial_commitments = financial_commitments

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
        if issubclass(FinancialCommitments, dict):
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
        if not isinstance(other, FinancialCommitments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FinancialCommitments):
            return True

        return self.to_dict() != other.to_dict()
