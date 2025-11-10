# ZSGF.Client.ExternalAccountApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_account_sign_in**](ExternalAccountApi.md#external_account_sign_in) | **POST** /ExternalAccount/{appKey}/SignIn | 外部账号登录
[**user_external_account_bind**](ExternalAccountApi.md#user_external_account_bind) | **POST** /ExternalAccount/{appKey} | 绑定外部账号
[**user_o_auth_accounts**](ExternalAccountApi.md#user_o_auth_accounts) | **GET** /ExternalAccount/{appKey} | 外部账号列表
[**user_o_auth_accounts_put_bind**](ExternalAccountApi.md#user_o_auth_accounts_put_bind) | **PUT** /ExternalAccount/{appKey}/{id} | 更新绑定账号
[**user_o_auth_accounts_un_bind**](ExternalAccountApi.md#user_o_auth_accounts_un_bind) | **DELETE** /ExternalAccount/{appKey}/{id} | 删除绑定账号


# **external_account_sign_in**
> TokenModelApiResponse external_account_sign_in(app_key, user_id=user_id, external_account_sign_in_request=external_account_sign_in_request)

外部账号登录

使用外部账号登录应用

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.external_account_sign_in_request import ExternalAccountSignInRequest
from ZSGF.Client.models.token_model_api_response import TokenModelApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
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
    api_instance = ZSGF.Client.ExternalAccountApi(api_client)
    app_key = 'app_key_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    external_account_sign_in_request = ZSGF.Client.ExternalAccountSignInRequest() # ExternalAccountSignInRequest | 登录请求参数 (optional)

    try:
        # 外部账号登录
        api_response = api_instance.external_account_sign_in(app_key, user_id=user_id, external_account_sign_in_request=external_account_sign_in_request)
        print("The response of ExternalAccountApi->external_account_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAccountApi->external_account_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **external_account_sign_in_request** | [**ExternalAccountSignInRequest**](ExternalAccountSignInRequest.md)| 登录请求参数 | [optional] 

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

# **user_external_account_bind**
> BooleanApiResponse user_external_account_bind(app_key, user_id=user_id, external_account_bind_request=external_account_bind_request)

绑定外部账号

绑定外部账号，如果已存在绑定则直接返回成功

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.external_account_bind_request import ExternalAccountBindRequest
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
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
    api_instance = ZSGF.Client.ExternalAccountApi(api_client)
    app_key = 'app_key_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    external_account_bind_request = ZSGF.Client.ExternalAccountBindRequest() # ExternalAccountBindRequest | 绑定请求参数 (optional)

    try:
        # 绑定外部账号
        api_response = api_instance.user_external_account_bind(app_key, user_id=user_id, external_account_bind_request=external_account_bind_request)
        print("The response of ExternalAccountApi->user_external_account_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAccountApi->user_external_account_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **external_account_bind_request** | [**ExternalAccountBindRequest**](ExternalAccountBindRequest.md)| 绑定请求参数 | [optional] 

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

# **user_o_auth_accounts**
> UserLoginsListApiResponse user_o_auth_accounts(app_key, user_id=user_id)

外部账号列表

获取绑定成功的外部账号列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_logins_list_api_response import UserLoginsListApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
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
    api_instance = ZSGF.Client.ExternalAccountApi(api_client)
    app_key = 'app_key_example' # str | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        # 外部账号列表
        api_response = api_instance.user_o_auth_accounts(app_key, user_id=user_id)
        print("The response of ExternalAccountApi->user_o_auth_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAccountApi->user_o_auth_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **user_id** | **str**|  | [optional] 

### Return type

[**UserLoginsListApiResponse**](UserLoginsListApiResponse.md)

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

# **user_o_auth_accounts_put_bind**
> BooleanApiResponse user_o_auth_accounts_put_bind(id, app_key, user_id=user_id, external_account_put_request=external_account_put_request)

更新绑定账号

更新绑定的账号信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.external_account_put_request import ExternalAccountPutRequest
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
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
    api_instance = ZSGF.Client.ExternalAccountApi(api_client)
    id = 56 # int | 绑定ID
    app_key = 'app_key_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    external_account_put_request = ZSGF.Client.ExternalAccountPutRequest() # ExternalAccountPutRequest | 更新请求参数 (optional)

    try:
        # 更新绑定账号
        api_response = api_instance.user_o_auth_accounts_put_bind(id, app_key, user_id=user_id, external_account_put_request=external_account_put_request)
        print("The response of ExternalAccountApi->user_o_auth_accounts_put_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAccountApi->user_o_auth_accounts_put_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 绑定ID | 
 **app_key** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **external_account_put_request** | [**ExternalAccountPutRequest**](ExternalAccountPutRequest.md)| 更新请求参数 | [optional] 

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

# **user_o_auth_accounts_un_bind**
> BooleanApiResponse user_o_auth_accounts_un_bind(id, app_key, user_id=user_id)

删除绑定账号

删除绑定的外部账号

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-dev.zashigaofa.cn
# See configuration.py for a list of all supported configuration parameters.
configuration = ZSGF.Client.Configuration(
    host = "https://api-dev.zashigaofa.cn"
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
    api_instance = ZSGF.Client.ExternalAccountApi(api_client)
    id = 56 # int | 绑定ID
    app_key = 'app_key_example' # str | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        # 删除绑定账号
        api_response = api_instance.user_o_auth_accounts_un_bind(id, app_key, user_id=user_id)
        print("The response of ExternalAccountApi->user_o_auth_accounts_un_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAccountApi->user_o_auth_accounts_un_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 绑定ID | 
 **app_key** | **str**|  | 
 **user_id** | **str**|  | [optional] 

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

