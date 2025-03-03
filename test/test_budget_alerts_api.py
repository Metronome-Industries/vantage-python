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
from vantage.api.budget_alerts_api import BudgetAlertsApi  # noqa: E501
from vantage.rest import ApiException


class TestBudgetAlertsApi(unittest.TestCase):
    """BudgetAlertsApi unit test stubs"""

    def setUp(self):
        self.api = vantage.api.budget_alerts_api.BudgetAlertsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_budget_alert(self):
        """Test case for create_budget_alert

        """
        pass

    def test_delete_budget_alert(self):
        """Test case for delete_budget_alert

        """
        pass

    def test_get_budget_alert(self):
        """Test case for get_budget_alert

        """
        pass

    def test_get_budget_alerts(self):
        """Test case for get_budget_alerts

        """
        pass

    def test_update_budget_alert(self):
        """Test case for update_budget_alert

        """
        pass


if __name__ == '__main__':
    unittest.main()
