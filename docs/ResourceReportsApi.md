# vantage.ResourceReportsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_report**](ResourceReportsApi.md#create_resource_report) | **POST** /resource_reports | 
[**delete_resource_report**](ResourceReportsApi.md#delete_resource_report) | **DELETE** /resource_reports/{resource_report_token} | 
[**get_resource_report**](ResourceReportsApi.md#get_resource_report) | **GET** /resource_reports/{resource_report_token} | 
[**get_resource_reports**](ResourceReportsApi.md#get_resource_reports) | **GET** /resource_reports | 
[**update_resource_report**](ResourceReportsApi.md#update_resource_report) | **PUT** /resource_reports/{resource_report_token} | 


# **create_resource_report**
> ResourceReport create_resource_report(create_resource_report)



Create a ResourceReport.

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
api_instance = vantage.ResourceReportsApi(vantage.ApiClient(configuration))
create_resource_report = vantage.CreateResourceReport() # CreateResourceReport | 

try:
    api_response = api_instance.create_resource_report(create_resource_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceReportsApi->create_resource_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_resource_report** | [**CreateResourceReport**](CreateResourceReport.md)|  | 

### Return type

[**ResourceReport**](ResourceReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_report**
> ResourceReport delete_resource_report(resource_report_token)



Delete a ResourceReport.

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
api_instance = vantage.ResourceReportsApi(vantage.ApiClient(configuration))
resource_report_token = 'resource_report_token_example' # str | 

try:
    api_response = api_instance.delete_resource_report(resource_report_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceReportsApi->delete_resource_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_report_token** | **str**|  | 

### Return type

[**ResourceReport**](ResourceReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_report**
> ResourceReport get_resource_report(resource_report_token)



Return a ResourceReport.

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
api_instance = vantage.ResourceReportsApi(vantage.ApiClient(configuration))
resource_report_token = 'resource_report_token_example' # str | 

try:
    api_response = api_instance.get_resource_report(resource_report_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceReportsApi->get_resource_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_report_token** | **str**|  | 

### Return type

[**ResourceReport**](ResourceReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_reports**
> ResourceReports get_resource_reports(page=page, limit=limit)



Return all ResourceReports.

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
api_instance = vantage.ResourceReportsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The number of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_resource_reports(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceReportsApi->get_resource_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The number of results to return. The maximum is 1000. | [optional] 

### Return type

[**ResourceReports**](ResourceReports.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_report**
> ResourceReport update_resource_report(resource_report_token, update_resource_report)



Update a ResourceReport.

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
api_instance = vantage.ResourceReportsApi(vantage.ApiClient(configuration))
resource_report_token = 'resource_report_token_example' # str | 
update_resource_report = vantage.UpdateResourceReport() # UpdateResourceReport | 

try:
    api_response = api_instance.update_resource_report(resource_report_token, update_resource_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceReportsApi->update_resource_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_report_token** | **str**|  | 
 **update_resource_report** | [**UpdateResourceReport**](UpdateResourceReport.md)|  | 

### Return type

[**ResourceReport**](ResourceReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

