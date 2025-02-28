# vantage.BudgetsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_budget**](BudgetsApi.md#create_budget) | **POST** /budgets | 
[**delete_budget**](BudgetsApi.md#delete_budget) | **DELETE** /budgets/{budget_token} | 
[**get_budget**](BudgetsApi.md#get_budget) | **GET** /budgets/{budget_token} | 
[**get_budgets**](BudgetsApi.md#get_budgets) | **GET** /budgets | 
[**update_budget**](BudgetsApi.md#update_budget) | **PUT** /budgets/{budget_token} | 


# **create_budget**
> Budget create_budget(create_budget)



Create a Budget.

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
api_instance = vantage.BudgetsApi(vantage.ApiClient(configuration))
create_budget = vantage.CreateBudget() # CreateBudget | 

try:
    api_response = api_instance.create_budget(create_budget)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->create_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_budget** | [**CreateBudget**](CreateBudget.md)|  | 

### Return type

[**Budget**](Budget.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_budget**
> Budget delete_budget(budget_token)



Delete a Budget.

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
api_instance = vantage.BudgetsApi(vantage.ApiClient(configuration))
budget_token = 'budget_token_example' # str | 

try:
    api_response = api_instance.delete_budget(budget_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->delete_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_token** | **str**|  | 

### Return type

[**Budget**](Budget.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget**
> Budget get_budget(budget_token, include_performance=include_performance)



Return a Budget.

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
api_instance = vantage.BudgetsApi(vantage.ApiClient(configuration))
budget_token = 'budget_token_example' # str | 
include_performance = true # bool | Include performance data. (optional)

try:
    api_response = api_instance.get_budget(budget_token, include_performance=include_performance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_token** | **str**|  | 
 **include_performance** | **bool**| Include performance data. | [optional] 

### Return type

[**Budget**](Budget.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets**
> Budgets get_budgets(page=page, limit=limit)



Return all Budgets.

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
api_instance = vantage.BudgetsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The number of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_budgets(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The number of results to return. The maximum is 1000. | [optional] 

### Return type

[**Budgets**](Budgets.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget**
> Budget update_budget(budget_token, update_budget)



Update a Budget.

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
api_instance = vantage.BudgetsApi(vantage.ApiClient(configuration))
budget_token = 'budget_token_example' # str | 
update_budget = vantage.UpdateBudget() # UpdateBudget | 

try:
    api_response = api_instance.update_budget(budget_token, update_budget)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->update_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_token** | **str**|  | 
 **update_budget** | [**UpdateBudget**](UpdateBudget.md)|  | 

### Return type

[**Budget**](Budget.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

