# ZSGF.Client.OAuthApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth_authorize**](OAuthApi.md#o_auth_authorize) | **POST** /OAuth/{appKey}/Authorize | 获取访问令牌
[**o_auth_consents**](OAuthApi.md#o_auth_consents) | **GET** /OAuth/{appKey}/Consents | 获取授权记录
[**o_auth_delete_consent**](OAuthApi.md#o_auth_delete_consent) | **DELETE** /OAuth/{appKey}/Consents/{id} | 删除授权记录
[**o_auth_grant_code**](OAuthApi.md#o_auth_grant_code) | **POST** /OAuth/{appKey}/GrantCode | 获取授权码
[**o_auth_profile**](OAuthApi.md#o_auth_profile) | **GET** /OAuth/{appKey}/Profile | 获取用户资料


# **o_auth_authorize**
> AuthorizeResultApiResponse o_auth_authorize(app_key, scheme=scheme, code=code)

获取访问令牌

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.authorize_result_api_response import AuthorizeResultApiResponse
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
    api_instance = ZSGF.Client.OAuthApi(api_client)
    app_key = 'app_key_example' # str | 
    scheme = 'scheme_example' # str | 身份源 (optional)
    code = 'code_example' # str | 授权码 (optional)

    try:
        # 获取访问令牌
        api_response = api_instance.o_auth_authorize(app_key, scheme=scheme, code=code)
        print("The response of OAuthApi->o_auth_authorize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->o_auth_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **scheme** | **str**| 身份源 | [optional] 
 **code** | **str**| 授权码 | [optional] 

### Return type

[**AuthorizeResultApiResponse**](AuthorizeResultApiResponse.md)

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

# **o_auth_consents**
> AppUserConsentModelListApiResponse o_auth_consents(app_key)

获取授权记录

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.app_user_consent_model_list_api_response import AppUserConsentModelListApiResponse
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
    api_instance = ZSGF.Client.OAuthApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 获取授权记录
        api_response = api_instance.o_auth_consents(app_key)
        print("The response of OAuthApi->o_auth_consents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->o_auth_consents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 

### Return type

[**AppUserConsentModelListApiResponse**](AppUserConsentModelListApiResponse.md)

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

# **o_auth_delete_consent**
> BooleanApiResponse o_auth_delete_consent(id, app_key)

删除授权记录

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
    api_instance = ZSGF.Client.OAuthApi(api_client)
    id = 56 # int | 
    app_key = 'app_key_example' # str | 

    try:
        # 删除授权记录
        api_response = api_instance.o_auth_delete_consent(id, app_key)
        print("The response of OAuthApi->o_auth_delete_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->o_auth_delete_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
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

# **o_auth_grant_code**
> GrantResultApiResponse o_auth_grant_code(app_key, scheme=scheme, grant_request=grant_request)

获取授权码

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.grant_request import GrantRequest
from ZSGF.Client.models.grant_result_api_response import GrantResultApiResponse
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
    api_instance = ZSGF.Client.OAuthApi(api_client)
    app_key = 'app_key_example' # str | 
    scheme = 'scheme_example' # str | 身份源，固定填：app (optional)
    grant_request = ZSGF.Client.GrantRequest() # GrantRequest | 授权详情 (optional)

    try:
        # 获取授权码
        api_response = api_instance.o_auth_grant_code(app_key, scheme=scheme, grant_request=grant_request)
        print("The response of OAuthApi->o_auth_grant_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->o_auth_grant_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **scheme** | **str**| 身份源，固定填：app | [optional] 
 **grant_request** | [**GrantRequest**](GrantRequest.md)| 授权详情 | [optional] 

### Return type

[**GrantResultApiResponse**](GrantResultApiResponse.md)

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

# **o_auth_profile**
> ProfileResultApiResponse o_auth_profile(app_key)

获取用户资料

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.profile_result_api_response import ProfileResultApiResponse
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
    api_instance = ZSGF.Client.OAuthApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 获取用户资料
        api_response = api_instance.o_auth_profile(app_key)
        print("The response of OAuthApi->o_auth_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->o_auth_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 

### Return type

[**ProfileResultApiResponse**](ProfileResultApiResponse.md)

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

