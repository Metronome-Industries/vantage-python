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


class AnomalyAlerts(object):
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
        'anomaly_alerts': 'list[AnomalyAlert]'
    }

    attribute_map = {
        'links': 'links',
        'anomaly_alerts': 'anomaly_alerts'
    }

    def __init__(self, links=None, anomaly_alerts=None, _configuration=None):  # noqa: E501
        """AnomalyAlerts - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._anomaly_alerts = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if anomaly_alerts is not None:
            self.anomaly_alerts = anomaly_alerts

    @property
    def links(self):
        """Gets the links of this AnomalyAlerts.  # noqa: E501


        :return: The links of this AnomalyAlerts.  # noqa: E501
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AnomalyAlerts.


        :param links: The links of this AnomalyAlerts.  # noqa: E501
        :type: object
        """

        self._links = links

    @property
    def anomaly_alerts(self):
        """Gets the anomaly_alerts of this AnomalyAlerts.  # noqa: E501


        :return: The anomaly_alerts of this AnomalyAlerts.  # noqa: E501
        :rtype: list[AnomalyAlert]
        """
        return self._anomaly_alerts

    @anomaly_alerts.setter
    def anomaly_alerts(self, anomaly_alerts):
        """Sets the anomaly_alerts of this AnomalyAlerts.


        :param anomaly_alerts: The anomaly_alerts of this AnomalyAlerts.  # noqa: E501
        :type: list[AnomalyAlert]
        """

        self._anomaly_alerts = anomaly_alerts

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
        if issubclass(AnomalyAlerts, dict):
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
        if not isinstance(other, AnomalyAlerts):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnomalyAlerts):
            return True

        return self.to_dict() != other.to_dict()
