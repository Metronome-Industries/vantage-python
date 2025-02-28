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
from vantage.api.workspaces_api import WorkspacesApi  # noqa: E501
from vantage.rest import ApiException


class TestWorkspacesApi(unittest.TestCase):
    """WorkspacesApi unit test stubs"""

    def setUp(self):
        self.api = vantage.api.workspaces_api.WorkspacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_workspace(self):
        """Test case for create_workspace

        """
        pass

    def test_delete_workspace(self):
        """Test case for delete_workspace

        """
        pass

    def test_get_workspace(self):
        """Test case for get_workspace

        """
        pass

    def test_get_workspaces(self):
        """Test case for get_workspaces

        """
        pass

    def test_update_workspace(self):
        """Test case for update_workspace

        """
        pass


if __name__ == '__main__':
    unittest.main()
