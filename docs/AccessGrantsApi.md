# vantage.AccessGrantsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_grant**](AccessGrantsApi.md#create_access_grant) | **POST** /access_grants | 
[**delete_access_grant**](AccessGrantsApi.md#delete_access_grant) | **DELETE** /access_grants/{access_grant_token} | 
[**get_access_grant**](AccessGrantsApi.md#get_access_grant) | **GET** /access_grants/{access_grant_token} | 
[**get_access_grants**](AccessGrantsApi.md#get_access_grants) | **GET** /access_grants | 
[**update_access_grant**](AccessGrantsApi.md#update_access_grant) | **PUT** /access_grants/{access_grant_token} | 


# **create_access_grant**
> AccessGrant create_access_grant(create_access_grant)



Create an Access Grant.

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
api_instance = vantage.AccessGrantsApi(vantage.ApiClient(configuration))
create_access_grant = vantage.CreateAccessGrant() # CreateAccessGrant | 

try:
    api_response = api_instance.create_access_grant(create_access_grant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessGrantsApi->create_access_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_access_grant** | [**CreateAccessGrant**](CreateAccessGrant.md)|  | 

### Return type

[**AccessGrant**](AccessGrant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_grant**
> AccessGrant delete_access_grant(access_grant_token)



Delete an Access Grant.

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
api_instance = vantage.AccessGrantsApi(vantage.ApiClient(configuration))
access_grant_token = 'access_grant_token_example' # str | 

try:
    api_response = api_instance.delete_access_grant(access_grant_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessGrantsApi->delete_access_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_grant_token** | **str**|  | 

### Return type

[**AccessGrant**](AccessGrant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_grant**
> AccessGrant get_access_grant(access_grant_token)



Return a specific Access Grant.

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
api_instance = vantage.AccessGrantsApi(vantage.ApiClient(configuration))
access_grant_token = 'access_grant_token_example' # str | 

try:
    api_response = api_instance.get_access_grant(access_grant_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessGrantsApi->get_access_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_grant_token** | **str**|  | 

### Return type

[**AccessGrant**](AccessGrant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_grants**
> AccessGrants get_access_grants(page=page, limit=limit)



Return all Access Grants that the current API token has access to.

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
api_instance = vantage.AccessGrantsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_access_grants(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessGrantsApi->get_access_grants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**AccessGrants**](AccessGrants.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_grant**
> AccessGrant update_access_grant(access_grant_token, update_access_grant)



Update an AccessGrant.

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
api_instance = vantage.AccessGrantsApi(vantage.ApiClient(configuration))
access_grant_token = 'access_grant_token_example' # str | 
update_access_grant = vantage.UpdateAccessGrant() # UpdateAccessGrant | 

try:
    api_response = api_instance.update_access_grant(access_grant_token, update_access_grant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessGrantsApi->update_access_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_grant_token** | **str**|  | 
 **update_access_grant** | [**UpdateAccessGrant**](UpdateAccessGrant.md)|  | 

### Return type

[**AccessGrant**](AccessGrant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

