# vantage.BudgetAlertsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_budget_alert**](BudgetAlertsApi.md#create_budget_alert) | **POST** /budget_alerts | 
[**delete_budget_alert**](BudgetAlertsApi.md#delete_budget_alert) | **DELETE** /budget_alerts/{budget_alert_token} | 
[**get_budget_alert**](BudgetAlertsApi.md#get_budget_alert) | **GET** /budget_alerts/{budget_alert_token} | 
[**get_budget_alerts**](BudgetAlertsApi.md#get_budget_alerts) | **GET** /budget_alerts | 
[**update_budget_alert**](BudgetAlertsApi.md#update_budget_alert) | **PUT** /budget_alerts/{budget_alert_token} | 


# **create_budget_alert**
> BudgetAlert create_budget_alert(budget_tokens, threshold, duration_in_days, user_tokens=user_tokens, period_to_track=period_to_track, recipient_channels=recipient_channels)



Create a Budget Alert.

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
api_instance = vantage.BudgetAlertsApi(vantage.ApiClient(configuration))
budget_tokens = ['budget_tokens_example'] # list[str] | The tokens of the Budget that has the alert.
threshold = 56 # int | The threshold amount that must be met for the alert to fire.
duration_in_days = 56 # int | The number of days from the start or end of the month to trigger the alert if the threshold is reached.  For the full month, pass an empty value.
user_tokens = ['user_tokens_example'] # list[str] | The tokens of the users that receive the alert. (optional)
period_to_track = 'period_to_track_example' # str | The period tracked on the alert. Used with duration_in_days to determine the time window of the alert. Defaults to start_of_the_month if not passed. Possible values: start_of_the_month, end_of_the_month. (optional)
recipient_channels = ['recipient_channels_example'] # list[str] | The channels receiving the alerts. Requires an integration provider to be connected. (optional)

try:
    api_response = api_instance.create_budget_alert(budget_tokens, threshold, duration_in_days, user_tokens=user_tokens, period_to_track=period_to_track, recipient_channels=recipient_channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetAlertsApi->create_budget_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_tokens** | [**list[str]**](str.md)| The tokens of the Budget that has the alert. | 
 **threshold** | **int**| The threshold amount that must be met for the alert to fire. | 
 **duration_in_days** | **int**| The number of days from the start or end of the month to trigger the alert if the threshold is reached.  For the full month, pass an empty value. | 
 **user_tokens** | [**list[str]**](str.md)| The tokens of the users that receive the alert. | [optional] 
 **period_to_track** | **str**| The period tracked on the alert. Used with duration_in_days to determine the time window of the alert. Defaults to start_of_the_month if not passed. Possible values: start_of_the_month, end_of_the_month. | [optional] 
 **recipient_channels** | [**list[str]**](str.md)| The channels receiving the alerts. Requires an integration provider to be connected. | [optional] 

### Return type

[**BudgetAlert**](BudgetAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_budget_alert**
> BudgetAlert delete_budget_alert(budget_alert_token)



Delete a BudgetAlert.

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
api_instance = vantage.BudgetAlertsApi(vantage.ApiClient(configuration))
budget_alert_token = 'budget_alert_token_example' # str | 

try:
    api_response = api_instance.delete_budget_alert(budget_alert_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetAlertsApi->delete_budget_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_alert_token** | **str**|  | 

### Return type

[**BudgetAlert**](BudgetAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_alert**
> BudgetAlert get_budget_alert(budget_alert_token)



Return a BudgetAlert.

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
api_instance = vantage.BudgetAlertsApi(vantage.ApiClient(configuration))
budget_alert_token = 'budget_alert_token_example' # str | 

try:
    api_response = api_instance.get_budget_alert(budget_alert_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetAlertsApi->get_budget_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_alert_token** | **str**|  | 

### Return type

[**BudgetAlert**](BudgetAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_alerts**
> BudgetAlerts get_budget_alerts(page=page, limit=limit)



Return all BudgetAlerts.

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
api_instance = vantage.BudgetAlertsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The number of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_budget_alerts(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetAlertsApi->get_budget_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The number of results to return. The maximum is 1000. | [optional] 

### Return type

[**BudgetAlerts**](BudgetAlerts.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget_alert**
> BudgetAlert update_budget_alert(budget_alert_token, budget_tokens=budget_tokens, threshold=threshold, user_tokens=user_tokens, duration_in_days=duration_in_days, period_to_track=period_to_track, recipient_channels=recipient_channels)



Updates an existing BudgetAlert.

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
api_instance = vantage.BudgetAlertsApi(vantage.ApiClient(configuration))
budget_alert_token = 'budget_alert_token_example' # str | 
budget_tokens = ['budget_tokens_example'] # list[str] | The tokens of the Budget that has the alert. (optional)
threshold = 56 # int | The threshold amount that must be met for the alert to fire. (optional)
user_tokens = ['user_tokens_example'] # list[str] | The tokens of the users that receive the alert. (optional)
duration_in_days = 56 # int | The number of days from the start or end of the month to trigger the alert if the threshold is reached. For the full month, pass an empty value. (optional)
period_to_track = 'period_to_track_example' # str | The period tracked on the alert. Used with duration_in_days to determine the time window of the alert. Defaults to start_of_the_month if not passed. Possible values: start_of_the_month, end_of_the_month. (optional)
recipient_channels = ['recipient_channels_example'] # list[str] | The channels receiving the alerts. Requires an integration provider to be connected. (optional)

try:
    api_response = api_instance.update_budget_alert(budget_alert_token, budget_tokens=budget_tokens, threshold=threshold, user_tokens=user_tokens, duration_in_days=duration_in_days, period_to_track=period_to_track, recipient_channels=recipient_channels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetAlertsApi->update_budget_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_alert_token** | **str**|  | 
 **budget_tokens** | [**list[str]**](str.md)| The tokens of the Budget that has the alert. | [optional] 
 **threshold** | **int**| The threshold amount that must be met for the alert to fire. | [optional] 
 **user_tokens** | [**list[str]**](str.md)| The tokens of the users that receive the alert. | [optional] 
 **duration_in_days** | **int**| The number of days from the start or end of the month to trigger the alert if the threshold is reached. For the full month, pass an empty value. | [optional] 
 **period_to_track** | **str**| The period tracked on the alert. Used with duration_in_days to determine the time window of the alert. Defaults to start_of_the_month if not passed. Possible values: start_of_the_month, end_of_the_month. | [optional] 
 **recipient_channels** | [**list[str]**](str.md)| The channels receiving the alerts. Requires an integration provider to be connected. | [optional] 

### Return type

[**BudgetAlert**](BudgetAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

