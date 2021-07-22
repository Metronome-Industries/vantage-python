# vantage.PricesApi

All URIs are relative to *https://api.vantage.sh*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_price**](PricesApi.md#get_price) | **GET** /v1/products/{product_id}/prices/{id} | 
[**get_prices**](PricesApi.md#get_prices) | **GET** /v1/products/{product_id}/prices | 
[**get_product**](PricesApi.md#get_product) | **GET** /v1/products/{id} | 
[**get_products**](PricesApi.md#get_products) | **GET** /v1/products | 
[**get_providers**](PricesApi.md#get_providers) | **GET** /v1/providers | 
[**get_services**](PricesApi.md#get_services) | **GET** /v1/services | 


# **get_price**
> Price get_price(product_id, id)



Returns a price

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
api_instance = vantage.PricesApi(vantage.ApiClient(configuration))
product_id = 'product_id_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_price(product_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricesApi->get_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Price**](Price.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prices**
> Prices get_prices(product_id, page=page, limit=limit)



Return available Prices across all Regions for a Product.

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
api_instance = vantage.PricesApi(vantage.ApiClient(configuration))
product_id = 'product_id_example' # str | 
page = 2 # int | The page of results to return. (optional)
limit = 500 # int | The amount of results to return. The maximum is 1000 (optional)

try:
    api_response = api_instance.get_prices(product_id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricesApi->get_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000 | [optional] 

### Return type

[**Prices**](Prices.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> Product get_product(id)



Return a product

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
api_instance = vantage.PricesApi(vantage.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_product(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricesApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Product**](Product.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> Products get_products(provider_id=provider_id, service_id=service_id, name=name, page=page, limit=limit)



Return available Products for a Service. For example, with a Provider of AWS and a Service of EC2, Products will be a list of all EC2 Instances. By default, this endpoint returns all Products across all Services and Providers but has optional query parameters for filtering listed below.

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
api_instance = vantage.PricesApi(vantage.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Query by Provider to list all Products across all Services for a Provider. e.g. aws (optional)
service_id = 'service_id_example' # str | Query by Service to list all Products for a specific provider service. e.g. aws-ec2 (optional)
name = 'name_example' # str | Query by name of the Product to see a list of products which match that name. e.g. m5a.16xlarge (optional)
page = 2 # int | The page of results to return. (optional)
limit = 500 # int | The amount of results to return. The maximum is 1000 (optional)

try:
    api_response = api_instance.get_products(provider_id=provider_id, service_id=service_id, name=name, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricesApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Query by Provider to list all Products across all Services for a Provider. e.g. aws | [optional] 
 **service_id** | **str**| Query by Service to list all Products for a specific provider service. e.g. aws-ec2 | [optional] 
 **name** | **str**| Query by name of the Product to see a list of products which match that name. e.g. m5a.16xlarge | [optional] 
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000 | [optional] 

### Return type

[**Products**](Products.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers**
> Providers get_providers(page=page, limit=limit)



Providers are cloud infrastructure and service providers from which all cloud prices are derived. You can think of example Providers as being AWS, GCP, Cloudflare or Datadog. Currently, Vantage only supports a single provider of AWS but over time more will be added. Use this endpoint to retrieve a provider id for other API calls.

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
api_instance = vantage.PricesApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000 (optional)

try:
    api_response = api_instance.get_providers(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricesApi->get_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000 | [optional] 

### Return type

[**Providers**](Providers.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services**
> Services get_services(provider_id=provider_id, page=page, limit=limit)



Return all Services. Examples of Services are EC2 for AWS. This endpoint will return all Services by default but you have the ability to filter Services by Provider using the optional query parameter documented below.

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
api_instance = vantage.PricesApi(vantage.ApiClient(configuration))
provider_id = 'provider_id_example' # str | Query services for a specific provider. e.g. aws (optional)
page = 2 # int | The page of results to return. (optional)
limit = 500 # int | The amount of results to return. The maximum is 1000 (optional)

try:
    api_response = api_instance.get_services(provider_id=provider_id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricesApi->get_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Query services for a specific provider. e.g. aws | [optional] 
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000 | [optional] 

### Return type

[**Services**](Services.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

