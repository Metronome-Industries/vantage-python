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


class Integration(object):
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
        'token': 'str',
        'provider': 'str',
        'account_identifier': 'str',
        'status': 'str',
        'workspace_tokens': 'list[str]',
        'created_at': 'str'
    }

    attribute_map = {
        'token': 'token',
        'provider': 'provider',
        'account_identifier': 'account_identifier',
        'status': 'status',
        'workspace_tokens': 'workspace_tokens',
        'created_at': 'created_at'
    }

    def __init__(self, token=None, provider=None, account_identifier=None, status=None, workspace_tokens=None, created_at=None, _configuration=None):  # noqa: E501
        """Integration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._token = None
        self._provider = None
        self._account_identifier = None
        self._status = None
        self._workspace_tokens = None
        self._created_at = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if provider is not None:
            self.provider = provider
        if account_identifier is not None:
            self.account_identifier = account_identifier
        if status is not None:
            self.status = status
        if workspace_tokens is not None:
            self.workspace_tokens = workspace_tokens
        if created_at is not None:
            self.created_at = created_at

    @property
    def token(self):
        """Gets the token of this Integration.  # noqa: E501


        :return: The token of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Integration.


        :param token: The token of this Integration.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def provider(self):
        """Gets the provider of this Integration.  # noqa: E501

        The name of the Integration.  # noqa: E501

        :return: The provider of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Integration.

        The name of the Integration.  # noqa: E501

        :param provider: The provider of this Integration.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def account_identifier(self):
        """Gets the account_identifier of this Integration.  # noqa: E501

        The account identifier. For GCP this is the billing Account ID, for Azure this is the account ID  # noqa: E501

        :return: The account_identifier of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._account_identifier

    @account_identifier.setter
    def account_identifier(self, account_identifier):
        """Sets the account_identifier of this Integration.

        The account identifier. For GCP this is the billing Account ID, for Azure this is the account ID  # noqa: E501

        :param account_identifier: The account_identifier of this Integration.  # noqa: E501
        :type: str
        """

        self._account_identifier = account_identifier

    @property
    def status(self):
        """Gets the status of this Integration.  # noqa: E501

        The status of the Integration. Can be 'connected' or 'disconnected'.  # noqa: E501

        :return: The status of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Integration.

        The status of the Integration. Can be 'connected' or 'disconnected'.  # noqa: E501

        :param status: The status of this Integration.  # noqa: E501
        :type: str
        """
        allowed_values = ["connected", "disconnected"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def workspace_tokens(self):
        """Gets the workspace_tokens of this Integration.  # noqa: E501

        The tokens for any Workspaces that the account belongs to.  # noqa: E501

        :return: The workspace_tokens of this Integration.  # noqa: E501
        :rtype: list[str]
        """
        return self._workspace_tokens

    @workspace_tokens.setter
    def workspace_tokens(self, workspace_tokens):
        """Sets the workspace_tokens of this Integration.

        The tokens for any Workspaces that the account belongs to.  # noqa: E501

        :param workspace_tokens: The workspace_tokens of this Integration.  # noqa: E501
        :type: list[str]
        """

        self._workspace_tokens = workspace_tokens

    @property
    def created_at(self):
        """Gets the created_at of this Integration.  # noqa: E501

        The date and time, in UTC, the Integration was created. ISO 8601 Formatted.  # noqa: E501

        :return: The created_at of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Integration.

        The date and time, in UTC, the Integration was created. ISO 8601 Formatted.  # noqa: E501

        :param created_at: The created_at of this Integration.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

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
        if issubclass(Integration, dict):
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
        if not isinstance(other, Integration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Integration):
            return True

        return self.to_dict() != other.to_dict()
