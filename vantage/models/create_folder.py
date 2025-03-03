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


class CreateFolder(object):
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
        'title': 'str',
        'parent_folder_token': 'str',
        'saved_filter_tokens': 'list[str]',
        'workspace_token': 'str'
    }

    attribute_map = {
        'title': 'title',
        'parent_folder_token': 'parent_folder_token',
        'saved_filter_tokens': 'saved_filter_tokens',
        'workspace_token': 'workspace_token'
    }

    def __init__(self, title=None, parent_folder_token=None, saved_filter_tokens=None, workspace_token=None, _configuration=None):  # noqa: E501
        """CreateFolder - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._title = None
        self._parent_folder_token = None
        self._saved_filter_tokens = None
        self._workspace_token = None
        self.discriminator = None

        self.title = title
        if parent_folder_token is not None:
            self.parent_folder_token = parent_folder_token
        if saved_filter_tokens is not None:
            self.saved_filter_tokens = saved_filter_tokens
        if workspace_token is not None:
            self.workspace_token = workspace_token

    @property
    def title(self):
        """Gets the title of this CreateFolder.  # noqa: E501

        The title of the Folder.  # noqa: E501

        :return: The title of this CreateFolder.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateFolder.

        The title of the Folder.  # noqa: E501

        :param title: The title of this CreateFolder.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def parent_folder_token(self):
        """Gets the parent_folder_token of this CreateFolder.  # noqa: E501

        The token of the parent Folder.  # noqa: E501

        :return: The parent_folder_token of this CreateFolder.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_token

    @parent_folder_token.setter
    def parent_folder_token(self, parent_folder_token):
        """Sets the parent_folder_token of this CreateFolder.

        The token of the parent Folder.  # noqa: E501

        :param parent_folder_token: The parent_folder_token of this CreateFolder.  # noqa: E501
        :type: str
        """

        self._parent_folder_token = parent_folder_token

    @property
    def saved_filter_tokens(self):
        """Gets the saved_filter_tokens of this CreateFolder.  # noqa: E501

        The tokens of the SavedFilters to apply to any Cost Report contained within the Folder.  # noqa: E501

        :return: The saved_filter_tokens of this CreateFolder.  # noqa: E501
        :rtype: list[str]
        """
        return self._saved_filter_tokens

    @saved_filter_tokens.setter
    def saved_filter_tokens(self, saved_filter_tokens):
        """Sets the saved_filter_tokens of this CreateFolder.

        The tokens of the SavedFilters to apply to any Cost Report contained within the Folder.  # noqa: E501

        :param saved_filter_tokens: The saved_filter_tokens of this CreateFolder.  # noqa: E501
        :type: list[str]
        """

        self._saved_filter_tokens = saved_filter_tokens

    @property
    def workspace_token(self):
        """Gets the workspace_token of this CreateFolder.  # noqa: E501

        The token of the Workspace to add the Folder to. Ignored if 'parent_folder_token' is set. Required if the API token is associated with multiple Workspaces.  # noqa: E501

        :return: The workspace_token of this CreateFolder.  # noqa: E501
        :rtype: str
        """
        return self._workspace_token

    @workspace_token.setter
    def workspace_token(self, workspace_token):
        """Sets the workspace_token of this CreateFolder.

        The token of the Workspace to add the Folder to. Ignored if 'parent_folder_token' is set. Required if the API token is associated with multiple Workspaces.  # noqa: E501

        :param workspace_token: The workspace_token of this CreateFolder.  # noqa: E501
        :type: str
        """

        self._workspace_token = workspace_token

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
        if issubclass(CreateFolder, dict):
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
        if not isinstance(other, CreateFolder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateFolder):
            return True

        return self.to_dict() != other.to_dict()
