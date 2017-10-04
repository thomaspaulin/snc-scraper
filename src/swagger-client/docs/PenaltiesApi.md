# swagger_client.PenaltiesApi

All URIs are relative to *http://https://snc-api.herokuapp.com//v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**penalties**](PenaltiesApi.md#penalties) | **GET** /penalties | All penalties for the season
[**save_penalty**](PenaltiesApi.md#save_penalty) | **POST** /penalties | Save a penalty


# **penalties**
> list[Penalty] penalties()

All penalties for the season

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PenaltiesApi()

try: 
    # All penalties for the season
    api_response = api_instance.penalties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PenaltiesApi->penalties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Penalty]**](Penalty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_penalty**
> save_penalty(body)

Save a penalty

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
api_instance = swagger_client.PenaltiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Penalty() # Penalty | The penalty to save

try: 
    # Save a penalty
    api_instance.save_penalty(body)
except ApiException as e:
    print("Exception when calling PenaltiesApi->save_penalty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Penalty**](Penalty.md)| The penalty to save | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

