# swagger_client.GoalsApi

All URIs are relative to *http://https://snc-api.herokuapp.com//v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**goals**](GoalsApi.md#goals) | **GET** /goals | All goals for the season
[**save_goal**](GoalsApi.md#save_goal) | **POST** /goals | Save a goal


# **goals**
> list[Goal] goals()

All goals for the season

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GoalsApi()

try: 
    # All goals for the season
    api_response = api_instance.goals()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->goals: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Goal]**](Goal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_goal**
> save_goal(body)

Save a goal

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
api_instance = swagger_client.GoalsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Goal() # Goal | The goal to save

try: 
    # Save a goal
    api_instance.save_goal(body)
except ApiException as e:
    print("Exception when calling GoalsApi->save_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Goal**](Goal.md)| The goal to save | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

