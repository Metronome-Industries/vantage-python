# vantage.VirtualTagsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_virtual_tag_config**](VirtualTagsApi.md#create_virtual_tag_config) | **POST** /virtual_tag_configs | 
[**delete_virtual_tag_config**](VirtualTagsApi.md#delete_virtual_tag_config) | **DELETE** /virtual_tag_configs/{token} | 
[**get_virtual_tag_config**](VirtualTagsApi.md#get_virtual_tag_config) | **GET** /virtual_tag_configs/{token} | 
[**get_virtual_tag_configs**](VirtualTagsApi.md#get_virtual_tag_configs) | **GET** /virtual_tag_configs | 
[**update_virtual_tag_config**](VirtualTagsApi.md#update_virtual_tag_config) | **PUT** /virtual_tag_configs/{token} | 


# **create_virtual_tag_config**
> VirtualTagConfig create_virtual_tag_config(create_virtual_tag_config)



Create a new VirtualTagConfig.

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
api_instance = vantage.VirtualTagsApi(vantage.ApiClient(configuration))
create_virtual_tag_config = vantage.CreateVirtualTagConfig() # CreateVirtualTagConfig | 

try:
    api_response = api_instance.create_virtual_tag_config(create_virtual_tag_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualTagsApi->create_virtual_tag_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_virtual_tag_config** | [**CreateVirtualTagConfig**](CreateVirtualTagConfig.md)|  | 

### Return type

[**VirtualTagConfig**](VirtualTagConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_tag_config**
> VirtualTagConfig delete_virtual_tag_config(token)



Deletes an existing VirtualTagConfig.

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
api_instance = vantage.VirtualTagsApi(vantage.ApiClient(configuration))
token = 'token_example' # str | 

try:
    api_response = api_instance.delete_virtual_tag_config(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualTagsApi->delete_virtual_tag_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**VirtualTagConfig**](VirtualTagConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_tag_config**
> VirtualTagConfig get_virtual_tag_config(token)



Return a specific VirtualTagConfig.

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
api_instance = vantage.VirtualTagsApi(vantage.ApiClient(configuration))
token = 'token_example' # str | 

try:
    api_response = api_instance.get_virtual_tag_config(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualTagsApi->get_virtual_tag_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**VirtualTagConfig**](VirtualTagConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_tag_configs**
> VirtualTagConfigs get_virtual_tag_configs()



Return all VirtualTagConfigs that the current API token has access to.

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
api_instance = vantage.VirtualTagsApi(vantage.ApiClient(configuration))

try:
    api_response = api_instance.get_virtual_tag_configs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualTagsApi->get_virtual_tag_configs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VirtualTagConfigs**](VirtualTagConfigs.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_tag_config**
> VirtualTagConfig update_virtual_tag_config(token, update_virtual_tag_config)



Updates an existing VirtualTagConfig.

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
api_instance = vantage.VirtualTagsApi(vantage.ApiClient(configuration))
token = 'token_example' # str | 
update_virtual_tag_config = vantage.UpdateVirtualTagConfig() # UpdateVirtualTagConfig | 

try:
    api_response = api_instance.update_virtual_tag_config(token, update_virtual_tag_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualTagsApi->update_virtual_tag_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **update_virtual_tag_config** | [**UpdateVirtualTagConfig**](UpdateVirtualTagConfig.md)|  | 

### Return type

[**VirtualTagConfig**](VirtualTagConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

