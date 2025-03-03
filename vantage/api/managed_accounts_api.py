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


class ManagedAccountsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_managed_account(self, create_managed_account, **kwargs):  # noqa: E501
        """create_managed_account  # noqa: E501

        Create a Managed Account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_managed_account(create_managed_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateManagedAccount create_managed_account: (required)
        :return: ManagedAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_managed_account_with_http_info(create_managed_account, **kwargs)  # noqa: E501
        else:
            (data) = self.create_managed_account_with_http_info(create_managed_account, **kwargs)  # noqa: E501
            return data

    def create_managed_account_with_http_info(self, create_managed_account, **kwargs):  # noqa: E501
        """create_managed_account  # noqa: E501

        Create a Managed Account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_managed_account_with_http_info(create_managed_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateManagedAccount create_managed_account: (required)
        :return: ManagedAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_managed_account']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_managed_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_managed_account' is set
        if self.api_client.client_side_validation and ('create_managed_account' not in params or
                                                       params['create_managed_account'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `create_managed_account` when calling `create_managed_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_managed_account' in params:
            body_params = params['create_managed_account']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/managed_accounts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ManagedAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_managed_account(self, managed_account_token, **kwargs):  # noqa: E501
        """delete_managed_account  # noqa: E501

        Delete a Managed Account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_managed_account(managed_account_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_account_token: (required)
        :return: ManagedAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_managed_account_with_http_info(managed_account_token, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_managed_account_with_http_info(managed_account_token, **kwargs)  # noqa: E501
            return data

    def delete_managed_account_with_http_info(self, managed_account_token, **kwargs):  # noqa: E501
        """delete_managed_account  # noqa: E501

        Delete a Managed Account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_managed_account_with_http_info(managed_account_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_account_token: (required)
        :return: ManagedAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['managed_account_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_managed_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'managed_account_token' is set
        if self.api_client.client_side_validation and ('managed_account_token' not in params or
                                                       params['managed_account_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `managed_account_token` when calling `delete_managed_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'managed_account_token' in params:
            path_params['managed_account_token'] = params['managed_account_token']  # noqa: E501

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
            '/managed_accounts/{managed_account_token}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ManagedAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_managed_account(self, managed_account_token, **kwargs):  # noqa: E501
        """get_managed_account  # noqa: E501

        Return a Managed Account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_managed_account(managed_account_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_account_token: (required)
        :return: ManagedAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_managed_account_with_http_info(managed_account_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_managed_account_with_http_info(managed_account_token, **kwargs)  # noqa: E501
            return data

    def get_managed_account_with_http_info(self, managed_account_token, **kwargs):  # noqa: E501
        """get_managed_account  # noqa: E501

        Return a Managed Account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_managed_account_with_http_info(managed_account_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_account_token: (required)
        :return: ManagedAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['managed_account_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_managed_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'managed_account_token' is set
        if self.api_client.client_side_validation and ('managed_account_token' not in params or
                                                       params['managed_account_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `managed_account_token` when calling `get_managed_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'managed_account_token' in params:
            path_params['managed_account_token'] = params['managed_account_token']  # noqa: E501

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
            '/managed_accounts/{managed_account_token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ManagedAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_managed_accounts(self, **kwargs):  # noqa: E501
        """get_managed_accounts  # noqa: E501

        Returns a list of managed accounts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_managed_accounts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results to return.
        :param int limit: The amount of results to return. The maximum is 1000.
        :return: ManagedAccounts
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_managed_accounts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_managed_accounts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_managed_accounts_with_http_info(self, **kwargs):  # noqa: E501
        """get_managed_accounts  # noqa: E501

        Returns a list of managed accounts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_managed_accounts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results to return.
        :param int limit: The amount of results to return. The maximum is 1000.
        :return: ManagedAccounts
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
                    " to method get_managed_accounts" % key
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
            '/managed_accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ManagedAccounts',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_managed_account(self, managed_account_token, update_managed_account, **kwargs):  # noqa: E501
        """update_managed_account  # noqa: E501

        Update a Managed Account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_managed_account(managed_account_token, update_managed_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_account_token: (required)
        :param UpdateManagedAccount update_managed_account: (required)
        :return: ManagedAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_managed_account_with_http_info(managed_account_token, update_managed_account, **kwargs)  # noqa: E501
        else:
            (data) = self.update_managed_account_with_http_info(managed_account_token, update_managed_account, **kwargs)  # noqa: E501
            return data

    def update_managed_account_with_http_info(self, managed_account_token, update_managed_account, **kwargs):  # noqa: E501
        """update_managed_account  # noqa: E501

        Update a Managed Account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_managed_account_with_http_info(managed_account_token, update_managed_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_account_token: (required)
        :param UpdateManagedAccount update_managed_account: (required)
        :return: ManagedAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['managed_account_token', 'update_managed_account']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_managed_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'managed_account_token' is set
        if self.api_client.client_side_validation and ('managed_account_token' not in params or
                                                       params['managed_account_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `managed_account_token` when calling `update_managed_account`")  # noqa: E501
        # verify the required parameter 'update_managed_account' is set
        if self.api_client.client_side_validation and ('update_managed_account' not in params or
                                                       params['update_managed_account'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `update_managed_account` when calling `update_managed_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'managed_account_token' in params:
            path_params['managed_account_token'] = params['managed_account_token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_managed_account' in params:
            body_params = params['update_managed_account']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/managed_accounts/{managed_account_token}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ManagedAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
