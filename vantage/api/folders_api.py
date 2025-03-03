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


class FoldersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_folder(self, create_folder, **kwargs):  # noqa: E501
        """create_folder  # noqa: E501

        Create a Folder for CostReports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_folder(create_folder, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateFolder create_folder: (required)
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_folder_with_http_info(create_folder, **kwargs)  # noqa: E501
        else:
            (data) = self.create_folder_with_http_info(create_folder, **kwargs)  # noqa: E501
            return data

    def create_folder_with_http_info(self, create_folder, **kwargs):  # noqa: E501
        """create_folder  # noqa: E501

        Create a Folder for CostReports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_folder_with_http_info(create_folder, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateFolder create_folder: (required)
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_folder']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_folder' is set
        if self.api_client.client_side_validation and ('create_folder' not in params or
                                                       params['create_folder'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `create_folder` when calling `create_folder`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_folder' in params:
            body_params = params['create_folder']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/folders', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Folder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_folder(self, folder_token, **kwargs):  # noqa: E501
        """delete_folder  # noqa: E501

        Delete a Folder for CostReports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_folder(folder_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_token: (required)
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_folder_with_http_info(folder_token, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_folder_with_http_info(folder_token, **kwargs)  # noqa: E501
            return data

    def delete_folder_with_http_info(self, folder_token, **kwargs):  # noqa: E501
        """delete_folder  # noqa: E501

        Delete a Folder for CostReports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_folder_with_http_info(folder_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_token: (required)
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_token' is set
        if self.api_client.client_side_validation and ('folder_token' not in params or
                                                       params['folder_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder_token` when calling `delete_folder`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_token' in params:
            path_params['folder_token'] = params['folder_token']  # noqa: E501

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
            '/folders/{folder_token}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Folder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_folder(self, folder_token, **kwargs):  # noqa: E501
        """get_folder  # noqa: E501

        Return a specific Folder for CostReports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_folder(folder_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_token: (required)
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_folder_with_http_info(folder_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_folder_with_http_info(folder_token, **kwargs)  # noqa: E501
            return data

    def get_folder_with_http_info(self, folder_token, **kwargs):  # noqa: E501
        """get_folder  # noqa: E501

        Return a specific Folder for CostReports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_folder_with_http_info(folder_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_token: (required)
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_token' is set
        if self.api_client.client_side_validation and ('folder_token' not in params or
                                                       params['folder_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder_token` when calling `get_folder`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_token' in params:
            path_params['folder_token'] = params['folder_token']  # noqa: E501

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
            '/folders/{folder_token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Folder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_folders(self, **kwargs):  # noqa: E501
        """get_folders  # noqa: E501

        Return all Folders for CostReports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_folders(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results to return.
        :param int limit: The amount of results to return. The maximum is 1000.
        :return: Folders
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_folders_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_folders_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_folders_with_http_info(self, **kwargs):  # noqa: E501
        """get_folders  # noqa: E501

        Return all Folders for CostReports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_folders_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results to return.
        :param int limit: The amount of results to return. The maximum is 1000.
        :return: Folders
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
                    " to method get_folders" % key
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
            '/folders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Folders',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_folder(self, folder_token, update_folder, **kwargs):  # noqa: E501
        """update_folder  # noqa: E501

        Update a Folder for CostReports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_folder(folder_token, update_folder, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_token: (required)
        :param UpdateFolder update_folder: (required)
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_folder_with_http_info(folder_token, update_folder, **kwargs)  # noqa: E501
        else:
            (data) = self.update_folder_with_http_info(folder_token, update_folder, **kwargs)  # noqa: E501
            return data

    def update_folder_with_http_info(self, folder_token, update_folder, **kwargs):  # noqa: E501
        """update_folder  # noqa: E501

        Update a Folder for CostReports.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_folder_with_http_info(folder_token, update_folder, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_token: (required)
        :param UpdateFolder update_folder: (required)
        :return: Folder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_token', 'update_folder']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_token' is set
        if self.api_client.client_side_validation and ('folder_token' not in params or
                                                       params['folder_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder_token` when calling `update_folder`")  # noqa: E501
        # verify the required parameter 'update_folder' is set
        if self.api_client.client_side_validation and ('update_folder' not in params or
                                                       params['update_folder'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `update_folder` when calling `update_folder`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_token' in params:
            path_params['folder_token'] = params['folder_token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_folder' in params:
            body_params = params['update_folder']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/folders/{folder_token}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Folder',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
