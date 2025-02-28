# vantage.RecommendationsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recommendation**](RecommendationsApi.md#get_recommendation) | **GET** /recommendations/{recommendation_token} | 
[**get_recommendation_resource**](RecommendationsApi.md#get_recommendation_resource) | **GET** /recommendations/{recommendation_token}/resources/{resource_token} | 
[**get_recommendation_resources**](RecommendationsApi.md#get_recommendation_resources) | **GET** /recommendations/{recommendation_token}/resources | 
[**get_recommendations**](RecommendationsApi.md#get_recommendations) | **GET** /recommendations | 


# **get_recommendation**
> Recommendation get_recommendation(recommendation_token)



Return a Recommendation.

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
api_instance = vantage.RecommendationsApi(vantage.ApiClient(configuration))
recommendation_token = 'recommendation_token_example' # str | 

try:
    api_response = api_instance.get_recommendation(recommendation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecommendationsApi->get_recommendation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_token** | **str**|  | 

### Return type

[**Recommendation**](Recommendation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommendation_resource**
> ProviderResource get_recommendation_resource(recommendation_token, resource_token)



Return an Active Resource, including Recommendation Actions, referenced in this Recommendation.

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
api_instance = vantage.RecommendationsApi(vantage.ApiClient(configuration))
recommendation_token = 'recommendation_token_example' # str | 
resource_token = 'resource_token_example' # str | 

try:
    api_response = api_instance.get_recommendation_resource(recommendation_token, resource_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecommendationsApi->get_recommendation_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_token** | **str**|  | 
 **resource_token** | **str**|  | 

### Return type

[**ProviderResource**](ProviderResource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommendation_resources**
> ProviderResource get_recommendation_resources(recommendation_token, page=page, limit=limit)



Return all Active Resources, including Recommendation Actions, referenced in this Recommendation.

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
api_instance = vantage.RecommendationsApi(vantage.ApiClient(configuration))
recommendation_token = 'recommendation_token_example' # str | 
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The number of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_recommendation_resources(recommendation_token, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecommendationsApi->get_recommendation_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_token** | **str**|  | 
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The number of results to return. The maximum is 1000. | [optional] 

### Return type

[**ProviderResource**](ProviderResource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommendations**
> Recommendations get_recommendations(workspace_token=workspace_token, provider_account_id=provider_account_id, category=category, provider=provider, page=page, limit=limit)



Return all Recommendations.

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
api_instance = vantage.RecommendationsApi(vantage.ApiClient(configuration))
workspace_token = 'workspace_token_example' # str | Filter by workspace. (optional)
provider_account_id = 'provider_account_id_example' # str | Filter by provider account id (AWS account, Azure subscription id, etc). (optional)
category = 'category_example' # str | Filter by category. (optional)
provider = 'provider_example' # str | Filter by provider. (optional)
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The number of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_recommendations(workspace_token=workspace_token, provider_account_id=provider_account_id, category=category, provider=provider, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecommendationsApi->get_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_token** | **str**| Filter by workspace. | [optional] 
 **provider_account_id** | **str**| Filter by provider account id (AWS account, Azure subscription id, etc). | [optional] 
 **category** | **str**| Filter by category. | [optional] 
 **provider** | **str**| Filter by provider. | [optional] 
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The number of results to return. The maximum is 1000. | [optional] 

### Return type

[**Recommendations**](Recommendations.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

