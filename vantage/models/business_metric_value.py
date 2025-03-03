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


class BusinessMetricValue(object):
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
        '_date': 'str',
        'amount': 'str',
        'label': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'amount': 'amount',
        'label': 'label'
    }

    def __init__(self, _date=None, amount=None, label=None, _configuration=None):  # noqa: E501
        """BusinessMetricValue - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__date = None
        self._amount = None
        self._label = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if amount is not None:
            self.amount = amount
        if label is not None:
            self.label = label

    @property
    def _date(self):
        """Gets the _date of this BusinessMetricValue.  # noqa: E501

        The date of the Business Metric Value. ISO 8601 formatted.  # noqa: E501

        :return: The _date of this BusinessMetricValue.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this BusinessMetricValue.

        The date of the Business Metric Value. ISO 8601 formatted.  # noqa: E501

        :param _date: The _date of this BusinessMetricValue.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def amount(self):
        """Gets the amount of this BusinessMetricValue.  # noqa: E501

        The amount of the Business Metric Value as a string to ensure precision.  # noqa: E501

        :return: The amount of this BusinessMetricValue.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BusinessMetricValue.

        The amount of the Business Metric Value as a string to ensure precision.  # noqa: E501

        :param amount: The amount of this BusinessMetricValue.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def label(self):
        """Gets the label of this BusinessMetricValue.  # noqa: E501

        The label of the Business Metric Value.  # noqa: E501

        :return: The label of this BusinessMetricValue.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this BusinessMetricValue.

        The label of the Business Metric Value.  # noqa: E501

        :param label: The label of this BusinessMetricValue.  # noqa: E501
        :type: str
        """

        self._label = label

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
        if issubclass(BusinessMetricValue, dict):
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
        if not isinstance(other, BusinessMetricValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BusinessMetricValue):
            return True

        return self.to_dict() != other.to_dict()
