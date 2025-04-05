# ZSGF.Client.TeamApi

All URIs are relative to *https://api.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_delete**](TeamApi.md#team_delete) | **DELETE** /Team/{id} | 删除团队
[**team_post**](TeamApi.md#team_post) | **POST** /Team | 创建团队
[**team_put**](TeamApi.md#team_put) | **PUT** /Team/{id} | 更新团队信息
[**teams**](TeamApi.md#teams) | **GET** /Team | 获取团队列表


# **team_delete**
> BooleanApiResponse team_delete(id)

删除团队

根据团队ID删除团队

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.TeamApi(api_client)
    id = 56 # int | 团队ID

    try:
        # 删除团队
        api_response = api_instance.team_delete(id)
        print("The response of TeamApi->team_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->team_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 团队ID | 

### Return type

[**BooleanApiResponse**](BooleanApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_post**
> BooleanApiResponse team_post(team=team)

创建团队

创建一个新的团队

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.team import Team
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.TeamApi(api_client)
    team = ZSGF.Client.Team() # Team | 团队信息 (optional)

    try:
        # 创建团队
        api_response = api_instance.team_post(team=team)
        print("The response of TeamApi->team_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->team_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | [**Team**](Team.md)| 团队信息 | [optional] 

### Return type

[**BooleanApiResponse**](BooleanApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_put**
> BooleanApiResponse team_put(id, team=team)

更新团队信息

根据团队ID更新团队信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.team import Team
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.TeamApi(api_client)
    id = 56 # int | 团队ID
    team = ZSGF.Client.Team() # Team | 团队信息 (optional)

    try:
        # 更新团队信息
        api_response = api_instance.team_put(id, team=team)
        print("The response of TeamApi->team_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->team_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 团队ID | 
 **team** | [**Team**](Team.md)| 团队信息 | [optional] 

### Return type

[**BooleanApiResponse**](BooleanApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams**
> ListResponseItemListApiResponse teams(channel_code=channel_code, channel_app_id=channel_app_id)

获取团队列表

根据渠道代码和渠道应用ID获取团队列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.list_response_item_list_api_response import ListResponseItemListApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api.zashigaofa.cn"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = ZSGF.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ZSGF.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ZSGF.Client.TeamApi(api_client)
    channel_code = 'channel_code_example' # str | 渠道代码 (optional)
    channel_app_id = 'channel_app_id_example' # str | 渠道应用ID (optional)

    try:
        # 获取团队列表
        api_response = api_instance.teams(channel_code=channel_code, channel_app_id=channel_app_id)
        print("The response of TeamApi->teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_code** | **str**| 渠道代码 | [optional] 
 **channel_app_id** | **str**| 渠道应用ID | [optional] 

### Return type

[**ListResponseItemListApiResponse**](ListResponseItemListApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

