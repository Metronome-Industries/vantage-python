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
from vantage.api.resource_reports_api import ResourceReportsApi  # noqa: E501
from vantage.rest import ApiException


class TestResourceReportsApi(unittest.TestCase):
    """ResourceReportsApi unit test stubs"""

    def setUp(self):
        self.api = vantage.api.resource_reports_api.ResourceReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_resource_report(self):
        """Test case for create_resource_report

        """
        pass

    def test_delete_resource_report(self):
        """Test case for delete_resource_report

        """
        pass

    def test_get_resource_report(self):
        """Test case for get_resource_report

        """
        pass

    def test_get_resource_reports(self):
        """Test case for get_resource_reports

        """
        pass

    def test_update_resource_report(self):
        """Test case for update_resource_report

        """
        pass


if __name__ == '__main__':
    unittest.main()
