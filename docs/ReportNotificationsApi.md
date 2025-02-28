# vantage.ReportNotificationsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report_notification**](ReportNotificationsApi.md#create_report_notification) | **POST** /report_notifications | 
[**delete_report_notification**](ReportNotificationsApi.md#delete_report_notification) | **DELETE** /report_notifications/{report_notification_token} | 
[**get_report_notification**](ReportNotificationsApi.md#get_report_notification) | **GET** /report_notifications/{report_notification_token} | 
[**get_report_notifications**](ReportNotificationsApi.md#get_report_notifications) | **GET** /report_notifications | 
[**update_report_notification**](ReportNotificationsApi.md#update_report_notification) | **PUT** /report_notifications/{report_notification_token} | 


# **create_report_notification**
> ReportNotification create_report_notification(create_report_notification)



Create a ReportNotification.

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
api_instance = vantage.ReportNotificationsApi(vantage.ApiClient(configuration))
create_report_notification = vantage.CreateReportNotification() # CreateReportNotification | 

try:
    api_response = api_instance.create_report_notification(create_report_notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportNotificationsApi->create_report_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_report_notification** | [**CreateReportNotification**](CreateReportNotification.md)|  | 

### Return type

[**ReportNotification**](ReportNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_notification**
> ReportNotification delete_report_notification(report_notification_token)



Delete a ReportNotification.

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
api_instance = vantage.ReportNotificationsApi(vantage.ApiClient(configuration))
report_notification_token = 'report_notification_token_example' # str | 

try:
    api_response = api_instance.delete_report_notification(report_notification_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportNotificationsApi->delete_report_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_notification_token** | **str**|  | 

### Return type

[**ReportNotification**](ReportNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_notification**
> ReportNotification get_report_notification(report_notification_token)



Return a ReportNotification.

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
api_instance = vantage.ReportNotificationsApi(vantage.ApiClient(configuration))
report_notification_token = 'report_notification_token_example' # str | 

try:
    api_response = api_instance.get_report_notification(report_notification_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportNotificationsApi->get_report_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_notification_token** | **str**|  | 

### Return type

[**ReportNotification**](ReportNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_notifications**
> ReportNotifications get_report_notifications(page=page, limit=limit)



Return all ReportNotifications.

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
api_instance = vantage.ReportNotificationsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_report_notifications(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportNotificationsApi->get_report_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**ReportNotifications**](ReportNotifications.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_notification**
> ReportNotification update_report_notification(report_notification_token, update_report_notification)



Update a ReportNotification.

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
api_instance = vantage.ReportNotificationsApi(vantage.ApiClient(configuration))
report_notification_token = 'report_notification_token_example' # str | 
update_report_notification = vantage.UpdateReportNotification() # UpdateReportNotification | 

try:
    api_response = api_instance.update_report_notification(report_notification_token, update_report_notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportNotificationsApi->update_report_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_notification_token** | **str**|  | 
 **update_report_notification** | [**UpdateReportNotification**](UpdateReportNotification.md)|  | 

### Return type

[**ReportNotification**](ReportNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

