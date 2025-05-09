# ZSGF.Client.AccessTokenApi

All URIs are relative to *https://api.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_token_delete**](AccessTokenApi.md#access_token_delete) | **DELETE** /AccessToken/{appKey}/{id} | 删除令牌
[**access_token_post**](AccessTokenApi.md#access_token_post) | **POST** /AccessToken/{appKey} | 创建令牌
[**access_token_put**](AccessTokenApi.md#access_token_put) | **PUT** /AccessToken/{appKey}/{id} | 更新令牌
[**access_tokens**](AccessTokenApi.md#access_tokens) | **GET** /AccessToken/{appKey} | 令牌列表


# **access_token_delete**
> BooleanApiResponse access_token_delete(id, app_key)

删除令牌

删除用户令牌

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
    api_instance = ZSGF.Client.AccessTokenApi(api_client)
    id = 56 # int | 令牌ID
    app_key = 'app_key_example' # str | 

    try:
        # 删除令牌
        api_response = api_instance.access_token_delete(id, app_key)
        print("The response of AccessTokenApi->access_token_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessTokenApi->access_token_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 令牌ID | 
 **app_key** | **str**|  | 

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

# **access_token_post**
> TokenModelApiResponse access_token_post(app_key, access_token_post_request=access_token_post_request)

创建令牌

创建新的用户令牌

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.access_token_post_request import AccessTokenPostRequest
from ZSGF.Client.models.token_model_api_response import TokenModelApiResponse
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
    api_instance = ZSGF.Client.AccessTokenApi(api_client)
    app_key = 'app_key_example' # str | 
    access_token_post_request = ZSGF.Client.AccessTokenPostRequest() # AccessTokenPostRequest | 令牌创建请求参数 (optional)

    try:
        # 创建令牌
        api_response = api_instance.access_token_post(app_key, access_token_post_request=access_token_post_request)
        print("The response of AccessTokenApi->access_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessTokenApi->access_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **access_token_post_request** | [**AccessTokenPostRequest**](AccessTokenPostRequest.md)| 令牌创建请求参数 | [optional] 

### Return type

[**TokenModelApiResponse**](TokenModelApiResponse.md)

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

# **access_token_put**
> BooleanApiResponse access_token_put(id, app_key, access_token_put_request=access_token_put_request)

更新令牌

更新现有的用户令牌

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.access_token_put_request import AccessTokenPutRequest
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
    api_instance = ZSGF.Client.AccessTokenApi(api_client)
    id = 56 # int | 令牌ID
    app_key = 'app_key_example' # str | 
    access_token_put_request = ZSGF.Client.AccessTokenPutRequest() # AccessTokenPutRequest | 令牌更新请求参数 (optional)

    try:
        # 更新令牌
        api_response = api_instance.access_token_put(id, app_key, access_token_put_request=access_token_put_request)
        print("The response of AccessTokenApi->access_token_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessTokenApi->access_token_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 令牌ID | 
 **app_key** | **str**|  | 
 **access_token_put_request** | [**AccessTokenPutRequest**](AccessTokenPutRequest.md)| 令牌更新请求参数 | [optional] 

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

# **access_tokens**
> AccessTokenListResultApiResponse access_tokens(app_key, user_id=user_id, skip=skip, take=take)

令牌列表

获取用户令牌列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.access_token_list_result_api_response import AccessTokenListResultApiResponse
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
    api_instance = ZSGF.Client.AccessTokenApi(api_client)
    app_key = 'app_key_example' # str | 
    user_id = 56 # int | 用户ID (optional)
    skip = 56 # int | 跳过的记录数 (optional)
    take = 56 # int | 获取的记录数 (optional)

    try:
        # 令牌列表
        api_response = api_instance.access_tokens(app_key, user_id=user_id, skip=skip, take=take)
        print("The response of AccessTokenApi->access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessTokenApi->access_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **user_id** | **int**| 用户ID | [optional] 
 **skip** | **int**| 跳过的记录数 | [optional] 
 **take** | **int**| 获取的记录数 | [optional] 

### Return type

[**AccessTokenListResultApiResponse**](AccessTokenListResultApiResponse.md)

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

