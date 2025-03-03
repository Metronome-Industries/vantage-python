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


class BillingRulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_billing_rule(self, create_billing_rule, **kwargs):  # noqa: E501
        """create_billing_rule  # noqa: E501

        Create a Billing Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_billing_rule(create_billing_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateBillingRule create_billing_rule: (required)
        :return: BillingRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_billing_rule_with_http_info(create_billing_rule, **kwargs)  # noqa: E501
        else:
            (data) = self.create_billing_rule_with_http_info(create_billing_rule, **kwargs)  # noqa: E501
            return data

    def create_billing_rule_with_http_info(self, create_billing_rule, **kwargs):  # noqa: E501
        """create_billing_rule  # noqa: E501

        Create a Billing Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_billing_rule_with_http_info(create_billing_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateBillingRule create_billing_rule: (required)
        :return: BillingRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_billing_rule']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_billing_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_billing_rule' is set
        if self.api_client.client_side_validation and ('create_billing_rule' not in params or
                                                       params['create_billing_rule'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `create_billing_rule` when calling `create_billing_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_billing_rule' in params:
            body_params = params['create_billing_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/billing_rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BillingRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_billing_rule(self, billing_rule_token, **kwargs):  # noqa: E501
        """delete_billing_rule  # noqa: E501

        Delete a Billing Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_billing_rule(billing_rule_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_rule_token: (required)
        :return: BillingRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_billing_rule_with_http_info(billing_rule_token, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_billing_rule_with_http_info(billing_rule_token, **kwargs)  # noqa: E501
            return data

    def delete_billing_rule_with_http_info(self, billing_rule_token, **kwargs):  # noqa: E501
        """delete_billing_rule  # noqa: E501

        Delete a Billing Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_billing_rule_with_http_info(billing_rule_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_rule_token: (required)
        :return: BillingRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_rule_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_billing_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'billing_rule_token' is set
        if self.api_client.client_side_validation and ('billing_rule_token' not in params or
                                                       params['billing_rule_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `billing_rule_token` when calling `delete_billing_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'billing_rule_token' in params:
            path_params['billing_rule_token'] = params['billing_rule_token']  # noqa: E501

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
            '/billing_rules/{billing_rule_token}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BillingRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_billing_rule(self, billing_rule_token, **kwargs):  # noqa: E501
        """get_billing_rule  # noqa: E501

        Return a Billing Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_billing_rule(billing_rule_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_rule_token: (required)
        :return: BillingRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_billing_rule_with_http_info(billing_rule_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_billing_rule_with_http_info(billing_rule_token, **kwargs)  # noqa: E501
            return data

    def get_billing_rule_with_http_info(self, billing_rule_token, **kwargs):  # noqa: E501
        """get_billing_rule  # noqa: E501

        Return a Billing Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_billing_rule_with_http_info(billing_rule_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_rule_token: (required)
        :return: BillingRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_rule_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_billing_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'billing_rule_token' is set
        if self.api_client.client_side_validation and ('billing_rule_token' not in params or
                                                       params['billing_rule_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `billing_rule_token` when calling `get_billing_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'billing_rule_token' in params:
            path_params['billing_rule_token'] = params['billing_rule_token']  # noqa: E501

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
            '/billing_rules/{billing_rule_token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BillingRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_billing_rules(self, **kwargs):  # noqa: E501
        """get_billing_rules  # noqa: E501

        Returns a list of billing rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_billing_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results to return.
        :param int limit: The amount of results to return. The maximum is 1000.
        :return: BillingRules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_billing_rules_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_billing_rules_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_billing_rules_with_http_info(self, **kwargs):  # noqa: E501
        """get_billing_rules  # noqa: E501

        Returns a list of billing rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_billing_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results to return.
        :param int limit: The amount of results to return. The maximum is 1000.
        :return: BillingRules
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
                    " to method get_billing_rules" % key
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
            '/billing_rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BillingRules',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_billing_rule(self, billing_rule_token, update_billing_rule, **kwargs):  # noqa: E501
        """update_billing_rule  # noqa: E501

        Update a Billing Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_billing_rule(billing_rule_token, update_billing_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_rule_token: (required)
        :param UpdateBillingRule update_billing_rule: (required)
        :return: BillingRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_billing_rule_with_http_info(billing_rule_token, update_billing_rule, **kwargs)  # noqa: E501
        else:
            (data) = self.update_billing_rule_with_http_info(billing_rule_token, update_billing_rule, **kwargs)  # noqa: E501
            return data

    def update_billing_rule_with_http_info(self, billing_rule_token, update_billing_rule, **kwargs):  # noqa: E501
        """update_billing_rule  # noqa: E501

        Update a Billing Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_billing_rule_with_http_info(billing_rule_token, update_billing_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_rule_token: (required)
        :param UpdateBillingRule update_billing_rule: (required)
        :return: BillingRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_rule_token', 'update_billing_rule']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_billing_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'billing_rule_token' is set
        if self.api_client.client_side_validation and ('billing_rule_token' not in params or
                                                       params['billing_rule_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `billing_rule_token` when calling `update_billing_rule`")  # noqa: E501
        # verify the required parameter 'update_billing_rule' is set
        if self.api_client.client_side_validation and ('update_billing_rule' not in params or
                                                       params['update_billing_rule'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `update_billing_rule` when calling `update_billing_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'billing_rule_token' in params:
            path_params['billing_rule_token'] = params['billing_rule_token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_billing_rule' in params:
            body_params = params['update_billing_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/billing_rules/{billing_rule_token}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BillingRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
