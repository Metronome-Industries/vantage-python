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


class UpdateSegment(object):
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
        'description': 'str',
        'priority': 'int',
        'track_unallocated': 'bool',
        'report_settings': 'CreateSegmentReportSettings',
        'filter': 'str',
        'parent_segment_token': 'str'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'priority': 'priority',
        'track_unallocated': 'track_unallocated',
        'report_settings': 'report_settings',
        'filter': 'filter',
        'parent_segment_token': 'parent_segment_token'
    }

    def __init__(self, title=None, description=None, priority=None, track_unallocated=False, report_settings=None, filter=None, parent_segment_token=None, _configuration=None):  # noqa: E501
        """UpdateSegment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._title = None
        self._description = None
        self._priority = None
        self._track_unallocated = None
        self._report_settings = None
        self._filter = None
        self._parent_segment_token = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if priority is not None:
            self.priority = priority
        if track_unallocated is not None:
            self.track_unallocated = track_unallocated
        if report_settings is not None:
            self.report_settings = report_settings
        if filter is not None:
            self.filter = filter
        if parent_segment_token is not None:
            self.parent_segment_token = parent_segment_token

    @property
    def title(self):
        """Gets the title of this UpdateSegment.  # noqa: E501

        The title of the Segment.  # noqa: E501

        :return: The title of this UpdateSegment.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdateSegment.

        The title of the Segment.  # noqa: E501

        :param title: The title of this UpdateSegment.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this UpdateSegment.  # noqa: E501

        The description of the Segment.  # noqa: E501

        :return: The description of this UpdateSegment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSegment.

        The description of the Segment.  # noqa: E501

        :param description: The description of this UpdateSegment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def priority(self):
        """Gets the priority of this UpdateSegment.  # noqa: E501

        The priority of the Segment.  # noqa: E501

        :return: The priority of this UpdateSegment.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpdateSegment.

        The priority of the Segment.  # noqa: E501

        :param priority: The priority of this UpdateSegment.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def track_unallocated(self):
        """Gets the track_unallocated of this UpdateSegment.  # noqa: E501

        Track Unallocated Costs which are not assigned to any of the created Segments.  # noqa: E501

        :return: The track_unallocated of this UpdateSegment.  # noqa: E501
        :rtype: bool
        """
        return self._track_unallocated

    @track_unallocated.setter
    def track_unallocated(self, track_unallocated):
        """Sets the track_unallocated of this UpdateSegment.

        Track Unallocated Costs which are not assigned to any of the created Segments.  # noqa: E501

        :param track_unallocated: The track_unallocated of this UpdateSegment.  # noqa: E501
        :type: bool
        """

        self._track_unallocated = track_unallocated

    @property
    def report_settings(self):
        """Gets the report_settings of this UpdateSegment.  # noqa: E501


        :return: The report_settings of this UpdateSegment.  # noqa: E501
        :rtype: CreateSegmentReportSettings
        """
        return self._report_settings

    @report_settings.setter
    def report_settings(self, report_settings):
        """Sets the report_settings of this UpdateSegment.


        :param report_settings: The report_settings of this UpdateSegment.  # noqa: E501
        :type: CreateSegmentReportSettings
        """

        self._report_settings = report_settings

    @property
    def filter(self):
        """Gets the filter of this UpdateSegment.  # noqa: E501

        The filter query language to apply to the Segment. Additional documentation available at https://docs.vantage.sh/vql.  # noqa: E501

        :return: The filter of this UpdateSegment.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this UpdateSegment.

        The filter query language to apply to the Segment. Additional documentation available at https://docs.vantage.sh/vql.  # noqa: E501

        :param filter: The filter of this UpdateSegment.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def parent_segment_token(self):
        """Gets the parent_segment_token of this UpdateSegment.  # noqa: E501

        The token of the parent Segment this new Segment belongs to. Determines the Workspace the segment is assigned to.  # noqa: E501

        :return: The parent_segment_token of this UpdateSegment.  # noqa: E501
        :rtype: str
        """
        return self._parent_segment_token

    @parent_segment_token.setter
    def parent_segment_token(self, parent_segment_token):
        """Sets the parent_segment_token of this UpdateSegment.

        The token of the parent Segment this new Segment belongs to. Determines the Workspace the segment is assigned to.  # noqa: E501

        :param parent_segment_token: The parent_segment_token of this UpdateSegment.  # noqa: E501
        :type: str
        """

        self._parent_segment_token = parent_segment_token

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
        if issubclass(UpdateSegment, dict):
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
        if not isinstance(other, UpdateSegment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSegment):
            return True

        return self.to_dict() != other.to_dict()
