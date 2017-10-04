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
from swagger_client.apis.goalies_api import GoaliesApi


class TestGoaliesApi(unittest.TestCase):
    """ GoaliesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.goalies_api.GoaliesApi()

    def tearDown(self):
        pass

    def test_goalies(self):
        """
        Test case for goalies

        All goalies league wide
        """
        pass

    def test_save_goalie(self):
        """
        Test case for save_goalie

        Save a goalie
        """
        pass


if __name__ == '__main__':
    unittest.main()