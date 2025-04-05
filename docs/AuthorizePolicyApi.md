# ZSGF.Client.AuthorizePolicyApi

All URIs are relative to *https://api.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_policies**](AuthorizePolicyApi.md#authorize_policies) | **GET** /AuthorizePolicy/{appKey} | 获取鉴权策略列表
[**authorize_policy**](AuthorizePolicyApi.md#authorize_policy) | **GET** /AuthorizePolicy/{appKey}/{id} | 获取鉴权策略详情
[**authorize_policy_delete**](AuthorizePolicyApi.md#authorize_policy_delete) | **DELETE** /AuthorizePolicy/{appKey}/{id} | 删除鉴权策略
[**authorize_policy_post**](AuthorizePolicyApi.md#authorize_policy_post) | **POST** /AuthorizePolicy/{appKey} | 添加鉴权策略
[**authorize_policy_put**](AuthorizePolicyApi.md#authorize_policy_put) | **PUT** /AuthorizePolicy/{appKey}/{id} | 更新鉴权策略


# **authorize_policies**
> AuthorizePolicyListApiResponse authorize_policies(app_key, auth_type=auth_type, policy_name=policy_name)

获取鉴权策略列表

根据鉴权类型和策略名称获取鉴权策略列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.authorize_policy_list_api_response import AuthorizePolicyListApiResponse
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
    api_instance = ZSGF.Client.AuthorizePolicyApi(api_client)
    app_key = 'app_key_example' # str | 
    auth_type = 'auth_type_example' # str | 鉴权类型（access_token、user、role） (optional)
    policy_name = 'policy_name_example' # str | 策略名称 (optional)

    try:
        # 获取鉴权策略列表
        api_response = api_instance.authorize_policies(app_key, auth_type=auth_type, policy_name=policy_name)
        print("The response of AuthorizePolicyApi->authorize_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizePolicyApi->authorize_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **auth_type** | **str**| 鉴权类型（access_token、user、role） | [optional] 
 **policy_name** | **str**| 策略名称 | [optional] 

### Return type

[**AuthorizePolicyListApiResponse**](AuthorizePolicyListApiResponse.md)

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

# **authorize_policy**
> AuthorizePolicyApiResponse authorize_policy(id, app_key)

获取鉴权策略详情

根据鉴权策略ID获取鉴权策略详情

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.authorize_policy_api_response import AuthorizePolicyApiResponse
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
    api_instance = ZSGF.Client.AuthorizePolicyApi(api_client)
    id = 56 # int | 鉴权策略ID
    app_key = 'app_key_example' # str | 

    try:
        # 获取鉴权策略详情
        api_response = api_instance.authorize_policy(id, app_key)
        print("The response of AuthorizePolicyApi->authorize_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizePolicyApi->authorize_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 鉴权策略ID | 
 **app_key** | **str**|  | 

### Return type

[**AuthorizePolicyApiResponse**](AuthorizePolicyApiResponse.md)

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

# **authorize_policy_delete**
> BooleanApiResponse authorize_policy_delete(id, app_key)

删除鉴权策略

根据鉴权策略ID删除鉴权策略

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
    api_instance = ZSGF.Client.AuthorizePolicyApi(api_client)
    id = 56 # int | 鉴权策略ID
    app_key = 'app_key_example' # str | 

    try:
        # 删除鉴权策略
        api_response = api_instance.authorize_policy_delete(id, app_key)
        print("The response of AuthorizePolicyApi->authorize_policy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizePolicyApi->authorize_policy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 鉴权策略ID | 
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

# **authorize_policy_post**
> CreatePostResultApiResponse authorize_policy_post(app_key, authorize_policy=authorize_policy)

添加鉴权策略

添加新的鉴权策略

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.authorize_policy import AuthorizePolicy
from ZSGF.Client.models.create_post_result_api_response import CreatePostResultApiResponse
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
    api_instance = ZSGF.Client.AuthorizePolicyApi(api_client)
    app_key = 'app_key_example' # str | 
    authorize_policy = ZSGF.Client.AuthorizePolicy() # AuthorizePolicy | 鉴权策略对象 (optional)

    try:
        # 添加鉴权策略
        api_response = api_instance.authorize_policy_post(app_key, authorize_policy=authorize_policy)
        print("The response of AuthorizePolicyApi->authorize_policy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizePolicyApi->authorize_policy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **authorize_policy** | [**AuthorizePolicy**](AuthorizePolicy.md)| 鉴权策略对象 | [optional] 

### Return type

[**CreatePostResultApiResponse**](CreatePostResultApiResponse.md)

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

# **authorize_policy_put**
> BooleanApiResponse authorize_policy_put(id, app_key, authorize_policy=authorize_policy)

更新鉴权策略

根据鉴权策略ID更新鉴权策略

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.authorize_policy import AuthorizePolicy
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
    api_instance = ZSGF.Client.AuthorizePolicyApi(api_client)
    id = 56 # int | 鉴权策略ID
    app_key = 'app_key_example' # str | 
    authorize_policy = ZSGF.Client.AuthorizePolicy() # AuthorizePolicy | 鉴权策略对象 (optional)

    try:
        # 更新鉴权策略
        api_response = api_instance.authorize_policy_put(id, app_key, authorize_policy=authorize_policy)
        print("The response of AuthorizePolicyApi->authorize_policy_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizePolicyApi->authorize_policy_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 鉴权策略ID | 
 **app_key** | **str**|  | 
 **authorize_policy** | [**AuthorizePolicy**](AuthorizePolicy.md)| 鉴权策略对象 | [optional] 

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

