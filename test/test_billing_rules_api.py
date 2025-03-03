# coding: utf-8

"""
    Vantage

    Vantage API  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@vantage.sh
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import vantage
from vantage.api.billing_rules_api import BillingRulesApi  # noqa: E501
from vantage.rest import ApiException


class TestBillingRulesApi(unittest.TestCase):
    """BillingRulesApi unit test stubs"""

    def setUp(self):
        self.api = vantage.api.billing_rules_api.BillingRulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_billing_rule(self):
        """Test case for create_billing_rule

        """
        pass

    def test_delete_billing_rule(self):
        """Test case for delete_billing_rule

        """
        pass

    def test_get_billing_rule(self):
        """Test case for get_billing_rule

        """
        pass

    def test_get_billing_rules(self):
        """Test case for get_billing_rules

        """
        pass

    def test_update_billing_rule(self):
        """Test case for update_billing_rule

        """
        pass


if __name__ == '__main__':
    unittest.main()
