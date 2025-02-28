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


class Segment(object):
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
        'title': 'str',
        'parent_segment_token': 'str',
        'description': 'str',
        'track_unallocated': 'bool',
        'report_settings': 'SegmentReportSettings',
        'priority': 'int',
        'filter': 'str',
        'created_at': 'str',
        'workspace_token': 'str',
        'report_token': 'str'
    }

    attribute_map = {
        'token': 'token',
        'title': 'title',
        'parent_segment_token': 'parent_segment_token',
        'description': 'description',
        'track_unallocated': 'track_unallocated',
        'report_settings': 'report_settings',
        'priority': 'priority',
        'filter': 'filter',
        'created_at': 'created_at',
        'workspace_token': 'workspace_token',
        'report_token': 'report_token'
    }

    def __init__(self, token=None, title=None, parent_segment_token=None, description=None, track_unallocated=None, report_settings=None, priority=None, filter=None, created_at=None, workspace_token=None, report_token=None, _configuration=None):  # noqa: E501
        """Segment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._token = None
        self._title = None
        self._parent_segment_token = None
        self._description = None
        self._track_unallocated = None
        self._report_settings = None
        self._priority = None
        self._filter = None
        self._created_at = None
        self._workspace_token = None
        self._report_token = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if title is not None:
            self.title = title
        if parent_segment_token is not None:
            self.parent_segment_token = parent_segment_token
        if description is not None:
            self.description = description
        if track_unallocated is not None:
            self.track_unallocated = track_unallocated
        if report_settings is not None:
            self.report_settings = report_settings
        if priority is not None:
            self.priority = priority
        if filter is not None:
            self.filter = filter
        if created_at is not None:
            self.created_at = created_at
        if workspace_token is not None:
            self.workspace_token = workspace_token
        if report_token is not None:
            self.report_token = report_token

    @property
    def token(self):
        """Gets the token of this Segment.  # noqa: E501


        :return: The token of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Segment.


        :param token: The token of this Segment.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def title(self):
        """Gets the title of this Segment.  # noqa: E501

        The title of the Segment.  # noqa: E501

        :return: The title of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Segment.

        The title of the Segment.  # noqa: E501

        :param title: The title of this Segment.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def parent_segment_token(self):
        """Gets the parent_segment_token of this Segment.  # noqa: E501

        The token of the parent Segment of this Segment.  # noqa: E501

        :return: The parent_segment_token of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._parent_segment_token

    @parent_segment_token.setter
    def parent_segment_token(self, parent_segment_token):
        """Sets the parent_segment_token of this Segment.

        The token of the parent Segment of this Segment.  # noqa: E501

        :param parent_segment_token: The parent_segment_token of this Segment.  # noqa: E501
        :type: str
        """

        self._parent_segment_token = parent_segment_token

    @property
    def description(self):
        """Gets the description of this Segment.  # noqa: E501

        The description of the Segment.  # noqa: E501

        :return: The description of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Segment.

        The description of the Segment.  # noqa: E501

        :param description: The description of this Segment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def track_unallocated(self):
        """Gets the track_unallocated of this Segment.  # noqa: E501

        Track Unallocated Costs which are not assigned to any of the created Segments.  # noqa: E501

        :return: The track_unallocated of this Segment.  # noqa: E501
        :rtype: bool
        """
        return self._track_unallocated

    @track_unallocated.setter
    def track_unallocated(self, track_unallocated):
        """Sets the track_unallocated of this Segment.

        Track Unallocated Costs which are not assigned to any of the created Segments.  # noqa: E501

        :param track_unallocated: The track_unallocated of this Segment.  # noqa: E501
        :type: bool
        """

        self._track_unallocated = track_unallocated

    @property
    def report_settings(self):
        """Gets the report_settings of this Segment.  # noqa: E501


        :return: The report_settings of this Segment.  # noqa: E501
        :rtype: SegmentReportSettings
        """
        return self._report_settings

    @report_settings.setter
    def report_settings(self, report_settings):
        """Sets the report_settings of this Segment.


        :param report_settings: The report_settings of this Segment.  # noqa: E501
        :type: SegmentReportSettings
        """

        self._report_settings = report_settings

    @property
    def priority(self):
        """Gets the priority of this Segment.  # noqa: E501

        Costs are assigned in priority order across all Segments with assigned filters.  # noqa: E501

        :return: The priority of this Segment.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Segment.

        Costs are assigned in priority order across all Segments with assigned filters.  # noqa: E501

        :param priority: The priority of this Segment.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def filter(self):
        """Gets the filter of this Segment.  # noqa: E501

        The filter applied to the Segment. Additional documentation available at https://docs.vantage.sh/vql.  # noqa: E501

        :return: The filter of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Segment.

        The filter applied to the Segment. Additional documentation available at https://docs.vantage.sh/vql.  # noqa: E501

        :param filter: The filter of this Segment.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def created_at(self):
        """Gets the created_at of this Segment.  # noqa: E501

        The date and time, in UTC, the Segment was created. ISO 8601 Formatted.  # noqa: E501

        :return: The created_at of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Segment.

        The date and time, in UTC, the Segment was created. ISO 8601 Formatted.  # noqa: E501

        :param created_at: The created_at of this Segment.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def workspace_token(self):
        """Gets the workspace_token of this Segment.  # noqa: E501

        The token for the Workspace the Segment is a part of.  # noqa: E501

        :return: The workspace_token of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._workspace_token

    @workspace_token.setter
    def workspace_token(self, workspace_token):
        """Sets the workspace_token of this Segment.

        The token for the Workspace the Segment is a part of.  # noqa: E501

        :param workspace_token: The workspace_token of this Segment.  # noqa: E501
        :type: str
        """

        self._workspace_token = workspace_token

    @property
    def report_token(self):
        """Gets the report_token of this Segment.  # noqa: E501

        The token for the Report the Segment has generated.  # noqa: E501

        :return: The report_token of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._report_token

    @report_token.setter
    def report_token(self, report_token):
        """Sets the report_token of this Segment.

        The token for the Report the Segment has generated.  # noqa: E501

        :param report_token: The report_token of this Segment.  # noqa: E501
        :type: str
        """

        self._report_token = report_token

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
        if issubclass(Segment, dict):
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
        if not isinstance(other, Segment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Segment):
            return True

        return self.to_dict() != other.to_dict()
