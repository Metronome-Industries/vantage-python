# vantage.AnomalyNotificationsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_anomaly_notification**](AnomalyNotificationsApi.md#create_anomaly_notification) | **POST** /anomaly_notifications | 
[**delete_anomaly_notification**](AnomalyNotificationsApi.md#delete_anomaly_notification) | **DELETE** /anomaly_notifications/{anomaly_notification_token} | 
[**get_anomaly_notification**](AnomalyNotificationsApi.md#get_anomaly_notification) | **GET** /anomaly_notifications/{anomaly_notification_token} | 
[**get_anomaly_notifications**](AnomalyNotificationsApi.md#get_anomaly_notifications) | **GET** /anomaly_notifications | 
[**update_anomaly_notification**](AnomalyNotificationsApi.md#update_anomaly_notification) | **PUT** /anomaly_notifications/{anomaly_notification_token} | 


# **create_anomaly_notification**
> AnomalyNotification create_anomaly_notification(create_anomaly_notification)



Create an Anomaly Notification for a Cost Report.

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
api_instance = vantage.AnomalyNotificationsApi(vantage.ApiClient(configuration))
create_anomaly_notification = vantage.CreateAnomalyNotification() # CreateAnomalyNotification | 

try:
    api_response = api_instance.create_anomaly_notification(create_anomaly_notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyNotificationsApi->create_anomaly_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_anomaly_notification** | [**CreateAnomalyNotification**](CreateAnomalyNotification.md)|  | 

### Return type

[**AnomalyNotification**](AnomalyNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_anomaly_notification**
> AnomalyNotification delete_anomaly_notification(anomaly_notification_token)



Delete an Anomaly Notification.

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
api_instance = vantage.AnomalyNotificationsApi(vantage.ApiClient(configuration))
anomaly_notification_token = 'anomaly_notification_token_example' # str | 

try:
    api_response = api_instance.delete_anomaly_notification(anomaly_notification_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyNotificationsApi->delete_anomaly_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_notification_token** | **str**|  | 

### Return type

[**AnomalyNotification**](AnomalyNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anomaly_notification**
> AnomalyNotification get_anomaly_notification(anomaly_notification_token)



Return an Anomaly Notification that the current API token has access to.

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
api_instance = vantage.AnomalyNotificationsApi(vantage.ApiClient(configuration))
anomaly_notification_token = 'anomaly_notification_token_example' # str | 

try:
    api_response = api_instance.get_anomaly_notification(anomaly_notification_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyNotificationsApi->get_anomaly_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_notification_token** | **str**|  | 

### Return type

[**AnomalyNotification**](AnomalyNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anomaly_notifications**
> AnomalyNotifications get_anomaly_notifications(page=page, limit=limit)



Return all Anomaly Notifications.

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
api_instance = vantage.AnomalyNotificationsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_anomaly_notifications(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyNotificationsApi->get_anomaly_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**AnomalyNotifications**](AnomalyNotifications.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_anomaly_notification**
> AnomalyNotification update_anomaly_notification(anomaly_notification_token, update_anomaly_notification)



Update an Anomaly Notification.

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
api_instance = vantage.AnomalyNotificationsApi(vantage.ApiClient(configuration))
anomaly_notification_token = 'anomaly_notification_token_example' # str | 
update_anomaly_notification = vantage.UpdateAnomalyNotification() # UpdateAnomalyNotification | 

try:
    api_response = api_instance.update_anomaly_notification(anomaly_notification_token, update_anomaly_notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyNotificationsApi->update_anomaly_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anomaly_notification_token** | **str**|  | 
 **update_anomaly_notification** | [**UpdateAnomalyNotification**](UpdateAnomalyNotification.md)|  | 

### Return type

[**AnomalyNotification**](AnomalyNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

