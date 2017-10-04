# coding: utf-8

"""
    SNC API

    This is an API server for the data scraped from the SNC website.

    OpenAPI spec version: 1.0.0
    Contact: not-an-email@example.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.teams_api import TeamsApi


class TestTeamsApi(unittest.TestCase):
    """ TeamsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.teams_api.TeamsApi()

    def tearDown(self):
        pass

    def test_create_team(self):
        """
        Test case for create_team

        Create team
        """
        pass

    def test_get_team_by_name(self):
        """
        Test case for get_team_by_name

        Get team by name
        """
        pass

    def test_teams(self):
        """
        Test case for teams

        Get all teams
        """
        pass

    def test_update_team(self):
        """
        Test case for update_team

        Updated team
        """
        pass


if __name__ == '__main__':
    unittest.main()