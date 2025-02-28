# vantage.AnomalyAlertsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_anomaly_alert**](AnomalyAlertsApi.md#get_anomaly_alert) | **GET** /anomaly_alerts/{anomaly_alert_token} | 
[**get_anomaly_alerts**](AnomalyAlertsApi.md#get_anomaly_alerts) | **GET** /anomaly_alerts | 
[**update_anomaly_alert**](AnomalyAlertsApi.md#update_anomaly_alert) | **PUT** /anomaly_alerts/{anomaly_alert_token} | 


# **get_anomaly_alert**
> AnomalyAlert get_anomaly_alert(anomaly_alert_token)



Return an AnomalyAlert that the current API token has access to.

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
api_instance = vantage.AnomalyAlertsApi(vantage.ApiClient(configuration))
anomaly_alert_token = 'anomaly_alert_token_example' # str | 

try:
    api_response = api_instance.get_anomaly_alert(anomaly_alert_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyAlertsApi->get_anomaly_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_alert_token** | **str**|  | 

### Return type

[**AnomalyAlert**](AnomalyAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anomaly_alerts**
> AnomalyAlerts get_anomaly_alerts(page=page, limit=limit)



Return all Anomaly Alerts that the current API token has access to.

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
api_instance = vantage.AnomalyAlertsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_anomaly_alerts(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyAlertsApi->get_anomaly_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**AnomalyAlerts**](AnomalyAlerts.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_anomaly_alert**
> AnomalyAlert update_anomaly_alert(anomaly_alert_token, update_anomaly_alert)



Update an AnomalyAlert.

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
api_instance = vantage.AnomalyAlertsApi(vantage.ApiClient(configuration))
anomaly_alert_token = 'anomaly_alert_token_example' # str | 
update_anomaly_alert = vantage.UpdateAnomalyAlert() # UpdateAnomalyAlert | 

try:
    api_response = api_instance.update_anomaly_alert(anomaly_alert_token, update_anomaly_alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyAlertsApi->update_anomaly_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_alert_token** | **str**|  | 
 **update_anomaly_alert** | [**UpdateAnomalyAlert**](UpdateAnomalyAlert.md)|  | 

### Return type

[**AnomalyAlert**](AnomalyAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

