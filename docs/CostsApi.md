# vantage.CostsApi

All URIs are relative to *https://api.vantage.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_costs**](CostsApi.md#get_costs) | **GET** /v1/reports/{report_id}/costs | 
[**get_report**](CostsApi.md#get_report) | **GET** /v1/reports/{report_id} | 
[**get_reports**](CostsApi.md#get_reports) | **GET** /v1/reports | 


# **get_costs**
> Costs get_costs(report_id, start_date=start_date, end_date=end_date, page=page, limit=limit)



Return available Costs for the specified Cost Report and optional time period. If no time period is specified it will return all available costs for the report.

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
api_instance = vantage.CostsApi(vantage.ApiClient(configuration))
report_id = 'report_id_example' # str | 
start_date = 'start_date_example' # str | Query costs by the first date you would like to filter from. ISO 8601 Formatted - 2021-07-15 or 2021-07-15T19:20:48+00:00. (optional)
end_date = 'end_date_example' # str | Query costs by the last date you would like to filter to. ISO 8601 Formatted - 2021-07-15 or 2021-07-15T19:20:48+00:00. (optional)
page = 2 # int | The page of results to return. (optional)
limit = 500 # int | The amount of results to return. The maximum is 1000 (optional)

try:
    api_response = api_instance.get_costs(report_id, start_date=start_date, end_date=end_date, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->get_costs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **start_date** | **str**| Query costs by the first date you would like to filter from. ISO 8601 Formatted - 2021-07-15 or 2021-07-15T19:20:48+00:00. | [optional] 
 **end_date** | **str**| Query costs by the last date you would like to filter to. ISO 8601 Formatted - 2021-07-15 or 2021-07-15T19:20:48+00:00. | [optional] 
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000 | [optional] 

### Return type

[**Costs**](Costs.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> Report get_report(report_id)



Return a Cost Report.

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
api_instance = vantage.CostsApi(vantage.ApiClient(configuration))
report_id = 'report_id_example' # str | 

try:
    api_response = api_instance.get_report(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

### Return type

[**Report**](Report.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports**
> Reports get_reports(page=page, limit=limit)



Return all Cost Reports.

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
api_instance = vantage.CostsApi(vantage.ApiClient(configuration))
page = 2 # int | The page of results to return. (optional)
limit = 500 # int | The amount of results to return. The maximum is 1000 (optional)

try:
    api_response = api_instance.get_reports(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->get_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000 | [optional] 

### Return type

[**Reports**](Reports.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

