# vantage.SegmentsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segment**](SegmentsApi.md#create_segment) | **POST** /segments | 
[**delete_segment**](SegmentsApi.md#delete_segment) | **DELETE** /segments/{segment_token} | 
[**get_segment**](SegmentsApi.md#get_segment) | **GET** /segments/{segment_token} | 
[**get_segments**](SegmentsApi.md#get_segments) | **GET** /segments | 
[**update_segment**](SegmentsApi.md#update_segment) | **PUT** /segments/{segment_token} | 


# **create_segment**
> Segment create_segment(create_segment)



Create a Segment.

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
api_instance = vantage.SegmentsApi(vantage.ApiClient(configuration))
create_segment = vantage.CreateSegment() # CreateSegment | 

try:
    api_response = api_instance.create_segment(create_segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->create_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_segment** | [**CreateSegment**](CreateSegment.md)|  | 

### Return type

[**Segment**](Segment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_segment**
> Segment delete_segment(segment_token)



Delete a Segment.

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
api_instance = vantage.SegmentsApi(vantage.ApiClient(configuration))
segment_token = 'segment_token_example' # str | 

try:
    api_response = api_instance.delete_segment(segment_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->delete_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_token** | **str**|  | 

### Return type

[**Segment**](Segment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment**
> Segment get_segment(segment_token)



Return a Segment.

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
api_instance = vantage.SegmentsApi(vantage.ApiClient(configuration))
segment_token = 'segment_token_example' # str | 

try:
    api_response = api_instance.get_segment(segment_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_token** | **str**|  | 

### Return type

[**Segment**](Segment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segments**
> Segments get_segments(page=page, limit=limit)



Return all Segments.

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
api_instance = vantage.SegmentsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_segments(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**Segments**](Segments.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_segment**
> Segment update_segment(segment_token, update_segment)



Update a Segment.

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
api_instance = vantage.SegmentsApi(vantage.ApiClient(configuration))
segment_token = 'segment_token_example' # str | 
update_segment = vantage.UpdateSegment() # UpdateSegment | 

try:
    api_response = api_instance.update_segment(segment_token, update_segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->update_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_token** | **str**|  | 
 **update_segment** | [**UpdateSegment**](UpdateSegment.md)|  | 

### Return type

[**Segment**](Segment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

