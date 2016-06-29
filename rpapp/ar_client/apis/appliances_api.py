# coding: utf-8

"""
    Appliance Registry API

    Store appliances with the Appliance Registry API.

    OpenAPI spec version: 0.1.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AppliancesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def appliances_get(self, **kwargs):
        """
        Get the list of all the appliances registered.
        Get the list of all the appliances registered. No authentification is required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.appliances_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Appliance]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appliances_get" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/appliances/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Appliance]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def appliances_name_delete(self, name, **kwargs):
        """
        Delete an already existing appliance.
        Delete an already existing appliance. Authentification is required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.appliances_name_delete(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Name of the appliance (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appliances_name_delete" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `appliances_name_delete`")


        resource_path = '/appliances/{name}/'.replace('{format}', 'json')
        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'basic']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def appliances_name_get(self, name, **kwargs):
        """
        Get a single appliance.
        Get a single appliance. Authentification is not required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.appliances_name_get(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Name of the appliance (required)
        :return: Appliance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appliances_name_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `appliances_name_get`")


        resource_path = '/appliances/{name}/'.replace('{format}', 'json')
        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Appliance',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def appliances_name_patch(self, name, data, **kwargs):
        """
        Modify an already existing appliance.
        Modify an already existing appliance. Authentification is required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.appliances_name_patch(name, data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Name of the appliance (required)
        :param AppliancePatch data: Appliance (required)
        :return: Appliance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'data']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appliances_name_patch" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `appliances_name_patch`")
        # verify the required parameter 'data' is set
        if ('data' not in params) or (params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `appliances_name_patch`")


        resource_path = '/appliances/{name}/'.replace('{format}', 'json')
        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'basic']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Appliance',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def appliances_name_put(self, name, data, **kwargs):
        """
        Redefine an already existing appliance.
        Redefine an already existing appliance. Authentification is required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.appliances_name_put(name, data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Name of the appliance (required)
        :param AppliancePost data: Appliance (required)
        :return: Appliance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'data']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appliances_name_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `appliances_name_put`")
        # verify the required parameter 'data' is set
        if ('data' not in params) or (params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `appliances_name_put`")


        resource_path = '/appliances/{name}/'.replace('{format}', 'json')
        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'basic']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Appliance',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def appliances_post(self, data, **kwargs):
        """
        Add a new appliances.
        Add a new appliances. Authentification is required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.appliances_post(data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AppliancePost data: Appliance (required)
        :return: Appliance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method appliances_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'data' is set
        if ('data' not in params) or (params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `appliances_post`")


        resource_path = '/appliances/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'basic']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Appliance',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
