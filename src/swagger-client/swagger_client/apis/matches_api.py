# coding: utf-8

"""
    SNC API

    This is an API server for the data scraped from the SNC website.

    OpenAPI spec version: 1.0.0
    Contact: not-an-email@example.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class MatchesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_match(self, body, **kwargs):
        """
        Add a new match
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_match(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Match body: Match object that needs to be added to the system (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_match_with_http_info(body, **kwargs)
        else:
            (data) = self.add_match_with_http_info(body, **kwargs)
            return data

    def add_match_with_http_info(self, body, **kwargs):
        """
        Add a new match
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_match_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Match body: Match object that needs to be added to the system (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_match" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_match`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api('/matches', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def find_match(self, match_id, **kwargs):
        """
        Get a specific match
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_match(match_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int match_id: ID of the match to fetch (required)
        :return: Match
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.find_match_with_http_info(match_id, **kwargs)
        else:
            (data) = self.find_match_with_http_info(match_id, **kwargs)
            return data

    def find_match_with_http_info(self, match_id, **kwargs):
        """
        Get a specific match
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_match_with_http_info(match_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int match_id: ID of the match to fetch (required)
        :return: Match
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['match_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_match" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'match_id' is set
        if ('match_id' not in params) or (params['match_id'] is None):
            raise ValueError("Missing the required parameter `match_id` when calling `find_match`")


        collection_formats = {}

        path_params = {}
        if 'match_id' in params:
            path_params['matchId'] = params['match_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/matches/{matchId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Match',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def find_team_schedule(self, team_name, **kwargs):
        """
        Find this season's schedule for a given team
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_team_schedule(team_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int team_name: Name of the team whose schedule should be fetched (required)
        :return: list[Match]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.find_team_schedule_with_http_info(team_name, **kwargs)
        else:
            (data) = self.find_team_schedule_with_http_info(team_name, **kwargs)
            return data

    def find_team_schedule_with_http_info(self, team_name, **kwargs):
        """
        Find this season's schedule for a given team
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_team_schedule_with_http_info(team_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int team_name: Name of the team whose schedule should be fetched (required)
        :return: list[Match]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_name']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_team_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'team_name' is set
        if ('team_name' not in params) or (params['team_name'] is None):
            raise ValueError("Missing the required parameter `team_name` when calling `find_team_schedule`")


        collection_formats = {}

        path_params = {}
        if 'team_name' in params:
            path_params['teamName'] = params['team_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/matches/team/{teamName}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Match]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def match_summary(self, match_id, **kwargs):
        """
        Get a specific match
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.match_summary(match_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int match_id: ID of the match to fetch (required)
        :return: MatchSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.match_summary_with_http_info(match_id, **kwargs)
        else:
            (data) = self.match_summary_with_http_info(match_id, **kwargs)
            return data

    def match_summary_with_http_info(self, match_id, **kwargs):
        """
        Get a specific match
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.match_summary_with_http_info(match_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int match_id: ID of the match to fetch (required)
        :return: MatchSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['match_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method match_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'match_id' is set
        if ('match_id' not in params) or (params['match_id'] is None):
            raise ValueError("Missing the required parameter `match_id` when calling `match_summary`")


        collection_formats = {}

        path_params = {}
        if 'match_id' in params:
            path_params['matchId'] = params['match_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/matches/{matchId}/summary', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MatchSummary',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def save_match_summary(self, match_id, body, **kwargs):
        """
        Update the match summary
        Used to update a match's summary. There is no POST because summaries are automatically generated when a match is created
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.save_match_summary(match_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int match_id: ID of the match to fetch (required)
        :param MatchSummary body: Match summary that needs to be saved (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.save_match_summary_with_http_info(match_id, body, **kwargs)
        else:
            (data) = self.save_match_summary_with_http_info(match_id, body, **kwargs)
            return data

    def save_match_summary_with_http_info(self, match_id, body, **kwargs):
        """
        Update the match summary
        Used to update a match's summary. There is no POST because summaries are automatically generated when a match is created
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.save_match_summary_with_http_info(match_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int match_id: ID of the match to fetch (required)
        :param MatchSummary body: Match summary that needs to be saved (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['match_id', 'body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_match_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'match_id' is set
        if ('match_id' not in params) or (params['match_id'] is None):
            raise ValueError("Missing the required parameter `match_id` when calling `save_match_summary`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `save_match_summary`")


        collection_formats = {}

        path_params = {}
        if 'match_id' in params:
            path_params['matchId'] = params['match_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api('/matches/{matchId}/summary', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def season_matches(self, **kwargs):
        """
        Get the current season's matches
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.season_matches(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Match]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.season_matches_with_http_info(**kwargs)
        else:
            (data) = self.season_matches_with_http_info(**kwargs)
            return data

    def season_matches_with_http_info(self, **kwargs):
        """
        Get the current season's matches
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.season_matches_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Match]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method season_matches" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/matches', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Match]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_match(self, match_id, body, **kwargs):
        """
        Update an existing match
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_match(match_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int match_id: ID of the match to update (required)
        :param Match body: Match object that needs to be updated (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_match_with_http_info(match_id, body, **kwargs)
        else:
            (data) = self.update_match_with_http_info(match_id, body, **kwargs)
            return data

    def update_match_with_http_info(self, match_id, body, **kwargs):
        """
        Update an existing match
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_match_with_http_info(match_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int match_id: ID of the match to update (required)
        :param Match body: Match object that needs to be updated (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['match_id', 'body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_match" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'match_id' is set
        if ('match_id' not in params) or (params['match_id'] is None):
            raise ValueError("Missing the required parameter `match_id` when calling `update_match`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_match`")


        collection_formats = {}

        path_params = {}
        if 'match_id' in params:
            path_params['matchId'] = params['match_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api('/matches/{matchId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
