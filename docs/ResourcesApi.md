# vantage.ResourcesApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_resources**](ResourcesApi.md#get_report_resources) | **GET** /resources | 
[**get_resource**](ResourcesApi.md#get_resource) | **GET** /resources/{resource_token} | 


# **get_report_resources**
> Resources get_report_resources(resource_report_token=resource_report_token, filter=filter, workspace_token=workspace_token, include_cost=include_cost)



Return Resources contained in a ResourceReport

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
api_instance = vantage.ResourcesApi(vantage.ApiClient(configuration))
resource_report_token = 'resource_report_token_example' # str | The ResourceReport token. (optional)
filter = 'filter_example' # str | The filter query language to apply to the Resources. Additional documentation available at https://docs.vantage.sh/vql. (optional)
workspace_token = 'workspace_token_example' # str | The Workspace in which the Resources are located. (optional)
include_cost = true # bool | Include cost information in the response. (optional)

try:
    api_response = api_instance.get_report_resources(resource_report_token=resource_report_token, filter=filter, workspace_token=workspace_token, include_cost=include_cost)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_report_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_report_token** | **str**| The ResourceReport token. | [optional] 
 **filter** | **str**| The filter query language to apply to the Resources. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 
 **workspace_token** | **str**| The Workspace in which the Resources are located. | [optional] 
 **include_cost** | **bool**| Include cost information in the response. | [optional] 

### Return type

[**Resources**](Resources.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource**
> Resource get_resource(resource_token, include_cost=include_cost)



Return a single Resource

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
api_instance = vantage.ResourcesApi(vantage.ApiClient(configuration))
resource_token = 'resource_token_example' # str | 
include_cost = true # bool | Include cost information in the response. (optional)

try:
    api_response = api_instance.get_resource(resource_token, include_cost=include_cost)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_token** | **str**|  | 
 **include_cost** | **bool**| Include cost information in the response. | [optional] 

### Return type

[**Resource**](Resource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

