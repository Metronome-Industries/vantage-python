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
from vantage.api.resources_api import ResourcesApi  # noqa: E501
from vantage.rest import ApiException


class TestResourcesApi(unittest.TestCase):
    """ResourcesApi unit test stubs"""

    def setUp(self):
        self.api = vantage.api.resources_api.ResourcesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_report_resources(self):
        """Test case for get_report_resources

        """
        pass

    def test_get_resource(self):
        """Test case for get_resource

        """
        pass


if __name__ == '__main__':
    unittest.main()
