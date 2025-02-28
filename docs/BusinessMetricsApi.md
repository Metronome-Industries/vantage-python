# vantage.BusinessMetricsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_metric**](BusinessMetricsApi.md#create_business_metric) | **POST** /business_metrics | 
[**delete_business_metric**](BusinessMetricsApi.md#delete_business_metric) | **DELETE** /business_metrics/{business_metric_token} | 
[**get_business_metric**](BusinessMetricsApi.md#get_business_metric) | **GET** /business_metrics/{business_metric_token} | 
[**get_business_metric_values**](BusinessMetricsApi.md#get_business_metric_values) | **GET** /business_metrics/{business_metric_token}/values | 
[**get_business_metrics**](BusinessMetricsApi.md#get_business_metrics) | **GET** /business_metrics | 
[**update_business_metric**](BusinessMetricsApi.md#update_business_metric) | **PUT** /business_metrics/{business_metric_token} | 
[**update_business_metric_values_csv**](BusinessMetricsApi.md#update_business_metric_values_csv) | **PUT** /business_metrics/{business_metric_token}/values.csv | 


# **create_business_metric**
> BusinessMetric create_business_metric(create_business_metric)



Create a new BusinessMetric.

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
api_instance = vantage.BusinessMetricsApi(vantage.ApiClient(configuration))
create_business_metric = vantage.CreateBusinessMetric() # CreateBusinessMetric | 

try:
    api_response = api_instance.create_business_metric(create_business_metric)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessMetricsApi->create_business_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_business_metric** | [**CreateBusinessMetric**](CreateBusinessMetric.md)|  | 

### Return type

[**BusinessMetric**](BusinessMetric.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_business_metric**
> BusinessMetric delete_business_metric(business_metric_token)



Deletes an existing BusinessMetric.

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
api_instance = vantage.BusinessMetricsApi(vantage.ApiClient(configuration))
business_metric_token = 'business_metric_token_example' # str | 

try:
    api_response = api_instance.delete_business_metric(business_metric_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessMetricsApi->delete_business_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metric_token** | **str**|  | 

### Return type

[**BusinessMetric**](BusinessMetric.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_metric**
> BusinessMetric get_business_metric(business_metric_token)



Return a BusinessMetric.

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
api_instance = vantage.BusinessMetricsApi(vantage.ApiClient(configuration))
business_metric_token = 'business_metric_token_example' # str | 

try:
    api_response = api_instance.get_business_metric(business_metric_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessMetricsApi->get_business_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metric_token** | **str**|  | 

### Return type

[**BusinessMetric**](BusinessMetric.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_metric_values**
> BusinessMetricValues get_business_metric_values(business_metric_token, page=page, limit=limit, start_date=start_date)



Return values of a BusinessMetric

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
api_instance = vantage.BusinessMetricsApi(vantage.ApiClient(configuration))
business_metric_token = 'business_metric_token_example' # str | 
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)
start_date = '2013-10-20' # date | Query BusinessMetrics by the first date you would like to filter from. ISO 8601 Formatted - 2021-07-15 (optional)

try:
    api_response = api_instance.get_business_metric_values(business_metric_token, page=page, limit=limit, start_date=start_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessMetricsApi->get_business_metric_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metric_token** | **str**|  | 
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 
 **start_date** | **date**| Query BusinessMetrics by the first date you would like to filter from. ISO 8601 Formatted - 2021-07-15 | [optional] 

### Return type

[**BusinessMetricValues**](BusinessMetricValues.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_metrics**
> BusinessMetrics get_business_metrics(page=page, limit=limit)



Return all BusinessMetrics that the current API token has access to.

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
api_instance = vantage.BusinessMetricsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_business_metrics(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessMetricsApi->get_business_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**BusinessMetrics**](BusinessMetrics.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_metric**
> BusinessMetric update_business_metric(business_metric_token, update_business_metric)



Updates an existing BusinessMetric.

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
api_instance = vantage.BusinessMetricsApi(vantage.ApiClient(configuration))
business_metric_token = 'business_metric_token_example' # str | 
update_business_metric = vantage.UpdateBusinessMetric() # UpdateBusinessMetric | 

try:
    api_response = api_instance.update_business_metric(business_metric_token, update_business_metric)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessMetricsApi->update_business_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metric_token** | **str**|  | 
 **update_business_metric** | [**UpdateBusinessMetric**](UpdateBusinessMetric.md)|  | 

### Return type

[**BusinessMetric**](BusinessMetric.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_metric_values_csv**
> BusinessMetric update_business_metric_values_csv(csv, business_metric_token)



Updates the values for an existing BusinessMetric from a CSV file.

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
api_instance = vantage.BusinessMetricsApi(vantage.ApiClient(configuration))
csv = '/path/to/file.txt' # file | CSV file containing BusinessMetric dates and amounts
business_metric_token = 'business_metric_token_example' # str | 

try:
    api_response = api_instance.update_business_metric_values_csv(csv, business_metric_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessMetricsApi->update_business_metric_values_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv** | **file**| CSV file containing BusinessMetric dates and amounts | 
 **business_metric_token** | **str**|  | 

### Return type

[**BusinessMetric**](BusinessMetric.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

