# swagger_client.PlayersApi

All URIs are relative to *http://https://snc-api.herokuapp.com//v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**players**](PlayersApi.md#players) | **GET** /players | All players league wide
[**save_player**](PlayersApi.md#save_player) | **POST** /players | Save a player


# **players**
> list[Player] players()

All players league wide

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlayersApi()

try: 
    # All players league wide
    api_response = api_instance.players()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->players: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Player]**](Player.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_player**
> save_player(body)

Save a player

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
api_instance = swagger_client.PlayersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Player() # Player | The player to save

try: 
    # Save a player
    api_instance.save_player(body)
except ApiException as e:
    print("Exception when calling PlayersApi->save_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Player**](Player.md)| The player to save | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

