# swagger_client.GoaliesApi

All URIs are relative to *http://https://snc-api.herokuapp.com//v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**goalies**](GoaliesApi.md#goalies) | **GET** /goalies | All goalies league wide
[**save_goalie**](GoaliesApi.md#save_goalie) | **POST** /goalies | Save a goalie


# **goalies**
> list[Goalie] goalies()

All goalies league wide

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GoaliesApi()

try: 
    # All goalies league wide
    api_response = api_instance.goalies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoaliesApi->goalies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Goalie]**](Goalie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_goalie**
> save_goalie(body)

Save a goalie

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GoaliesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Goalie() # Goalie | The goalie to save

try: 
    # Save a goalie
    api_instance.save_goalie(body)
except ApiException as e:
    print("Exception when calling GoaliesApi->save_goalie: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Goalie**](Goalie.md)| The goalie to save | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

