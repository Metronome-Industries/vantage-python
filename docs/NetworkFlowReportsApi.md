# vantage.NetworkFlowReportsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_flow_report**](NetworkFlowReportsApi.md#create_network_flow_report) | **POST** /network_flow_reports | 
[**delete_network_flow_report**](NetworkFlowReportsApi.md#delete_network_flow_report) | **DELETE** /network_flow_reports/{network_flow_report_token} | 
[**get_network_flow_report**](NetworkFlowReportsApi.md#get_network_flow_report) | **GET** /network_flow_reports/{network_flow_report_token} | 
[**get_network_flow_reports**](NetworkFlowReportsApi.md#get_network_flow_reports) | **GET** /network_flow_reports | 
[**update_network_flow_report**](NetworkFlowReportsApi.md#update_network_flow_report) | **PUT** /network_flow_reports/{network_flow_report_token} | 


# **create_network_flow_report**
> NetworkFlowReport create_network_flow_report(create_network_flow_report)



Create a NetworkFlowReport.

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
api_instance = vantage.NetworkFlowReportsApi(vantage.ApiClient(configuration))
create_network_flow_report = vantage.CreateNetworkFlowReport() # CreateNetworkFlowReport | 

try:
    api_response = api_instance.create_network_flow_report(create_network_flow_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkFlowReportsApi->create_network_flow_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_network_flow_report** | [**CreateNetworkFlowReport**](CreateNetworkFlowReport.md)|  | 

### Return type

[**NetworkFlowReport**](NetworkFlowReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_flow_report**
> NetworkFlowReport delete_network_flow_report(network_flow_report_token)



Delete a NetworkFlowReport.

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
api_instance = vantage.NetworkFlowReportsApi(vantage.ApiClient(configuration))
network_flow_report_token = 'network_flow_report_token_example' # str | 

try:
    api_response = api_instance.delete_network_flow_report(network_flow_report_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkFlowReportsApi->delete_network_flow_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_flow_report_token** | **str**|  | 

### Return type

[**NetworkFlowReport**](NetworkFlowReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_flow_report**
> NetworkFlowReport get_network_flow_report(network_flow_report_token)



Return a NetworkFlowReport.

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
api_instance = vantage.NetworkFlowReportsApi(vantage.ApiClient(configuration))
network_flow_report_token = 'network_flow_report_token_example' # str | 

try:
    api_response = api_instance.get_network_flow_report(network_flow_report_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkFlowReportsApi->get_network_flow_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_flow_report_token** | **str**|  | 

### Return type

[**NetworkFlowReport**](NetworkFlowReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_flow_reports**
> NetworkFlowReports get_network_flow_reports(page=page, limit=limit)



Return all NetworkFlowReports.

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
api_instance = vantage.NetworkFlowReportsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_network_flow_reports(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkFlowReportsApi->get_network_flow_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**NetworkFlowReports**](NetworkFlowReports.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_flow_report**
> NetworkFlowReport update_network_flow_report(network_flow_report_token, update_network_flow_report)



Update a NetworkFlowReport.

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
api_instance = vantage.NetworkFlowReportsApi(vantage.ApiClient(configuration))
network_flow_report_token = 'network_flow_report_token_example' # str | 
update_network_flow_report = vantage.UpdateNetworkFlowReport() # UpdateNetworkFlowReport | 

try:
    api_response = api_instance.update_network_flow_report(network_flow_report_token, update_network_flow_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkFlowReportsApi->update_network_flow_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_flow_report_token** | **str**|  | 
 **update_network_flow_report** | [**UpdateNetworkFlowReport**](UpdateNetworkFlowReport.md)|  | 

### Return type

[**NetworkFlowReport**](NetworkFlowReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

