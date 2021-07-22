# vantage.PingApi

All URIs are relative to *https://api.vantage.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](PingApi.md#ping) | **GET** /v1/ping | 


# **ping**
> object ping()



This is a health check endpoint that can be used to determine Vantage API healthiness. It will return 200 if everything is running smoothly.

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
api_instance = vantage.PingApi(vantage.ApiClient(configuration))

try:
    api_response = api_instance.ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingApi->ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

