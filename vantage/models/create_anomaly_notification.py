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


class CreateAnomalyNotification(object):
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
        'cost_report_token': 'str',
        'threshold': 'int',
        'user_tokens': 'list[str]',
        'recipient_channels': 'list[str]'
    }

    attribute_map = {
        'cost_report_token': 'cost_report_token',
        'threshold': 'threshold',
        'user_tokens': 'user_tokens',
        'recipient_channels': 'recipient_channels'
    }

    def __init__(self, cost_report_token=None, threshold=None, user_tokens=None, recipient_channels=None, _configuration=None):  # noqa: E501
        """CreateAnomalyNotification - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cost_report_token = None
        self._threshold = None
        self._user_tokens = None
        self._recipient_channels = None
        self.discriminator = None

        self.cost_report_token = cost_report_token
        if threshold is not None:
            self.threshold = threshold
        if user_tokens is not None:
            self.user_tokens = user_tokens
        if recipient_channels is not None:
            self.recipient_channels = recipient_channels

    @property
    def cost_report_token(self):
        """Gets the cost_report_token of this CreateAnomalyNotification.  # noqa: E501

        The token of the Cost Report that has the notification.  # noqa: E501

        :return: The cost_report_token of this CreateAnomalyNotification.  # noqa: E501
        :rtype: str
        """
        return self._cost_report_token

    @cost_report_token.setter
    def cost_report_token(self, cost_report_token):
        """Sets the cost_report_token of this CreateAnomalyNotification.

        The token of the Cost Report that has the notification.  # noqa: E501

        :param cost_report_token: The cost_report_token of this CreateAnomalyNotification.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cost_report_token is None:
            raise ValueError("Invalid value for `cost_report_token`, must not be `None`")  # noqa: E501

        self._cost_report_token = cost_report_token

    @property
    def threshold(self):
        """Gets the threshold of this CreateAnomalyNotification.  # noqa: E501

        The threshold amount that must be met for the notification to fire.  # noqa: E501

        :return: The threshold of this CreateAnomalyNotification.  # noqa: E501
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this CreateAnomalyNotification.

        The threshold amount that must be met for the notification to fire.  # noqa: E501

        :param threshold: The threshold of this CreateAnomalyNotification.  # noqa: E501
        :type: int
        """

        self._threshold = threshold

    @property
    def user_tokens(self):
        """Gets the user_tokens of this CreateAnomalyNotification.  # noqa: E501

        The tokens of the Users that receive the notification.  # noqa: E501

        :return: The user_tokens of this CreateAnomalyNotification.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_tokens

    @user_tokens.setter
    def user_tokens(self, user_tokens):
        """Sets the user_tokens of this CreateAnomalyNotification.

        The tokens of the Users that receive the notification.  # noqa: E501

        :param user_tokens: The user_tokens of this CreateAnomalyNotification.  # noqa: E501
        :type: list[str]
        """

        self._user_tokens = user_tokens

    @property
    def recipient_channels(self):
        """Gets the recipient_channels of this CreateAnomalyNotification.  # noqa: E501

        The Slack/MS Teams channels that receive the notification.  # noqa: E501

        :return: The recipient_channels of this CreateAnomalyNotification.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipient_channels

    @recipient_channels.setter
    def recipient_channels(self, recipient_channels):
        """Sets the recipient_channels of this CreateAnomalyNotification.

        The Slack/MS Teams channels that receive the notification.  # noqa: E501

        :param recipient_channels: The recipient_channels of this CreateAnomalyNotification.  # noqa: E501
        :type: list[str]
        """

        self._recipient_channels = recipient_channels

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
        if issubclass(CreateAnomalyNotification, dict):
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
        if not isinstance(other, CreateAnomalyNotification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAnomalyNotification):
            return True

        return self.to_dict() != other.to_dict()
