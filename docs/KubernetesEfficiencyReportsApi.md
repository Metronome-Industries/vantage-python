# vantage.KubernetesEfficiencyReportsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kubernetes_efficiency_report**](KubernetesEfficiencyReportsApi.md#create_kubernetes_efficiency_report) | **POST** /kubernetes_efficiency_reports | 
[**delete_kubernetes_efficiency_report**](KubernetesEfficiencyReportsApi.md#delete_kubernetes_efficiency_report) | **DELETE** /kubernetes_efficiency_reports/{kubernetes_efficiency_report_token} | 
[**get_kubernetes_efficiency_report**](KubernetesEfficiencyReportsApi.md#get_kubernetes_efficiency_report) | **GET** /kubernetes_efficiency_reports/{kubernetes_efficiency_report_token} | 
[**get_kubernetes_efficiency_reports**](KubernetesEfficiencyReportsApi.md#get_kubernetes_efficiency_reports) | **GET** /kubernetes_efficiency_reports | 
[**update_kubernetes_efficiency_report**](KubernetesEfficiencyReportsApi.md#update_kubernetes_efficiency_report) | **PUT** /kubernetes_efficiency_reports/{kubernetes_efficiency_report_token} | 


# **create_kubernetes_efficiency_report**
> KubernetesEfficiencyReport create_kubernetes_efficiency_report(create_kubernetes_efficiency_report)



Create a KubernetesEfficiencyReport.

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
api_instance = vantage.KubernetesEfficiencyReportsApi(vantage.ApiClient(configuration))
create_kubernetes_efficiency_report = vantage.CreateKubernetesEfficiencyReport() # CreateKubernetesEfficiencyReport | 

try:
    api_response = api_instance.create_kubernetes_efficiency_report(create_kubernetes_efficiency_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KubernetesEfficiencyReportsApi->create_kubernetes_efficiency_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_kubernetes_efficiency_report** | [**CreateKubernetesEfficiencyReport**](CreateKubernetesEfficiencyReport.md)|  | 

### Return type

[**KubernetesEfficiencyReport**](KubernetesEfficiencyReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kubernetes_efficiency_report**
> KubernetesEfficiencyReport delete_kubernetes_efficiency_report(kubernetes_efficiency_report_token)



Delete a KubernetesEfficiencyReport.

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
api_instance = vantage.KubernetesEfficiencyReportsApi(vantage.ApiClient(configuration))
kubernetes_efficiency_report_token = 'kubernetes_efficiency_report_token_example' # str | 

try:
    api_response = api_instance.delete_kubernetes_efficiency_report(kubernetes_efficiency_report_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KubernetesEfficiencyReportsApi->delete_kubernetes_efficiency_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_efficiency_report_token** | **str**|  | 

### Return type

[**KubernetesEfficiencyReport**](KubernetesEfficiencyReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_efficiency_report**
> KubernetesEfficiencyReport get_kubernetes_efficiency_report(kubernetes_efficiency_report_token)



Return a KubernetesEfficiencyReport.

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
api_instance = vantage.KubernetesEfficiencyReportsApi(vantage.ApiClient(configuration))
kubernetes_efficiency_report_token = 'kubernetes_efficiency_report_token_example' # str | 

try:
    api_response = api_instance.get_kubernetes_efficiency_report(kubernetes_efficiency_report_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KubernetesEfficiencyReportsApi->get_kubernetes_efficiency_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_efficiency_report_token** | **str**|  | 

### Return type

[**KubernetesEfficiencyReport**](KubernetesEfficiencyReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_efficiency_reports**
> KubernetesEfficiencyReports get_kubernetes_efficiency_reports(page=page, limit=limit)



Return all KubernetesEfficiencyReports.

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
api_instance = vantage.KubernetesEfficiencyReportsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_kubernetes_efficiency_reports(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KubernetesEfficiencyReportsApi->get_kubernetes_efficiency_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**KubernetesEfficiencyReports**](KubernetesEfficiencyReports.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_efficiency_report**
> KubernetesEfficiencyReport update_kubernetes_efficiency_report(kubernetes_efficiency_report_token, update_kubernetes_efficiency_report)



Update a KubernetesEfficiencyReport.

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
api_instance = vantage.KubernetesEfficiencyReportsApi(vantage.ApiClient(configuration))
kubernetes_efficiency_report_token = 'kubernetes_efficiency_report_token_example' # str | 
update_kubernetes_efficiency_report = vantage.UpdateKubernetesEfficiencyReport() # UpdateKubernetesEfficiencyReport | 

try:
    api_response = api_instance.update_kubernetes_efficiency_report(kubernetes_efficiency_report_token, update_kubernetes_efficiency_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KubernetesEfficiencyReportsApi->update_kubernetes_efficiency_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_efficiency_report_token** | **str**|  | 
 **update_kubernetes_efficiency_report** | [**UpdateKubernetesEfficiencyReport**](UpdateKubernetesEfficiencyReport.md)|  | 

### Return type

[**KubernetesEfficiencyReport**](KubernetesEfficiencyReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

