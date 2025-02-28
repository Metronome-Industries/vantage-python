# vantage.WorkspacesApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /workspaces | 
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspace_token} | 
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspace_token} | 
[**get_workspaces**](WorkspacesApi.md#get_workspaces) | **GET** /workspaces | 
[**update_workspace**](WorkspacesApi.md#update_workspace) | **PUT** /workspaces/{workspace_token} | 


# **create_workspace**
> Workspace create_workspace(name, enable_currency_conversion=enable_currency_conversion, currency=currency, exchange_rate_date=exchange_rate_date)



Create a workspace

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
api_instance = vantage.WorkspacesApi(vantage.ApiClient(configuration))
name = 'name_example' # str | Name of the workspace.
enable_currency_conversion = true # bool | Enable currency conversion for the workspace. (optional) (default to true)
currency = 'currency_example' # str | Currency code for the workspace. (optional)
exchange_rate_date = 'daily_rate' # str | The date to use for currency conversion. (optional) (default to daily_rate)

try:
    api_response = api_instance.create_workspace(name, enable_currency_conversion=enable_currency_conversion, currency=currency, exchange_rate_date=exchange_rate_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the workspace. | 
 **enable_currency_conversion** | **bool**| Enable currency conversion for the workspace. | [optional] [default to true]
 **currency** | **str**| Currency code for the workspace. | [optional] 
 **exchange_rate_date** | **str**| The date to use for currency conversion. | [optional] [default to daily_rate]

### Return type

[**Workspace**](Workspace.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> Workspace delete_workspace(workspace_token)



Delete a Workspace

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
api_instance = vantage.WorkspacesApi(vantage.ApiClient(configuration))
workspace_token = 'workspace_token_example' # str | 

try:
    api_response = api_instance.delete_workspace(workspace_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_token** | **str**|  | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> Workspace get_workspace(workspace_token)



Return a specific Workspace.

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
api_instance = vantage.WorkspacesApi(vantage.ApiClient(configuration))
workspace_token = 'workspace_token_example' # str | 

try:
    api_response = api_instance.get_workspace(workspace_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_token** | **str**|  | 

### Return type

[**Workspace**](Workspace.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces**
> Workspaces get_workspaces(page=page, limit=limit)



Return all Workspaces that the current API token has access to.

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
api_instance = vantage.WorkspacesApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_workspaces(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**Workspaces**](Workspaces.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> Workspace update_workspace(workspace_token, name=name, enable_currency_conversion=enable_currency_conversion, currency=currency, exchange_rate_date=exchange_rate_date)



Update a workspace

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
api_instance = vantage.WorkspacesApi(vantage.ApiClient(configuration))
workspace_token = 'workspace_token_example' # str | 
name = 'name_example' # str | Name of the workspace. (optional)
enable_currency_conversion = true # bool | Enable currency conversion for the workspace. (optional) (default to true)
currency = 'currency_example' # str | Currency code for the workspace. (optional)
exchange_rate_date = 'daily_rate' # str | The date to use for currency conversion. (optional) (default to daily_rate)

try:
    api_response = api_instance.update_workspace(workspace_token, name=name, enable_currency_conversion=enable_currency_conversion, currency=currency, exchange_rate_date=exchange_rate_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->update_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_token** | **str**|  | 
 **name** | **str**| Name of the workspace. | [optional] 
 **enable_currency_conversion** | **bool**| Enable currency conversion for the workspace. | [optional] [default to true]
 **currency** | **str**| Currency code for the workspace. | [optional] 
 **exchange_rate_date** | **str**| The date to use for currency conversion. | [optional] [default to daily_rate]

### Return type

[**Workspace**](Workspace.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

