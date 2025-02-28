# vantage.FinancialCommitmentReportsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_financial_commitment_report**](FinancialCommitmentReportsApi.md#create_financial_commitment_report) | **POST** /financial_commitment_reports | 
[**delete_financial_commitment_report**](FinancialCommitmentReportsApi.md#delete_financial_commitment_report) | **DELETE** /financial_commitment_reports/{financial_commitment_report_token} | 
[**get_financial_commitment_report**](FinancialCommitmentReportsApi.md#get_financial_commitment_report) | **GET** /financial_commitment_reports/{financial_commitment_report_token} | 
[**get_financial_commitment_reports**](FinancialCommitmentReportsApi.md#get_financial_commitment_reports) | **GET** /financial_commitment_reports | 
[**update_financial_commitment_report**](FinancialCommitmentReportsApi.md#update_financial_commitment_report) | **PUT** /financial_commitment_reports/{financial_commitment_report_token} | 


# **create_financial_commitment_report**
> FinancialCommitmentReport create_financial_commitment_report(create_financial_commitment_report)



Create a FinancialCommitmentReport.

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
api_instance = vantage.FinancialCommitmentReportsApi(vantage.ApiClient(configuration))
create_financial_commitment_report = vantage.CreateFinancialCommitmentReport() # CreateFinancialCommitmentReport | 

try:
    api_response = api_instance.create_financial_commitment_report(create_financial_commitment_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialCommitmentReportsApi->create_financial_commitment_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_financial_commitment_report** | [**CreateFinancialCommitmentReport**](CreateFinancialCommitmentReport.md)|  | 

### Return type

[**FinancialCommitmentReport**](FinancialCommitmentReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_financial_commitment_report**
> FinancialCommitmentReport delete_financial_commitment_report(financial_commitment_report_token)



Delete a FinancialCommitmentReport.

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
api_instance = vantage.FinancialCommitmentReportsApi(vantage.ApiClient(configuration))
financial_commitment_report_token = 'financial_commitment_report_token_example' # str | 

try:
    api_response = api_instance.delete_financial_commitment_report(financial_commitment_report_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialCommitmentReportsApi->delete_financial_commitment_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **financial_commitment_report_token** | **str**|  | 

### Return type

[**FinancialCommitmentReport**](FinancialCommitmentReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_commitment_report**
> FinancialCommitmentReport get_financial_commitment_report(financial_commitment_report_token)



Return a FinancialCommitmentReport.

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
api_instance = vantage.FinancialCommitmentReportsApi(vantage.ApiClient(configuration))
financial_commitment_report_token = 'financial_commitment_report_token_example' # str | 

try:
    api_response = api_instance.get_financial_commitment_report(financial_commitment_report_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialCommitmentReportsApi->get_financial_commitment_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **financial_commitment_report_token** | **str**|  | 

### Return type

[**FinancialCommitmentReport**](FinancialCommitmentReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_commitment_reports**
> FinancialCommitmentReports get_financial_commitment_reports(page=page, limit=limit)



Return all FinancialCommitmentReports.

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
api_instance = vantage.FinancialCommitmentReportsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_financial_commitment_reports(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialCommitmentReportsApi->get_financial_commitment_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**FinancialCommitmentReports**](FinancialCommitmentReports.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_financial_commitment_report**
> FinancialCommitmentReport update_financial_commitment_report(financial_commitment_report_token, update_financial_commitment_report)



Update a FinancialCommitmentReport.

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
api_instance = vantage.FinancialCommitmentReportsApi(vantage.ApiClient(configuration))
financial_commitment_report_token = 'financial_commitment_report_token_example' # str | 
update_financial_commitment_report = vantage.UpdateFinancialCommitmentReport() # UpdateFinancialCommitmentReport | 

try:
    api_response = api_instance.update_financial_commitment_report(financial_commitment_report_token, update_financial_commitment_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialCommitmentReportsApi->update_financial_commitment_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **financial_commitment_report_token** | **str**|  | 
 **update_financial_commitment_report** | [**UpdateFinancialCommitmentReport**](UpdateFinancialCommitmentReport.md)|  | 

### Return type

[**FinancialCommitmentReport**](FinancialCommitmentReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

