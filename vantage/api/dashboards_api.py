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


class DashboardsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_dashboard(self, create_dashboard, **kwargs):  # noqa: E501
        """create_dashboard  # noqa: E501

        Create a Dashboard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_dashboard(create_dashboard, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateDashboard create_dashboard: (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_dashboard_with_http_info(create_dashboard, **kwargs)  # noqa: E501
        else:
            (data) = self.create_dashboard_with_http_info(create_dashboard, **kwargs)  # noqa: E501
            return data

    def create_dashboard_with_http_info(self, create_dashboard, **kwargs):  # noqa: E501
        """create_dashboard  # noqa: E501

        Create a Dashboard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_dashboard_with_http_info(create_dashboard, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateDashboard create_dashboard: (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_dashboard']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dashboard" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_dashboard' is set
        if self.api_client.client_side_validation and ('create_dashboard' not in params or
                                                       params['create_dashboard'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `create_dashboard` when calling `create_dashboard`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_dashboard' in params:
            body_params = params['create_dashboard']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/dashboards', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dashboard',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dashboard(self, dashboard_token, **kwargs):  # noqa: E501
        """delete_dashboard  # noqa: E501

        Delete a Dashboard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dashboard(dashboard_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_token: (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_dashboard_with_http_info(dashboard_token, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dashboard_with_http_info(dashboard_token, **kwargs)  # noqa: E501
            return data

    def delete_dashboard_with_http_info(self, dashboard_token, **kwargs):  # noqa: E501
        """delete_dashboard  # noqa: E501

        Delete a Dashboard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dashboard_with_http_info(dashboard_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_token: (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dashboard" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_token' is set
        if self.api_client.client_side_validation and ('dashboard_token' not in params or
                                                       params['dashboard_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `dashboard_token` when calling `delete_dashboard`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_token' in params:
            path_params['dashboard_token'] = params['dashboard_token']  # noqa: E501

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
            '/dashboards/{dashboard_token}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dashboard',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dashboard(self, dashboard_token, **kwargs):  # noqa: E501
        """get_dashboard  # noqa: E501

        Return a specific Dashboard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard(dashboard_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_token: (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dashboard_with_http_info(dashboard_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dashboard_with_http_info(dashboard_token, **kwargs)  # noqa: E501
            return data

    def get_dashboard_with_http_info(self, dashboard_token, **kwargs):  # noqa: E501
        """get_dashboard  # noqa: E501

        Return a specific Dashboard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboard_with_http_info(dashboard_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_token: (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dashboard" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_token' is set
        if self.api_client.client_side_validation and ('dashboard_token' not in params or
                                                       params['dashboard_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `dashboard_token` when calling `get_dashboard`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_token' in params:
            path_params['dashboard_token'] = params['dashboard_token']  # noqa: E501

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
            '/dashboards/{dashboard_token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dashboard',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dashboards(self, **kwargs):  # noqa: E501
        """get_dashboards  # noqa: E501

        Return all Dashboards.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboards(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results to return.
        :param int limit: The amount of results to return. The maximum is 1000.
        :return: Dashboards
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dashboards_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_dashboards_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_dashboards_with_http_info(self, **kwargs):  # noqa: E501
        """get_dashboards  # noqa: E501

        Return all Dashboards.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dashboards_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results to return.
        :param int limit: The amount of results to return. The maximum is 1000.
        :return: Dashboards
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
                    " to method get_dashboards" % key
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
            '/dashboards', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dashboards',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dashboard(self, dashboard_token, update_dashboard, **kwargs):  # noqa: E501
        """update_dashboard  # noqa: E501

        Update a Dashboard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dashboard(dashboard_token, update_dashboard, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_token: (required)
        :param UpdateDashboard update_dashboard: (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_dashboard_with_http_info(dashboard_token, update_dashboard, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dashboard_with_http_info(dashboard_token, update_dashboard, **kwargs)  # noqa: E501
            return data

    def update_dashboard_with_http_info(self, dashboard_token, update_dashboard, **kwargs):  # noqa: E501
        """update_dashboard  # noqa: E501

        Update a Dashboard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dashboard_with_http_info(dashboard_token, update_dashboard, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_token: (required)
        :param UpdateDashboard update_dashboard: (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_token', 'update_dashboard']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dashboard" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_token' is set
        if self.api_client.client_side_validation and ('dashboard_token' not in params or
                                                       params['dashboard_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `dashboard_token` when calling `update_dashboard`")  # noqa: E501
        # verify the required parameter 'update_dashboard' is set
        if self.api_client.client_side_validation and ('update_dashboard' not in params or
                                                       params['update_dashboard'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `update_dashboard` when calling `update_dashboard`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_token' in params:
            path_params['dashboard_token'] = params['dashboard_token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_dashboard' in params:
            body_params = params['update_dashboard']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/dashboards/{dashboard_token}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dashboard',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
