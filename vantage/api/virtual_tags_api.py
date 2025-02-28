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


class VirtualTagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_virtual_tag_config(self, create_virtual_tag_config, **kwargs):  # noqa: E501
        """create_virtual_tag_config  # noqa: E501

        Create a new VirtualTagConfig.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_virtual_tag_config(create_virtual_tag_config, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateVirtualTagConfig create_virtual_tag_config: (required)
        :return: VirtualTagConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_virtual_tag_config_with_http_info(create_virtual_tag_config, **kwargs)  # noqa: E501
        else:
            (data) = self.create_virtual_tag_config_with_http_info(create_virtual_tag_config, **kwargs)  # noqa: E501
            return data

    def create_virtual_tag_config_with_http_info(self, create_virtual_tag_config, **kwargs):  # noqa: E501
        """create_virtual_tag_config  # noqa: E501

        Create a new VirtualTagConfig.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_virtual_tag_config_with_http_info(create_virtual_tag_config, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateVirtualTagConfig create_virtual_tag_config: (required)
        :return: VirtualTagConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_virtual_tag_config']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_virtual_tag_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_virtual_tag_config' is set
        if self.api_client.client_side_validation and ('create_virtual_tag_config' not in params or
                                                       params['create_virtual_tag_config'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `create_virtual_tag_config` when calling `create_virtual_tag_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_virtual_tag_config' in params:
            body_params = params['create_virtual_tag_config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/virtual_tag_configs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VirtualTagConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_virtual_tag_config(self, token, **kwargs):  # noqa: E501
        """delete_virtual_tag_config  # noqa: E501

        Deletes an existing VirtualTagConfig.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_virtual_tag_config(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :return: VirtualTagConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_virtual_tag_config_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_virtual_tag_config_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def delete_virtual_tag_config_with_http_info(self, token, **kwargs):  # noqa: E501
        """delete_virtual_tag_config  # noqa: E501

        Deletes an existing VirtualTagConfig.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_virtual_tag_config_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :return: VirtualTagConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_virtual_tag_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in params or
                                                       params['token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `token` when calling `delete_virtual_tag_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501

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
            '/virtual_tag_configs/{token}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VirtualTagConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_virtual_tag_config(self, token, **kwargs):  # noqa: E501
        """get_virtual_tag_config  # noqa: E501

        Return a specific VirtualTagConfig.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_virtual_tag_config(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :return: VirtualTagConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_virtual_tag_config_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_virtual_tag_config_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def get_virtual_tag_config_with_http_info(self, token, **kwargs):  # noqa: E501
        """get_virtual_tag_config  # noqa: E501

        Return a specific VirtualTagConfig.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_virtual_tag_config_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :return: VirtualTagConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_virtual_tag_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in params or
                                                       params['token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `token` when calling `get_virtual_tag_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501

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
            '/virtual_tag_configs/{token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VirtualTagConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_virtual_tag_configs(self, **kwargs):  # noqa: E501
        """get_virtual_tag_configs  # noqa: E501

        Return all VirtualTagConfigs that the current API token has access to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_virtual_tag_configs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: VirtualTagConfigs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_virtual_tag_configs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_virtual_tag_configs_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_virtual_tag_configs_with_http_info(self, **kwargs):  # noqa: E501
        """get_virtual_tag_configs  # noqa: E501

        Return all VirtualTagConfigs that the current API token has access to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_virtual_tag_configs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: VirtualTagConfigs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_virtual_tag_configs" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/virtual_tag_configs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VirtualTagConfigs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_virtual_tag_config(self, token, update_virtual_tag_config, **kwargs):  # noqa: E501
        """update_virtual_tag_config  # noqa: E501

        Updates an existing VirtualTagConfig.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_virtual_tag_config(token, update_virtual_tag_config, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :param UpdateVirtualTagConfig update_virtual_tag_config: (required)
        :return: VirtualTagConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_virtual_tag_config_with_http_info(token, update_virtual_tag_config, **kwargs)  # noqa: E501
        else:
            (data) = self.update_virtual_tag_config_with_http_info(token, update_virtual_tag_config, **kwargs)  # noqa: E501
            return data

    def update_virtual_tag_config_with_http_info(self, token, update_virtual_tag_config, **kwargs):  # noqa: E501
        """update_virtual_tag_config  # noqa: E501

        Updates an existing VirtualTagConfig.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_virtual_tag_config_with_http_info(token, update_virtual_tag_config, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :param UpdateVirtualTagConfig update_virtual_tag_config: (required)
        :return: VirtualTagConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'update_virtual_tag_config']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_virtual_tag_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in params or
                                                       params['token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `token` when calling `update_virtual_tag_config`")  # noqa: E501
        # verify the required parameter 'update_virtual_tag_config' is set
        if self.api_client.client_side_validation and ('update_virtual_tag_config' not in params or
                                                       params['update_virtual_tag_config'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `update_virtual_tag_config` when calling `update_virtual_tag_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_virtual_tag_config' in params:
            body_params = params['update_virtual_tag_config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/virtual_tag_configs/{token}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VirtualTagConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
