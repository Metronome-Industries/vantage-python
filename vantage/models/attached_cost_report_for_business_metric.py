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


class AttachedCostReportForBusinessMetric(object):
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
        'unit_scale': 'str',
        'label_filter': 'list[str]'
    }

    attribute_map = {
        'cost_report_token': 'cost_report_token',
        'unit_scale': 'unit_scale',
        'label_filter': 'label_filter'
    }

    def __init__(self, cost_report_token=None, unit_scale=None, label_filter=None, _configuration=None):  # noqa: E501
        """AttachedCostReportForBusinessMetric - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cost_report_token = None
        self._unit_scale = None
        self._label_filter = None
        self.discriminator = None

        if cost_report_token is not None:
            self.cost_report_token = cost_report_token
        if unit_scale is not None:
            self.unit_scale = unit_scale
        if label_filter is not None:
            self.label_filter = label_filter

    @property
    def cost_report_token(self):
        """Gets the cost_report_token of this AttachedCostReportForBusinessMetric.  # noqa: E501

        The token of the CostReport the BusinessMetric is attached to.  # noqa: E501

        :return: The cost_report_token of this AttachedCostReportForBusinessMetric.  # noqa: E501
        :rtype: str
        """
        return self._cost_report_token

    @cost_report_token.setter
    def cost_report_token(self, cost_report_token):
        """Sets the cost_report_token of this AttachedCostReportForBusinessMetric.

        The token of the CostReport the BusinessMetric is attached to.  # noqa: E501

        :param cost_report_token: The cost_report_token of this AttachedCostReportForBusinessMetric.  # noqa: E501
        :type: str
        """

        self._cost_report_token = cost_report_token

    @property
    def unit_scale(self):
        """Gets the unit_scale of this AttachedCostReportForBusinessMetric.  # noqa: E501

        Determines the scale of the BusinessMetric's values within a particular CostReport.  # noqa: E501

        :return: The unit_scale of this AttachedCostReportForBusinessMetric.  # noqa: E501
        :rtype: str
        """
        return self._unit_scale

    @unit_scale.setter
    def unit_scale(self, unit_scale):
        """Sets the unit_scale of this AttachedCostReportForBusinessMetric.

        Determines the scale of the BusinessMetric's values within a particular CostReport.  # noqa: E501

        :param unit_scale: The unit_scale of this AttachedCostReportForBusinessMetric.  # noqa: E501
        :type: str
        """
        allowed_values = ["per_unit", "per_hundred", "per_thousand", "per_million", "per_billion"]  # noqa: E501
        if (self._configuration.client_side_validation and
                unit_scale not in allowed_values):
            raise ValueError(
                "Invalid value for `unit_scale` ({0}), must be one of {1}"  # noqa: E501
                .format(unit_scale, allowed_values)
            )

        self._unit_scale = unit_scale

    @property
    def label_filter(self):
        """Gets the label_filter of this AttachedCostReportForBusinessMetric.  # noqa: E501

        The labels that the BusinessMetric is filtered by within a particular CostReport.  # noqa: E501

        :return: The label_filter of this AttachedCostReportForBusinessMetric.  # noqa: E501
        :rtype: list[str]
        """
        return self._label_filter

    @label_filter.setter
    def label_filter(self, label_filter):
        """Sets the label_filter of this AttachedCostReportForBusinessMetric.

        The labels that the BusinessMetric is filtered by within a particular CostReport.  # noqa: E501

        :param label_filter: The label_filter of this AttachedCostReportForBusinessMetric.  # noqa: E501
        :type: list[str]
        """

        self._label_filter = label_filter

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
        if issubclass(AttachedCostReportForBusinessMetric, dict):
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
        if not isinstance(other, AttachedCostReportForBusinessMetric):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachedCostReportForBusinessMetric):
            return True

        return self.to_dict() != other.to_dict()
