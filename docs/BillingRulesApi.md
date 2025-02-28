# vantage.BillingRulesApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_rule**](BillingRulesApi.md#create_billing_rule) | **POST** /billing_rules | 
[**delete_billing_rule**](BillingRulesApi.md#delete_billing_rule) | **DELETE** /billing_rules/{billing_rule_token} | 
[**get_billing_rule**](BillingRulesApi.md#get_billing_rule) | **GET** /billing_rules/{billing_rule_token} | 
[**get_billing_rules**](BillingRulesApi.md#get_billing_rules) | **GET** /billing_rules | 
[**update_billing_rule**](BillingRulesApi.md#update_billing_rule) | **PUT** /billing_rules/{billing_rule_token} | 


# **create_billing_rule**
> BillingRule create_billing_rule(create_billing_rule)



Create a Billing Rule.

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
api_instance = vantage.BillingRulesApi(vantage.ApiClient(configuration))
create_billing_rule = vantage.CreateBillingRule() # CreateBillingRule | 

try:
    api_response = api_instance.create_billing_rule(create_billing_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingRulesApi->create_billing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_billing_rule** | [**CreateBillingRule**](CreateBillingRule.md)|  | 

### Return type

[**BillingRule**](BillingRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_rule**
> BillingRule delete_billing_rule(billing_rule_token)



Delete a Billing Rule.

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
api_instance = vantage.BillingRulesApi(vantage.ApiClient(configuration))
billing_rule_token = 'billing_rule_token_example' # str | 

try:
    api_response = api_instance.delete_billing_rule(billing_rule_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingRulesApi->delete_billing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_rule_token** | **str**|  | 

### Return type

[**BillingRule**](BillingRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_rule**
> BillingRule get_billing_rule(billing_rule_token)



Return a Billing Rule.

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
api_instance = vantage.BillingRulesApi(vantage.ApiClient(configuration))
billing_rule_token = 'billing_rule_token_example' # str | 

try:
    api_response = api_instance.get_billing_rule(billing_rule_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingRulesApi->get_billing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_rule_token** | **str**|  | 

### Return type

[**BillingRule**](BillingRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_rules**
> BillingRules get_billing_rules(page=page, limit=limit)



Returns a list of billing rules.

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
api_instance = vantage.BillingRulesApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_billing_rules(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingRulesApi->get_billing_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**BillingRules**](BillingRules.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_rule**
> BillingRule update_billing_rule(billing_rule_token, update_billing_rule)



Update a Billing Rule.

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
api_instance = vantage.BillingRulesApi(vantage.ApiClient(configuration))
billing_rule_token = 'billing_rule_token_example' # str | 
update_billing_rule = vantage.UpdateBillingRule() # UpdateBillingRule | 

try:
    api_response = api_instance.update_billing_rule(billing_rule_token, update_billing_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingRulesApi->update_billing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_rule_token** | **str**|  | 
 **update_billing_rule** | [**UpdateBillingRule**](UpdateBillingRule.md)|  | 

### Return type

[**BillingRule**](BillingRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

