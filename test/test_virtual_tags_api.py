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
from vantage.api.virtual_tags_api import VirtualTagsApi  # noqa: E501
from vantage.rest import ApiException


class TestVirtualTagsApi(unittest.TestCase):
    """VirtualTagsApi unit test stubs"""

    def setUp(self):
        self.api = vantage.api.virtual_tags_api.VirtualTagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_virtual_tag_config(self):
        """Test case for create_virtual_tag_config

        """
        pass

    def test_delete_virtual_tag_config(self):
        """Test case for delete_virtual_tag_config

        """
        pass

    def test_get_virtual_tag_config(self):
        """Test case for get_virtual_tag_config

        """
        pass

    def test_get_virtual_tag_configs(self):
        """Test case for get_virtual_tag_configs

        """
        pass

    def test_update_virtual_tag_config(self):
        """Test case for update_virtual_tag_config

        """
        pass


if __name__ == '__main__':
    unittest.main()
