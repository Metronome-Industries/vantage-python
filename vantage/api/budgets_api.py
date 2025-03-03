# coding: utf-8

"""
    Vantage

    Vantage API  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@vantage.sh
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vantage.api_client import ApiClient


class BudgetsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_budget(self, create_budget, **kwargs):  # noqa: E501
        """create_budget  # noqa: E501

        Create a Budget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_budget(create_budget, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateBudget create_budget: (required)
        :return: Budget
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_budget_with_http_info(create_budget, **kwargs)  # noqa: E501
        else:
            (data) = self.create_budget_with_http_info(create_budget, **kwargs)  # noqa: E501
            return data

    def create_budget_with_http_info(self, create_budget, **kwargs):  # noqa: E501
        """create_budget  # noqa: E501

        Create a Budget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_budget_with_http_info(create_budget, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateBudget create_budget: (required)
        :return: Budget
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_budget']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_budget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_budget' is set
        if self.api_client.client_side_validation and ('create_budget' not in params or
                                                       params['create_budget'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `create_budget` when calling `create_budget`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_budget' in params:
            body_params = params['create_budget']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/budgets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Budget',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_budget(self, budget_token, **kwargs):  # noqa: E501
        """delete_budget  # noqa: E501

        Delete a Budget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_budget(budget_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_token: (required)
        :return: Budget
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_budget_with_http_info(budget_token, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_budget_with_http_info(budget_token, **kwargs)  # noqa: E501
            return data

    def delete_budget_with_http_info(self, budget_token, **kwargs):  # noqa: E501
        """delete_budget  # noqa: E501

        Delete a Budget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_budget_with_http_info(budget_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_token: (required)
        :return: Budget
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_budget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_token' is set
        if self.api_client.client_side_validation and ('budget_token' not in params or
                                                       params['budget_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `budget_token` when calling `delete_budget`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_token' in params:
            path_params['budget_token'] = params['budget_token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_token}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Budget',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_budget(self, budget_token, **kwargs):  # noqa: E501
        """get_budget  # noqa: E501

        Return a Budget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_budget(budget_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_token: (required)
        :param bool include_performance: Include performance data.
        :return: Budget
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_budget_with_http_info(budget_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_budget_with_http_info(budget_token, **kwargs)  # noqa: E501
            return data

    def get_budget_with_http_info(self, budget_token, **kwargs):  # noqa: E501
        """get_budget  # noqa: E501

        Return a Budget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_budget_with_http_info(budget_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_token: (required)
        :param bool include_performance: Include performance data.
        :return: Budget
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_token', 'include_performance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_budget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_token' is set
        if self.api_client.client_side_validation and ('budget_token' not in params or
                                                       params['budget_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `budget_token` when calling `get_budget`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_token' in params:
            path_params['budget_token'] = params['budget_token']  # noqa: E501

        query_params = []
        if 'include_performance' in params:
            query_params.append(('include_performance', params['include_performance']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Budget',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_budgets(self, **kwargs):  # noqa: E501
        """get_budgets  # noqa: E501

        Return all Budgets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_budgets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results to return.
        :param int limit: The number of results to return. The maximum is 1000.
        :return: Budgets
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_budgets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_budgets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_budgets_with_http_info(self, **kwargs):  # noqa: E501
        """get_budgets  # noqa: E501

        Return all Budgets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_budgets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results to return.
        :param int limit: The number of results to return. The maximum is 1000.
        :return: Budgets
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_budgets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/budgets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Budgets',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_budget(self, budget_token, update_budget, **kwargs):  # noqa: E501
        """update_budget  # noqa: E501

        Update a Budget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_budget(budget_token, update_budget, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_token: (required)
        :param UpdateBudget update_budget: (required)
        :return: Budget
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_budget_with_http_info(budget_token, update_budget, **kwargs)  # noqa: E501
        else:
            (data) = self.update_budget_with_http_info(budget_token, update_budget, **kwargs)  # noqa: E501
            return data

    def update_budget_with_http_info(self, budget_token, update_budget, **kwargs):  # noqa: E501
        """update_budget  # noqa: E501

        Update a Budget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_budget_with_http_info(budget_token, update_budget, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_token: (required)
        :param UpdateBudget update_budget: (required)
        :return: Budget
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_token', 'update_budget']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_budget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_token' is set
        if self.api_client.client_side_validation and ('budget_token' not in params or
                                                       params['budget_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `budget_token` when calling `update_budget`")  # noqa: E501
        # verify the required parameter 'update_budget' is set
        if self.api_client.client_side_validation and ('update_budget' not in params or
                                                       params['update_budget'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `update_budget` when calling `update_budget`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_token' in params:
            path_params['budget_token'] = params['budget_token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_budget' in params:
            body_params = params['update_budget']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_token}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Budget',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
