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
from vantage.api.teams_api import TeamsApi  # noqa: E501
from vantage.rest import ApiException


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = vantage.api.teams_api.TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_team(self):
        """Test case for create_team

        """
        pass

    def test_delete_team(self):
        """Test case for delete_team

        """
        pass

    def test_get_team(self):
        """Test case for get_team

        """
        pass

    def test_get_teams(self):
        """Test case for get_teams

        """
        pass

    def test_update_team(self):
        """Test case for update_team

        """
        pass


if __name__ == '__main__':
    unittest.main()
