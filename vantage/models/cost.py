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


class Cost(object):
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
        'accrued_at': 'str',
        'amount': 'str',
        'currency': 'str',
        'usage': 'object',
        'provider': 'str',
        'billing_account_id': 'str',
        'account_id': 'str',
        'service': 'str',
        'region': 'str',
        'resource_id': 'str',
        'tag': 'str',
        'tags': 'list[str]',
        'cost_category': 'str',
        'cost_subcategory': 'str'
    }

    attribute_map = {
        'links': 'links',
        'accrued_at': 'accrued_at',
        'amount': 'amount',
        'currency': 'currency',
        'usage': 'usage',
        'provider': 'provider',
        'billing_account_id': 'billing_account_id',
        'account_id': 'account_id',
        'service': 'service',
        'region': 'region',
        'resource_id': 'resource_id',
        'tag': 'tag',
        'tags': 'tags',
        'cost_category': 'cost_category',
        'cost_subcategory': 'cost_subcategory'
    }

    def __init__(self, links=None, accrued_at=None, amount=None, currency=None, usage=None, provider=None, billing_account_id=None, account_id=None, service=None, region=None, resource_id=None, tag=None, tags=None, cost_category=None, cost_subcategory=None, _configuration=None):  # noqa: E501
        """Cost - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._accrued_at = None
        self._amount = None
        self._currency = None
        self._usage = None
        self._provider = None
        self._billing_account_id = None
        self._account_id = None
        self._service = None
        self._region = None
        self._resource_id = None
        self._tag = None
        self._tags = None
        self._cost_category = None
        self._cost_subcategory = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if accrued_at is not None:
            self.accrued_at = accrued_at
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if usage is not None:
            self.usage = usage
        if provider is not None:
            self.provider = provider
        if billing_account_id is not None:
            self.billing_account_id = billing_account_id
        if account_id is not None:
            self.account_id = account_id
        if service is not None:
            self.service = service
        if region is not None:
            self.region = region
        if resource_id is not None:
            self.resource_id = resource_id
        if tag is not None:
            self.tag = tag
        if tags is not None:
            self.tags = tags
        if cost_category is not None:
            self.cost_category = cost_category
        if cost_subcategory is not None:
            self.cost_subcategory = cost_subcategory

    @property
    def links(self):
        """Gets the links of this Cost.  # noqa: E501


        :return: The links of this Cost.  # noqa: E501
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Cost.


        :param links: The links of this Cost.  # noqa: E501
        :type: object
        """

        self._links = links

    @property
    def accrued_at(self):
        """Gets the accrued_at of this Cost.  # noqa: E501

        The date the cost was accrued. ISO 8601 Formatted.  # noqa: E501

        :return: The accrued_at of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._accrued_at

    @accrued_at.setter
    def accrued_at(self, accrued_at):
        """Sets the accrued_at of this Cost.

        The date the cost was accrued. ISO 8601 Formatted.  # noqa: E501

        :param accrued_at: The accrued_at of this Cost.  # noqa: E501
        :type: str
        """

        self._accrued_at = accrued_at

    @property
    def amount(self):
        """Gets the amount of this Cost.  # noqa: E501

        The amount of the cost.  # noqa: E501

        :return: The amount of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Cost.

        The amount of the cost.  # noqa: E501

        :param amount: The amount of this Cost.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this Cost.  # noqa: E501

        The currency of the cost.  # noqa: E501

        :return: The currency of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Cost.

        The currency of the cost.  # noqa: E501

        :param currency: The currency of this Cost.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def usage(self):
        """Gets the usage of this Cost.  # noqa: E501

        The usage amount and unit incurred by the cost.  # noqa: E501

        :return: The usage of this Cost.  # noqa: E501
        :rtype: object
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this Cost.

        The usage amount and unit incurred by the cost.  # noqa: E501

        :param usage: The usage of this Cost.  # noqa: E501
        :type: object
        """

        self._usage = usage

    @property
    def provider(self):
        """Gets the provider of this Cost.  # noqa: E501

        The cost provider which incurred the cost.  # noqa: E501

        :return: The provider of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Cost.

        The cost provider which incurred the cost.  # noqa: E501

        :param provider: The provider of this Cost.  # noqa: E501
        :type: str
        """
        allowed_values = ["aws", "azure", "gcp", "snowflake", "databricks", "mongo", "datadog", "fastly", "new_relic", "opencost", "open_ai", "oracle", "confluent", "planetscale", "coralogix", "kubernetes", "custom_provider", "github", "linode", "grafana", "clickhouse", "temporal"]  # noqa: E501
        if (self._configuration.client_side_validation and
                provider not in allowed_values):
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def billing_account_id(self):
        """Gets the billing_account_id of this Cost.  # noqa: E501

        The cost provider's billing account id that incurred the cost.  # noqa: E501

        :return: The billing_account_id of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._billing_account_id

    @billing_account_id.setter
    def billing_account_id(self, billing_account_id):
        """Sets the billing_account_id of this Cost.

        The cost provider's billing account id that incurred the cost.  # noqa: E501

        :param billing_account_id: The billing_account_id of this Cost.  # noqa: E501
        :type: str
        """

        self._billing_account_id = billing_account_id

    @property
    def account_id(self):
        """Gets the account_id of this Cost.  # noqa: E501

        The cost provider's account id that incurred the cost.  # noqa: E501

        :return: The account_id of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Cost.

        The cost provider's account id that incurred the cost.  # noqa: E501

        :param account_id: The account_id of this Cost.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def service(self):
        """Gets the service of this Cost.  # noqa: E501

        The service which incurred the cost.  # noqa: E501

        :return: The service of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Cost.

        The service which incurred the cost.  # noqa: E501

        :param service: The service of this Cost.  # noqa: E501
        :type: str
        """

        self._service = service

    @property
    def region(self):
        """Gets the region of this Cost.  # noqa: E501

        The region which incurred the cost.  # noqa: E501

        :return: The region of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Cost.

        The region which incurred the cost.  # noqa: E501

        :param region: The region of this Cost.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def resource_id(self):
        """Gets the resource_id of this Cost.  # noqa: E501

        The resource id which incurred the cost.  # noqa: E501

        :return: The resource_id of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Cost.

        The resource id which incurred the cost.  # noqa: E501

        :param resource_id: The resource_id of this Cost.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def tag(self):
        """Gets the tag of this Cost.  # noqa: E501

        The tag attached to the cost that was incurred. DEPRECATED: does not support multiple tags.  # noqa: E501

        :return: The tag of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Cost.

        The tag attached to the cost that was incurred. DEPRECATED: does not support multiple tags.  # noqa: E501

        :param tag: The tag of this Cost.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def tags(self):
        """Gets the tags of this Cost.  # noqa: E501

        The tag pairs attached to the cost that was incurred.  # noqa: E501

        :return: The tags of this Cost.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Cost.

        The tag pairs attached to the cost that was incurred.  # noqa: E501

        :param tags: The tags of this Cost.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def cost_category(self):
        """Gets the cost_category of this Cost.  # noqa: E501

        The category for the cost.  # noqa: E501

        :return: The cost_category of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._cost_category

    @cost_category.setter
    def cost_category(self, cost_category):
        """Sets the cost_category of this Cost.

        The category for the cost.  # noqa: E501

        :param cost_category: The cost_category of this Cost.  # noqa: E501
        :type: str
        """

        self._cost_category = cost_category

    @property
    def cost_subcategory(self):
        """Gets the cost_subcategory of this Cost.  # noqa: E501

        The subcategory for the cost.  # noqa: E501

        :return: The cost_subcategory of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._cost_subcategory

    @cost_subcategory.setter
    def cost_subcategory(self, cost_subcategory):
        """Sets the cost_subcategory of this Cost.

        The subcategory for the cost.  # noqa: E501

        :param cost_subcategory: The cost_subcategory of this Cost.  # noqa: E501
        :type: str
        """

        self._cost_subcategory = cost_subcategory

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
        if issubclass(Cost, dict):
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
        if not isinstance(other, Cost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cost):
            return True

        return self.to_dict() != other.to_dict()
