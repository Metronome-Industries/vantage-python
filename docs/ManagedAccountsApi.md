# vantage.ManagedAccountsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_managed_account**](ManagedAccountsApi.md#create_managed_account) | **POST** /managed_accounts | 
[**delete_managed_account**](ManagedAccountsApi.md#delete_managed_account) | **DELETE** /managed_accounts/{managed_account_token} | 
[**get_managed_account**](ManagedAccountsApi.md#get_managed_account) | **GET** /managed_accounts/{managed_account_token} | 
[**get_managed_accounts**](ManagedAccountsApi.md#get_managed_accounts) | **GET** /managed_accounts | 
[**update_managed_account**](ManagedAccountsApi.md#update_managed_account) | **PUT** /managed_accounts/{managed_account_token} | 


# **create_managed_account**
> ManagedAccount create_managed_account(create_managed_account)



Create a Managed Account.

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
api_instance = vantage.ManagedAccountsApi(vantage.ApiClient(configuration))
create_managed_account = vantage.CreateManagedAccount() # CreateManagedAccount | 

try:
    api_response = api_instance.create_managed_account(create_managed_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedAccountsApi->create_managed_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_managed_account** | [**CreateManagedAccount**](CreateManagedAccount.md)|  | 

### Return type

[**ManagedAccount**](ManagedAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_managed_account**
> ManagedAccount delete_managed_account(managed_account_token)



Delete a Managed Account.

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
api_instance = vantage.ManagedAccountsApi(vantage.ApiClient(configuration))
managed_account_token = 'managed_account_token_example' # str | 

try:
    api_response = api_instance.delete_managed_account(managed_account_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedAccountsApi->delete_managed_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_account_token** | **str**|  | 

### Return type

[**ManagedAccount**](ManagedAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_account**
> ManagedAccount get_managed_account(managed_account_token)



Return a Managed Account.

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
api_instance = vantage.ManagedAccountsApi(vantage.ApiClient(configuration))
managed_account_token = 'managed_account_token_example' # str | 

try:
    api_response = api_instance.get_managed_account(managed_account_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedAccountsApi->get_managed_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_account_token** | **str**|  | 

### Return type

[**ManagedAccount**](ManagedAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_managed_accounts**
> ManagedAccounts get_managed_accounts(page=page, limit=limit)



Returns a list of managed accounts.

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
api_instance = vantage.ManagedAccountsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_managed_accounts(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedAccountsApi->get_managed_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**ManagedAccounts**](ManagedAccounts.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_managed_account**
> ManagedAccount update_managed_account(managed_account_token, update_managed_account)



Update a Managed Account.

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
api_instance = vantage.ManagedAccountsApi(vantage.ApiClient(configuration))
managed_account_token = 'managed_account_token_example' # str | 
update_managed_account = vantage.UpdateManagedAccount() # UpdateManagedAccount | 

try:
    api_response = api_instance.update_managed_account(managed_account_token, update_managed_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedAccountsApi->update_managed_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_account_token** | **str**|  | 
 **update_managed_account** | [**UpdateManagedAccount**](UpdateManagedAccount.md)|  | 

### Return type

[**ManagedAccount**](ManagedAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

