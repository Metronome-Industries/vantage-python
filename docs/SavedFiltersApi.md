# vantage.SavedFiltersApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saved_filter**](SavedFiltersApi.md#create_saved_filter) | **POST** /saved_filters | 
[**delete_saved_filter**](SavedFiltersApi.md#delete_saved_filter) | **DELETE** /saved_filters/{saved_filter_token} | 
[**get_saved_filter**](SavedFiltersApi.md#get_saved_filter) | **GET** /saved_filters/{saved_filter_token} | 
[**get_saved_filters**](SavedFiltersApi.md#get_saved_filters) | **GET** /saved_filters | 
[**update_saved_filter**](SavedFiltersApi.md#update_saved_filter) | **PUT** /saved_filters/{saved_filter_token} | 


# **create_saved_filter**
> SavedFilter create_saved_filter(create_saved_filter)



Create a SavedFilter for CostReports.

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
api_instance = vantage.SavedFiltersApi(vantage.ApiClient(configuration))
create_saved_filter = vantage.CreateSavedFilter() # CreateSavedFilter | 

try:
    api_response = api_instance.create_saved_filter(create_saved_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedFiltersApi->create_saved_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_saved_filter** | [**CreateSavedFilter**](CreateSavedFilter.md)|  | 

### Return type

[**SavedFilter**](SavedFilter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saved_filter**
> SavedFilter delete_saved_filter(saved_filter_token)



Delete a SavedFilter for CostReports.

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
api_instance = vantage.SavedFiltersApi(vantage.ApiClient(configuration))
saved_filter_token = 'saved_filter_token_example' # str | 

try:
    api_response = api_instance.delete_saved_filter(saved_filter_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedFiltersApi->delete_saved_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saved_filter_token** | **str**|  | 

### Return type

[**SavedFilter**](SavedFilter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_filter**
> SavedFilter get_saved_filter(saved_filter_token)



Return a specific SavedFilter.

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
api_instance = vantage.SavedFiltersApi(vantage.ApiClient(configuration))
saved_filter_token = 'saved_filter_token_example' # str | 

try:
    api_response = api_instance.get_saved_filter(saved_filter_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedFiltersApi->get_saved_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saved_filter_token** | **str**|  | 

### Return type

[**SavedFilter**](SavedFilter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_filters**
> SavedFilters get_saved_filters(page=page, limit=limit)



Return all SavedFilters that can be applied to a CostReport.

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
api_instance = vantage.SavedFiltersApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_saved_filters(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedFiltersApi->get_saved_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**SavedFilters**](SavedFilters.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saved_filter**
> SavedFilter update_saved_filter(saved_filter_token, update_saved_filter)



Update a SavedFilter for CostReports.

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
api_instance = vantage.SavedFiltersApi(vantage.ApiClient(configuration))
saved_filter_token = 'saved_filter_token_example' # str | 
update_saved_filter = vantage.UpdateSavedFilter() # UpdateSavedFilter | 

try:
    api_response = api_instance.update_saved_filter(saved_filter_token, update_saved_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedFiltersApi->update_saved_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saved_filter_token** | **str**|  | 
 **update_saved_filter** | [**UpdateSavedFilter**](UpdateSavedFilter.md)|  | 

### Return type

[**SavedFilter**](SavedFilter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

