# vantage.IntegrationsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_integration**](IntegrationsApi.md#create_azure_integration) | **POST** /integrations/azure | 
[**create_custom_provider_integration**](IntegrationsApi.md#create_custom_provider_integration) | **POST** /integrations/custom_provider | 
[**create_gcp_integration**](IntegrationsApi.md#create_gcp_integration) | **POST** /integrations/gcp | 
[**create_user_costs_upload_via_csv**](IntegrationsApi.md#create_user_costs_upload_via_csv) | **POST** /integrations/{integration_token}/costs.csv | 
[**delete_integration**](IntegrationsApi.md#delete_integration) | **DELETE** /integrations/{integration_token} | 
[**delete_user_costs_upload**](IntegrationsApi.md#delete_user_costs_upload) | **DELETE** /integrations/{integration_token}/costs/{user_costs_upload_token} | 
[**get_integration**](IntegrationsApi.md#get_integration) | **GET** /integrations/{integration_token} | 
[**get_integrations**](IntegrationsApi.md#get_integrations) | **GET** /integrations | 
[**get_user_costs_uploads**](IntegrationsApi.md#get_user_costs_uploads) | **GET** /integrations/{integration_token}/costs | 
[**update_integration**](IntegrationsApi.md#update_integration) | **PUT** /integrations/{integration_token} | 


# **create_azure_integration**
> Integration create_azure_integration(create_azure_integration)



Create an Azure Integration

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
api_instance = vantage.IntegrationsApi(vantage.ApiClient(configuration))
create_azure_integration = vantage.CreateAzureIntegration() # CreateAzureIntegration | 

try:
    api_response = api_instance.create_azure_integration(create_azure_integration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->create_azure_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_azure_integration** | [**CreateAzureIntegration**](CreateAzureIntegration.md)|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_provider_integration**
> Integration create_custom_provider_integration(create_custom_provider_integration)



Create a Custom Provider Integration

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
api_instance = vantage.IntegrationsApi(vantage.ApiClient(configuration))
create_custom_provider_integration = vantage.CreateCustomProviderIntegration() # CreateCustomProviderIntegration | 

try:
    api_response = api_instance.create_custom_provider_integration(create_custom_provider_integration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->create_custom_provider_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_provider_integration** | [**CreateCustomProviderIntegration**](CreateCustomProviderIntegration.md)|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gcp_integration**
> Integration create_gcp_integration(create_gcp_integration)



Create a GCP Integration

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
api_instance = vantage.IntegrationsApi(vantage.ApiClient(configuration))
create_gcp_integration = vantage.CreateGCPIntegration() # CreateGCPIntegration | 

try:
    api_response = api_instance.create_gcp_integration(create_gcp_integration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->create_gcp_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_gcp_integration** | [**CreateGCPIntegration**](CreateGCPIntegration.md)|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_costs_upload_via_csv**
> UserCostsUpload create_user_costs_upload_via_csv(csv, integration_token)



Create UserCostsUpload via CSV for a Custom Provider Integration.

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
api_instance = vantage.IntegrationsApi(vantage.ApiClient(configuration))
csv = '/path/to/file.txt' # file | CSV file containing custom costs
integration_token = 'integration_token_example' # str | 

try:
    api_response = api_instance.create_user_costs_upload_via_csv(csv, integration_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->create_user_costs_upload_via_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv** | **file**| CSV file containing custom costs | 
 **integration_token** | **str**|  | 

### Return type

[**UserCostsUpload**](UserCostsUpload.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration**
> Integration delete_integration(integration_token)



Delete an Integration.

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
api_instance = vantage.IntegrationsApi(vantage.ApiClient(configuration))
integration_token = 'integration_token_example' # str | 

try:
    api_response = api_instance.delete_integration(integration_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->delete_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_token** | **str**|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_costs_upload**
> Cost delete_user_costs_upload(integration_token, user_costs_upload_token)



Delete a UserCostsUpload.

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
api_instance = vantage.IntegrationsApi(vantage.ApiClient(configuration))
integration_token = 'integration_token_example' # str | 
user_costs_upload_token = 56 # int | 

try:
    api_response = api_instance.delete_user_costs_upload(integration_token, user_costs_upload_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->delete_user_costs_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_token** | **str**|  | 
 **user_costs_upload_token** | **int**|  | 

### Return type

[**Cost**](Cost.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration**
> Integration get_integration(integration_token)



Return an Integration.

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
api_instance = vantage.IntegrationsApi(vantage.ApiClient(configuration))
integration_token = 'integration_token_example' # str | 

try:
    api_response = api_instance.get_integration(integration_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_token** | **str**|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integrations**
> Integrations get_integrations(provider=provider, account_identifier=account_identifier, page=page, limit=limit)



Return all Integrations.

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
api_instance = vantage.IntegrationsApi(vantage.ApiClient(configuration))
provider = 'provider_example' # str | Query by provider name to list all Integrations for a specific provider. (optional)
account_identifier = 'account_identifier_example' # str | Query by account identifier to list all Integrations that match a specific account. For Azure, this is the subscription ID. Must include provider when using this parameter. (optional)
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The number of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_integrations(provider=provider, account_identifier=account_identifier, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Query by provider name to list all Integrations for a specific provider. | [optional] 
 **account_identifier** | **str**| Query by account identifier to list all Integrations that match a specific account. For Azure, this is the subscription ID. Must include provider when using this parameter. | [optional] 
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The number of results to return. The maximum is 1000. | [optional] 

### Return type

[**Integrations**](Integrations.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_costs_uploads**
> UserCostsUploads get_user_costs_uploads(integration_token)



List UserCostUploads.

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
api_instance = vantage.IntegrationsApi(vantage.ApiClient(configuration))
integration_token = 'integration_token_example' # str | 

try:
    api_response = api_instance.get_user_costs_uploads(integration_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_user_costs_uploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_token** | **str**|  | 

### Return type

[**UserCostsUploads**](UserCostsUploads.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration**
> Integration update_integration(integration_token, workspace_tokens=workspace_tokens)



Update an Integration.

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
api_instance = vantage.IntegrationsApi(vantage.ApiClient(configuration))
integration_token = 'integration_token_example' # str | 
workspace_tokens = [vantage.list[str]()] # list[str] | The Workspace tokens to associate to the Integration. (optional)

try:
    api_response = api_instance.update_integration(integration_token, workspace_tokens=workspace_tokens)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->update_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_token** | **str**|  | 
 **workspace_tokens** | **list[str]**| The Workspace tokens to associate to the Integration. | [optional] 

### Return type

[**Integration**](Integration.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

