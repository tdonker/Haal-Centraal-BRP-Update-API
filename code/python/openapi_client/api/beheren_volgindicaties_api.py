# coding: utf-8

"""
    BRP Update API

    Met deze API kun je opvragen welke door jou gevolgde personen zijn gewijzigd in de BRP. Je kunt je abonneren op een persoon die je wilt volgen, en je kunt opvragen welke personen door jou worden gevolgd. Je kunt deze API gebruiken in combinatie met de BRP bevragen API, bijvoorbeeld om lokale kopiegegevens actueel te houden.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class BeherenVolgindicatiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_volgindicatie(self, burgerservicenummer, **kwargs):  # noqa: E501
        """Raadplegen specifieke volgindicatie  # noqa: E501

        Opvragen van een volgindicatie van een specifieke persoon.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_volgindicatie(burgerservicenummer, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param object burgerservicenummer: Identificerend gegeven van een ingeschreven natuurlijk persoon, als bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: VolgindicatieRaadplegen
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_volgindicatie_with_http_info(burgerservicenummer, **kwargs)  # noqa: E501

    def get_volgindicatie_with_http_info(self, burgerservicenummer, **kwargs):  # noqa: E501
        """Raadplegen specifieke volgindicatie  # noqa: E501

        Opvragen van een volgindicatie van een specifieke persoon.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_volgindicatie_with_http_info(burgerservicenummer, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param object burgerservicenummer: Identificerend gegeven van een ingeschreven natuurlijk persoon, als bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(VolgindicatieRaadplegen, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'burgerservicenummer'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_volgindicatie" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'burgerservicenummer' is set
        if self.api_client.client_side_validation and ('burgerservicenummer' not in local_var_params or  # noqa: E501
                                                        local_var_params['burgerservicenummer'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `burgerservicenummer` when calling `get_volgindicatie`")  # noqa: E501

        if self.api_client.client_side_validation and ('burgerservicenummer' in local_var_params and  # noqa: E501
                                                        len(local_var_params['burgerservicenummer']) > 9):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `burgerservicenummer` when calling `get_volgindicatie`, length must be less than or equal to `9`")  # noqa: E501
        if self.api_client.client_side_validation and ('burgerservicenummer' in local_var_params and  # noqa: E501
                                                        len(local_var_params['burgerservicenummer']) < 9):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `burgerservicenummer` when calling `get_volgindicatie`, length must be greater than or equal to `9`")  # noqa: E501
        if self.api_client.client_side_validation and 'burgerservicenummer' in local_var_params and not re.search(r'^[0-9]*$', local_var_params['burgerservicenummer']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `burgerservicenummer` when calling `get_volgindicatie`, must conform to the pattern `/^[0-9]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'burgerservicenummer' in local_var_params:
            path_params['burgerservicenummer'] = local_var_params['burgerservicenummer']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volgindicaties/{burgerservicenummer}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VolgindicatieRaadplegen',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_volgindicaties(self, **kwargs):  # noqa: E501
        """Raadplegen alle actieve volgindicaties  # noqa: E501

        Opvragen van alle actuele (actieve) volgindicaties van een abonnee. Volgindicaties met een einddatum in het verleden worden niet geleverd.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_volgindicaties(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: VolgindicatieCollectie
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_volgindicaties_with_http_info(**kwargs)  # noqa: E501

    def get_volgindicaties_with_http_info(self, **kwargs):  # noqa: E501
        """Raadplegen alle actieve volgindicaties  # noqa: E501

        Opvragen van alle actuele (actieve) volgindicaties van een abonnee. Volgindicaties met een einddatum in het verleden worden niet geleverd.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_volgindicaties_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(VolgindicatieCollectie, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_volgindicaties" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volgindicaties', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VolgindicatieCollectie',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upsert_volgindicatie(self, burgerservicenummer, **kwargs):  # noqa: E501
        """Toevoegen, wijzigen of beëindigen volgindicatie  # noqa: E501

        Toevoegen, wijzigen of beëindigen van een volgindicatie van een specifieke persoon. Wanneer er nog geen volgindicatie is op deze persoon wordt de volgindicatie toegevoegd. Wanneer er al een volgindicatie is op deze persoon, wordt de volgindicatie gewijzigd.  De einddatum op een volgindicatie kan worden verwijderd (leeg gemaakt) door een leeg object { } te sturen in de request body.  Een volgindicatie kan worden beëindigd door het sturen van einddatum gelijk aan de datum van gisteren.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_volgindicatie(burgerservicenummer, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param object burgerservicenummer: Identificerend gegeven van een ingeschreven natuurlijk persoon, als bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer. (required)
        :param Volgindicatie volgindicatie:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: VolgindicatieRaadplegen
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upsert_volgindicatie_with_http_info(burgerservicenummer, **kwargs)  # noqa: E501

    def upsert_volgindicatie_with_http_info(self, burgerservicenummer, **kwargs):  # noqa: E501
        """Toevoegen, wijzigen of beëindigen volgindicatie  # noqa: E501

        Toevoegen, wijzigen of beëindigen van een volgindicatie van een specifieke persoon. Wanneer er nog geen volgindicatie is op deze persoon wordt de volgindicatie toegevoegd. Wanneer er al een volgindicatie is op deze persoon, wordt de volgindicatie gewijzigd.  De einddatum op een volgindicatie kan worden verwijderd (leeg gemaakt) door een leeg object { } te sturen in de request body.  Een volgindicatie kan worden beëindigd door het sturen van einddatum gelijk aan de datum van gisteren.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_volgindicatie_with_http_info(burgerservicenummer, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param object burgerservicenummer: Identificerend gegeven van een ingeschreven natuurlijk persoon, als bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer. (required)
        :param Volgindicatie volgindicatie:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(VolgindicatieRaadplegen, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'burgerservicenummer',
            'volgindicatie'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_volgindicatie" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'burgerservicenummer' is set
        if self.api_client.client_side_validation and ('burgerservicenummer' not in local_var_params or  # noqa: E501
                                                        local_var_params['burgerservicenummer'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `burgerservicenummer` when calling `upsert_volgindicatie`")  # noqa: E501

        if self.api_client.client_side_validation and ('burgerservicenummer' in local_var_params and  # noqa: E501
                                                        len(local_var_params['burgerservicenummer']) > 9):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `burgerservicenummer` when calling `upsert_volgindicatie`, length must be less than or equal to `9`")  # noqa: E501
        if self.api_client.client_side_validation and ('burgerservicenummer' in local_var_params and  # noqa: E501
                                                        len(local_var_params['burgerservicenummer']) < 9):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `burgerservicenummer` when calling `upsert_volgindicatie`, length must be greater than or equal to `9`")  # noqa: E501
        if self.api_client.client_side_validation and 'burgerservicenummer' in local_var_params and not re.search(r'^[0-9]*$', local_var_params['burgerservicenummer']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `burgerservicenummer` when calling `upsert_volgindicatie`, must conform to the pattern `/^[0-9]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'burgerservicenummer' in local_var_params:
            path_params['burgerservicenummer'] = local_var_params['burgerservicenummer']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'volgindicatie' in local_var_params:
            body_params = local_var_params['volgindicatie']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/hal+json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volgindicaties/{burgerservicenummer}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VolgindicatieRaadplegen',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)