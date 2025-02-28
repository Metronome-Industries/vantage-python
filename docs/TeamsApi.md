# vantage.TeamsApi

All URIs are relative to *https://api.vantage.sh/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team**](TeamsApi.md#create_team) | **POST** /teams | 
[**delete_team**](TeamsApi.md#delete_team) | **DELETE** /teams/{team_token} | 
[**get_team**](TeamsApi.md#get_team) | **GET** /teams/{team_token} | 
[**get_teams**](TeamsApi.md#get_teams) | **GET** /teams | 
[**update_team**](TeamsApi.md#update_team) | **PUT** /teams/{team_token} | 


# **create_team**
> Team create_team(create_team)



Create a new Team.

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
api_instance = vantage.TeamsApi(vantage.ApiClient(configuration))
create_team = vantage.CreateTeam() # CreateTeam | 

try:
    api_response = api_instance.create_team(create_team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_team** | [**CreateTeam**](CreateTeam.md)|  | 

### Return type

[**Team**](Team.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> Team delete_team(team_token)



Delete a Team.

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
api_instance = vantage.TeamsApi(vantage.ApiClient(configuration))
team_token = 'team_token_example' # str | 

try:
    api_response = api_instance.delete_team(team_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_token** | **str**|  | 

### Return type

[**Team**](Team.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> Team get_team(team_token)



Return a specific Team.

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
api_instance = vantage.TeamsApi(vantage.ApiClient(configuration))
team_token = 'team_token_example' # str | 

try:
    api_response = api_instance.get_team(team_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_token** | **str**|  | 

### Return type

[**Team**](Team.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> Teams get_teams(page=page, limit=limit)



Return all Teams that the current API token has access to.

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
api_instance = vantage.TeamsApi(vantage.ApiClient(configuration))
page = 56 # int | The page of results to return. (optional)
limit = 56 # int | The amount of results to return. The maximum is 1000. (optional)

try:
    api_response = api_instance.get_teams(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results to return. | [optional] 
 **limit** | **int**| The amount of results to return. The maximum is 1000. | [optional] 

### Return type

[**Teams**](Teams.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> Team update_team(team_token, update_team)



Update a Team.

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
api_instance = vantage.TeamsApi(vantage.ApiClient(configuration))
team_token = 'team_token_example' # str | 
update_team = vantage.UpdateTeam() # UpdateTeam | 

try:
    api_response = api_instance.update_team(team_token, update_team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_token** | **str**|  | 
 **update_team** | [**UpdateTeam**](UpdateTeam.md)|  | 

### Return type

[**Team**](Team.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

