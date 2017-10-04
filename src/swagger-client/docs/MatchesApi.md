# swagger_client.MatchesApi

All URIs are relative to *http://https://snc-api.herokuapp.com//v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_match**](MatchesApi.md#add_match) | **POST** /matches | Add a new match
[**find_match**](MatchesApi.md#find_match) | **GET** /matches/{matchId} | Get a specific match
[**find_team_schedule**](MatchesApi.md#find_team_schedule) | **GET** /matches/team/{teamName} | Find this season&#39;s schedule for a given team
[**match_summary**](MatchesApi.md#match_summary) | **GET** /matches/{matchId}/summary | Get a specific match
[**save_match_summary**](MatchesApi.md#save_match_summary) | **PUT** /matches/{matchId}/summary | Update the match summary
[**season_matches**](MatchesApi.md#season_matches) | **GET** /matches | Get the current season&#39;s matches
[**update_match**](MatchesApi.md#update_match) | **PUT** /matches/{matchId} | Update an existing match


# **add_match**
> add_match(body)

Add a new match



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
api_instance = swagger_client.MatchesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Match() # Match | Match object that needs to be added to the system

try: 
    # Add a new match
    api_instance.add_match(body)
except ApiException as e:
    print("Exception when calling MatchesApi->add_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Match**](Match.md)| Match object that needs to be added to the system | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_match**
> Match find_match(match_id)

Get a specific match

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MatchesApi()
match_id = 56 # int | ID of the match to fetch

try: 
    # Get a specific match
    api_response = api_instance.find_match(match_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->find_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| ID of the match to fetch | 

### Return type

[**Match**](Match.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_team_schedule**
> list[Match] find_team_schedule(team_name)

Find this season's schedule for a given team

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MatchesApi()
team_name = 56 # int | Name of the team whose schedule should be fetched

try: 
    # Find this season's schedule for a given team
    api_response = api_instance.find_team_schedule(team_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->find_team_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_name** | **int**| Name of the team whose schedule should be fetched | 

### Return type

[**list[Match]**](Match.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_summary**
> MatchSummary match_summary(match_id)

Get a specific match

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MatchesApi()
match_id = 56 # int | ID of the match to fetch

try: 
    # Get a specific match
    api_response = api_instance.match_summary(match_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->match_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| ID of the match to fetch | 

### Return type

[**MatchSummary**](MatchSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_match_summary**
> save_match_summary(match_id, body)

Update the match summary

Used to update a match's summary. There is no POST because summaries are automatically generated when a match is created

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
api_instance = swagger_client.MatchesApi(swagger_client.ApiClient(configuration))
match_id = 56 # int | ID of the match to fetch
body = swagger_client.MatchSummary() # MatchSummary | Match summary that needs to be saved

try: 
    # Update the match summary
    api_instance.save_match_summary(match_id, body)
except ApiException as e:
    print("Exception when calling MatchesApi->save_match_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| ID of the match to fetch | 
 **body** | [**MatchSummary**](MatchSummary.md)| Match summary that needs to be saved | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **season_matches**
> list[Match] season_matches()

Get the current season's matches

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MatchesApi()

try: 
    # Get the current season's matches
    api_response = api_instance.season_matches()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->season_matches: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Match]**](Match.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_match**
> update_match(match_id, body)

Update an existing match



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
api_instance = swagger_client.MatchesApi(swagger_client.ApiClient(configuration))
match_id = 56 # int | ID of the match to update
body = swagger_client.Match() # Match | Match object that needs to be updated

try: 
    # Update an existing match
    api_instance.update_match(match_id, body)
except ApiException as e:
    print("Exception when calling MatchesApi->update_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| ID of the match to update | 
 **body** | [**Match**](Match.md)| Match object that needs to be updated | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

