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
from vantage.api.business_metrics_api import BusinessMetricsApi  # noqa: E501
from vantage.rest import ApiException


class TestBusinessMetricsApi(unittest.TestCase):
    """BusinessMetricsApi unit test stubs"""

    def setUp(self):
        self.api = vantage.api.business_metrics_api.BusinessMetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_business_metric(self):
        """Test case for create_business_metric

        """
        pass

    def test_delete_business_metric(self):
        """Test case for delete_business_metric

        """
        pass

    def test_get_business_metric(self):
        """Test case for get_business_metric

        """
        pass

    def test_get_business_metric_values(self):
        """Test case for get_business_metric_values

        """
        pass

    def test_get_business_metrics(self):
        """Test case for get_business_metrics

        """
        pass

    def test_update_business_metric(self):
        """Test case for update_business_metric

        """
        pass

    def test_update_business_metric_values_csv(self):
        """Test case for update_business_metric_values_csv

        """
        pass


if __name__ == '__main__':
    unittest.main()
