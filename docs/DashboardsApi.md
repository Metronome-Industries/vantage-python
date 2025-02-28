# vantage.DashboardsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](DashboardsApi.md#create_dashboard) | **POST** /dashboards | 
[**delete_dashboard**](DashboardsApi.md#delete_dashboard) | **DELETE** /dashboards/{dashboard_token} | 
[**get_dashboard**](DashboardsApi.md#get_dashboard) | **GET** /dashboards/{dashboard_token} | 
[**get_dashboards**](DashboardsApi.md#get_dashboards) | **GET** /dashboards | 
[**update_dashboard**](DashboardsApi.md#update_dashboard) | **PUT** /dashboards/{dashboard_token} | 


# **create_dashboard**
> Dashboard create_dashboard(create_dashboard)



Create a Dashboard.

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
api_instance = vantage.DashboardsApi(vantage.ApiClient(configuration))
create_dashboard = vantage.CreateDashboard() # CreateDashboard | 

try:
    api_response = api_instance.create_dashboard(create_dashboard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->create_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dashboard** | [**CreateDashboard**](CreateDashboard.md)|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> Dashboard delete_dashboard(dashboard_token)



Delete a Dashboard.

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
api_instance = vantage.DashboardsApi(vantage.ApiClient(configuration))
dashboard_token = 'dashboard_token_example' # str | 

try:
    api_response = api_instance.delete_dashboard(dashboard_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->delete_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_token** | **str**|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> Dashboard get_dashboard(dashboard_token)



Return a specific Dashboard.

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
api_instance = vantage.DashboardsApi(vantage.ApiClient(configuration))
dashboard_token = 'dashboard_token_example' # str | 

try:
    api_response = api_instance.get_dashboard(dashboard_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->get_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_token** | **str**|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboards**
> Dashboards get_dashboards(page=page, limit=limit)



Return all Dashboards.

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
api_instance = vantage.DashboardsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_dashboards(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->get_dashboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**Dashboards**](Dashboards.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> Dashboard update_dashboard(dashboard_token, update_dashboard)



Update a Dashboard.

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
api_instance = vantage.DashboardsApi(vantage.ApiClient(configuration))
dashboard_token = 'dashboard_token_example' # str | 
update_dashboard = vantage.UpdateDashboard() # UpdateDashboard | 

try:
    api_response = api_instance.update_dashboard(dashboard_token, update_dashboard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardsApi->update_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_token** | **str**|  | 
 **update_dashboard** | [**UpdateDashboard**](UpdateDashboard.md)|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

