# swagger_client.TeamsApi

All URIs are relative to *http://https://snc-api.herokuapp.com//v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team**](TeamsApi.md#create_team) | **POST** /teams | Create team
[**get_team_by_name**](TeamsApi.md#get_team_by_name) | **GET** /teams/{teamName} | Get team by name
[**teams**](TeamsApi.md#teams) | **GET** /teams | Get all teams
[**update_team**](TeamsApi.md#update_team) | **PUT** /teams/{teamName} | Updated team


# **create_team**
> create_team(body)

Create team

Create a new team

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
body = swagger_client.Team() # Team | The name to create

try: 
    # Create team
    api_instance.create_team(body)
except ApiException as e:
    print("Exception when calling TeamsApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Team**](Team.md)| The name to create | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_by_name**
> Team get_team_by_name(team_name)

Get team by name



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_name = 'team_name_example' # str | The name that needs to be fetched.

try: 
    # Get team by name
    api_response = api_instance.get_team_by_name(team_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_name** | **str**| The name that needs to be fetched. | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams**
> list[Team] teams()

Get all teams

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()

try: 
    # Get all teams
    api_response = api_instance.teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> update_team(team_name, body)

Updated team

This can only be done by the logged in user.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamsApi()
team_name = 'team_name_example' # str | Team that need to be updated
body = swagger_client.Team() # Team | Updated team object

try: 
    # Updated team
    api_instance.update_team(team_name, body)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_name** | **str**| Team that need to be updated | 
 **body** | [**Team**](Team.md)| Updated team object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

