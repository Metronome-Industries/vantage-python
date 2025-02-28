# vantage.TagsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tag_values**](TagsApi.md#get_tag_values) | **GET** /tags/{key}/values | 
[**get_tags**](TagsApi.md#get_tags) | **GET** /tags | 
[**update_tag**](TagsApi.md#update_tag) | **PUT** /tags | 


# **get_tag_values**
> TagValues get_tag_values(key, providers=providers, sort_direction=sort_direction, search_query=search_query, page=page, limit=limit)



Returns corresponding TagValues for a given Tag.

### Example
```python
from __future__ import print_function
import time
import vantage
from vantage.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = vantage.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = vantage.TagsApi(vantage.ApiClient(configuration))
key = 'key_example' # str | The key of the Tag for which you would like to retrieve TagValues.
providers = ['providers_example'] # list[str] | An array of providers to scope TagValues by. (optional)
sort_direction = 'asc' # str | The direction in which to sort the TagValues. Defaults to 'asc'. (optional) (default to asc)
search_query = 'search_query_example' # str | A search query to filter TagValues by the value name. (optional)
page = 1 # int | The page of results to return. (optional) (default to 1)
limit = 100 # int | The number of results to return per page. Defaults to 100. The maximum is 1000. (optional) (default to 100)

try:
    api_response = api_instance.get_tag_values(key, providers=providers, sort_direction=sort_direction, search_query=search_query, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the Tag for which you would like to retrieve TagValues. | 
 **providers** | [**list[str]**](str.md)| An array of providers to scope TagValues by. | [optional] 
 **sort_direction** | **str**| The direction in which to sort the TagValues. Defaults to &#39;asc&#39;. | [optional] [default to asc]
 **search_query** | **str**| A search query to filter TagValues by the value name. | [optional] 
 **page** | **int**| The page of results to return. | [optional] [default to 1]
 **limit** | **int**| The number of results to return per page. Defaults to 100. The maximum is 1000. | [optional] [default to 100]

### Return type

[**TagValues**](TagValues.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> Tags get_tags(providers=providers, search_query=search_query, sort_direction=sort_direction, page=page, limit=limit)



Return all Tags that the current API token has access to.

### Example
```python
from __future__ import print_function
import time
import vantage
from vantage.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = vantage.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = vantage.TagsApi(vantage.ApiClient(configuration))
providers = ['providers_example'] # list[str] | An array of providers to scope Tags by. (optional)
search_query = 'search_query_example' # str | A search query to filter Tags by tag key. (optional)
sort_direction = 'sort_direction_example' # str | The direction in which you would like to sort the data by. Defaults to 'asc'. (optional)
page = 1 # int | The page of results to return. (optional) (default to 1)
limit = 100 # int | The number of results to return per page. Defaults to 100. The maximum is 1000. (optional) (default to 100)

try:
    api_response = api_instance.get_tags(providers=providers, search_query=search_query, sort_direction=sort_direction, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers** | [**list[str]**](str.md)| An array of providers to scope Tags by. | [optional] 
 **search_query** | **str**| A search query to filter Tags by tag key. | [optional] 
 **sort_direction** | **str**| The direction in which you would like to sort the data by. Defaults to &#39;asc&#39;. | [optional] 
 **page** | **int**| The page of results to return. | [optional] [default to 1]
 **limit** | **int**| The number of results to return per page. Defaults to 100. The maximum is 1000. | [optional] [default to 100]

### Return type

[**Tags**](Tags.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> Tag update_tag(update_tag)



Updates an existing Tag.

### Example
```python
from __future__ import print_function
import time
import vantage
from vantage.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = vantage.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = vantage.TagsApi(vantage.ApiClient(configuration))
update_tag = vantage.UpdateTag() # UpdateTag | 

try:
    api_response = api_instance.update_tag(update_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tag** | [**UpdateTag**](UpdateTag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

