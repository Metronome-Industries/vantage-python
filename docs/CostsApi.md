# vantage.CostsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cost_report**](CostsApi.md#create_cost_report) | **POST** /cost_reports | 
[**create_dashboard**](CostsApi.md#create_dashboard) | **POST** /dashboards | 
[**delete_cost_report**](CostsApi.md#delete_cost_report) | **DELETE** /cost_reports/{cost_report_token} | 
[**delete_dashboard**](CostsApi.md#delete_dashboard) | **DELETE** /dashboards/{dashboard_token} | 
[**get_cost_report**](CostsApi.md#get_cost_report) | **GET** /cost_reports/{cost_report_token} | 
[**get_cost_reports**](CostsApi.md#get_cost_reports) | **GET** /cost_reports | 
[**get_costs**](CostsApi.md#get_costs) | **GET** /costs | 
[**get_dashboard**](CostsApi.md#get_dashboard) | **GET** /dashboards/{dashboard_token} | 
[**get_dashboards**](CostsApi.md#get_dashboards) | **GET** /dashboards | 
[**get_forecasted_costs**](CostsApi.md#get_forecasted_costs) | **GET** /cost_reports/{cost_report_token}/forecasted_costs | 
[**update_cost_report**](CostsApi.md#update_cost_report) | **PUT** /cost_reports/{cost_report_token} | 
[**update_dashboard**](CostsApi.md#update_dashboard) | **PUT** /dashboards/{dashboard_token} | 


# **create_cost_report**
> CostReport create_cost_report(create_cost_report)



Create a CostReport.

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
create_cost_report = vantage.CreateCostReport() # CreateCostReport | 

try:
    api_response = api_instance.create_cost_report(create_cost_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->create_cost_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cost_report** | [**CreateCostReport**](CreateCostReport.md)|  | 

### Return type

[**CostReport**](CostReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = vantage.CostsApi(vantage.ApiClient(configuration))
create_dashboard = vantage.CreateDashboard() # CreateDashboard | 

try:
    api_response = api_instance.create_dashboard(create_dashboard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->create_dashboard: %s\n" % e)
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

# **delete_cost_report**
> CostReport delete_cost_report(cost_report_token)



Delete a CostReport.

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
cost_report_token = 'cost_report_token_example' # str | 

try:
    api_response = api_instance.delete_cost_report(cost_report_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->delete_cost_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_report_token** | **str**|  | 

### Return type

[**CostReport**](CostReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = vantage.CostsApi(vantage.ApiClient(configuration))
dashboard_token = 'dashboard_token_example' # str | 

try:
    api_response = api_instance.delete_dashboard(dashboard_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->delete_dashboard: %s\n" % e)
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

# **get_cost_report**
> CostReport get_cost_report(cost_report_token)



Return a CostReport.

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
cost_report_token = 'cost_report_token_example' # str | 

try:
    api_response = api_instance.get_cost_report(cost_report_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->get_cost_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_report_token** | **str**|  | 

### Return type

[**CostReport**](CostReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cost_reports**
> CostReports get_cost_reports(page=page, limit=limit, folder_token=folder_token)



Return all CostReports.

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
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)
folder_token = 'folder_token_example' # str | The token for the Folder you would like to fetch Reports from. (optional)

try:
    api_response = api_instance.get_cost_reports(page=page, limit=limit, folder_token=folder_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->get_cost_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 
 **folder_token** | **str**| The token for the Folder you would like to fetch Reports from. | [optional] 

### Return type

[**CostReports**](CostReports.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_costs**
> Costs get_costs(cost_report_token, start_date=start_date, end_date=end_date, groupings=groupings, order=order, limit=limit, date_bin=date_bin, settings_include_credits=settings_include_credits, settings_include_refunds=settings_include_refunds, settings_include_discounts=settings_include_discounts, settings_include_tax=settings_include_tax, settings_amortize=settings_amortize, settings_unallocated=settings_unallocated, settings_aggregate_by=settings_aggregate_by)



Return all Costs for a CostReport.

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
cost_report_token = 'cost_report_token_example' # str | The CostReport token.
start_date = 'start_date_example' # str | First date you would like to filter costs from. ISO 8601 formatted. (optional)
end_date = 'end_date_example' # str | Last date you would like to filter costs to. ISO 8601 formatted. (optional)
groupings = ['groupings_example'] # list[str] | Group the results by specific field(s). Defaults to provider, service, account_id. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:<tag_value>. If providing multiple groupings, join as comma separated values: groupings=provider,service,region (optional)
order = 'desc' # str | Whether to order costs by date in an ascending or descending manner. (optional) (default to desc)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)
date_bin = 'date_bin_example' # str | The date bin of the costs. Defaults to the report's default or day. (optional)
settings_include_credits = false # bool | Results will include credits. (optional) (default to false)
settings_include_refunds = false # bool | Results will include refunds. (optional) (default to false)
settings_include_discounts = true # bool | Results will include discounts. (optional) (default to true)
settings_include_tax = true # bool | Results will include tax. (optional) (default to true)
settings_amortize = true # bool | Results will amortize. (optional) (default to true)
settings_unallocated = false # bool | Results will show unallocated costs. (optional) (default to false)
settings_aggregate_by = 'cost' # str | Results will aggregate by cost or usage. (optional) (default to cost)

try:
    api_response = api_instance.get_costs(cost_report_token, start_date=start_date, end_date=end_date, groupings=groupings, order=order, limit=limit, date_bin=date_bin, settings_include_credits=settings_include_credits, settings_include_refunds=settings_include_refunds, settings_include_discounts=settings_include_discounts, settings_include_tax=settings_include_tax, settings_amortize=settings_amortize, settings_unallocated=settings_unallocated, settings_aggregate_by=settings_aggregate_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->get_costs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_report_token** | **str**| The CostReport token. | 
 **start_date** | **str**| First date you would like to filter costs from. ISO 8601 formatted. | [optional] 
 **end_date** | **str**| Last date you would like to filter costs to. ISO 8601 formatted. | [optional] 
 **groupings** | [**list[str]**](str.md)| Group the results by specific field(s). Defaults to provider, service, account_id. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:&lt;tag_value&gt;. If providing multiple groupings, join as comma separated values: groupings&#x3D;provider,service,region | [optional] 
 **order** | **str**| Whether to order costs by date in an ascending or descending manner. | [optional] [default to desc]
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 
 **date_bin** | **str**| The date bin of the costs. Defaults to the report&#39;s default or day. | [optional] 
 **settings_include_credits** | **bool**| Results will include credits. | [optional] [default to false]
 **settings_include_refunds** | **bool**| Results will include refunds. | [optional] [default to false]
 **settings_include_discounts** | **bool**| Results will include discounts. | [optional] [default to true]
 **settings_include_tax** | **bool**| Results will include tax. | [optional] [default to true]
 **settings_amortize** | **bool**| Results will amortize. | [optional] [default to true]
 **settings_unallocated** | **bool**| Results will show unallocated costs. | [optional] [default to false]
 **settings_aggregate_by** | **str**| Results will aggregate by cost or usage. | [optional] [default to cost]

### Return type

[**Costs**](Costs.md)

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
api_instance = vantage.CostsApi(vantage.ApiClient(configuration))
dashboard_token = 'dashboard_token_example' # str | 

try:
    api_response = api_instance.get_dashboard(dashboard_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->get_dashboard: %s\n" % e)
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
api_instance = vantage.CostsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_dashboards(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->get_dashboards: %s\n" % e)
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

# **get_forecasted_costs**
> CostReports get_forecasted_costs(cost_report_token, start_date=start_date, end_date=end_date, provider=provider, service=service, limit=limit)



Return all ForecastedCosts.

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
cost_report_token = 'cost_report_token_example' # str | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | First date you would like to filter forecasted costs from. ISO 8601 formatted. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Last date you would like to filter forecasted costs from. ISO 8601 formatted. (optional)
provider = 'provider_example' # str | Limit the forecasted costs to a specific provider. 'all' is accepted to filter to overall forecast. (optional)
service = 'service_example' # str | Limit the forecasted costs to a specific service. 'all' is accepted to filter to overall forecast. e.g. 'Amazon ElastiCache'. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_forecasted_costs(cost_report_token, start_date=start_date, end_date=end_date, provider=provider, service=service, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->get_forecasted_costs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_report_token** | **str**|  | 
 **start_date** | **datetime**| First date you would like to filter forecasted costs from. ISO 8601 formatted. | [optional] 
 **end_date** | **datetime**| Last date you would like to filter forecasted costs from. ISO 8601 formatted. | [optional] 
 **provider** | **str**| Limit the forecasted costs to a specific provider. &#39;all&#39; is accepted to filter to overall forecast. | [optional] 
 **service** | **str**| Limit the forecasted costs to a specific service. &#39;all&#39; is accepted to filter to overall forecast. e.g. &#39;Amazon ElastiCache&#39;. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**CostReports**](CostReports.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cost_report**
> CostReport update_cost_report(cost_report_token, update_cost_report)



Update a CostReport.

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
cost_report_token = 'cost_report_token_example' # str | 
update_cost_report = vantage.UpdateCostReport() # UpdateCostReport | 

try:
    api_response = api_instance.update_cost_report(cost_report_token, update_cost_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->update_cost_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_report_token** | **str**|  | 
 **update_cost_report** | [**UpdateCostReport**](UpdateCostReport.md)|  | 

### Return type

[**CostReport**](CostReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
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
api_instance = vantage.CostsApi(vantage.ApiClient(configuration))
dashboard_token = 'dashboard_token_example' # str | 
update_dashboard = vantage.UpdateDashboard() # UpdateDashboard | 

try:
    api_response = api_instance.update_dashboard(dashboard_token, update_dashboard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostsApi->update_dashboard: %s\n" % e)
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

