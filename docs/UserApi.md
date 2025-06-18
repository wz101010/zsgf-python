# ZSGF.Client.UserApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_deactivate_hard**](UserApi.md#user_deactivate_hard) | **DELETE** /User/{appKey}/DeactivateHard | 注销账号
[**user_email_sign_in**](UserApi.md#user_email_sign_in) | **POST** /User/{appKey}/EmailSignIn | 邮箱登录
[**user_email_sign_up**](UserApi.md#user_email_sign_up) | **POST** /User/{appKey}/EmailSignUp | 邮箱注册
[**user_phone_sign_in**](UserApi.md#user_phone_sign_in) | **POST** /User/{appKey}/PhoneSignIn | 手机登录
[**user_phone_sign_up**](UserApi.md#user_phone_sign_up) | **POST** /User/{appKey}/PhoneSignUp | 手机注册
[**user_profile**](UserApi.md#user_profile) | **GET** /User/{appKey}/Profile | 获取个人资料
[**user_reset_email**](UserApi.md#user_reset_email) | **PUT** /User/{appKey}/ResetEmail | 重置邮箱
[**user_reset_phone**](UserApi.md#user_reset_phone) | **PUT** /User/{appKey}/ResetPhone | 重置手机号
[**user_reset_pwd**](UserApi.md#user_reset_pwd) | **POST** /User/{appKey}/ResetPwd | 重置密码
[**user_send_email_code**](UserApi.md#user_send_email_code) | **POST** /User/{appKey}/SendEmailCode | 发送邮箱验证码
[**user_send_sms_code**](UserApi.md#user_send_sms_code) | **POST** /User/{appKey}/SendSMSCode | 发送手机验证码
[**user_sign_in**](UserApi.md#user_sign_in) | **POST** /User/{appKey}/SignIn | 密码登录
[**user_sign_up**](UserApi.md#user_sign_up) | **POST** /User/{appKey}/SignUp | 账号注册
[**user_two_factor_auth**](UserApi.md#user_two_factor_auth) | **GET** /User/{appKey}/TwoFactorAuth | 二次验证
[**user_union_id_sign_in**](UserApi.md#user_union_id_sign_in) | **POST** /User/{appKey}/UnionIDSignIn | UnionID登录
[**user_union_id_sign_up**](UserApi.md#user_union_id_sign_up) | **POST** /User/{appKey}/UnionIDSignUp | UnionID注册
[**user_update_profile**](UserApi.md#user_update_profile) | **PUT** /User/{appKey}/Profile | 更新个人资料


# **user_deactivate_hard**
> BooleanApiResponse user_deactivate_hard(app_key)

注销账号

清除用户所有附属数据，并注销账号

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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 注销账号
        api_response = api_instance.user_deactivate_hard(app_key)
        print("The response of UserApi->user_deactivate_hard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_deactivate_hard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **user_email_sign_in**
> TokenModelApiResponse user_email_sign_in(app_key, email_sign_in_request=email_sign_in_request)

邮箱登录

使用邮箱进行登录

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.email_sign_in_request import EmailSignInRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    email_sign_in_request = ZSGF.Client.EmailSignInRequest() # EmailSignInRequest | 登录请求参数 (optional)

    try:
        # 邮箱登录
        api_response = api_instance.user_email_sign_in(app_key, email_sign_in_request=email_sign_in_request)
        print("The response of UserApi->user_email_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_email_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **email_sign_in_request** | [**EmailSignInRequest**](EmailSignInRequest.md)| 登录请求参数 | [optional] 

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

# **user_email_sign_up**
> TokenModelApiResponse user_email_sign_up(app_key, email_sign_up_request=email_sign_up_request)

邮箱注册

使用邮箱进行注册

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.email_sign_up_request import EmailSignUpRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    email_sign_up_request = ZSGF.Client.EmailSignUpRequest() # EmailSignUpRequest | 注册请求参数 (optional)

    try:
        # 邮箱注册
        api_response = api_instance.user_email_sign_up(app_key, email_sign_up_request=email_sign_up_request)
        print("The response of UserApi->user_email_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_email_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **email_sign_up_request** | [**EmailSignUpRequest**](EmailSignUpRequest.md)| 注册请求参数 | [optional] 

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

# **user_phone_sign_in**
> TokenModelApiResponse user_phone_sign_in(app_key, phone_sign_in_request=phone_sign_in_request)

手机登录

使用手机号码进行登录

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.phone_sign_in_request import PhoneSignInRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    phone_sign_in_request = ZSGF.Client.PhoneSignInRequest() # PhoneSignInRequest | 登录请求参数 (optional)

    try:
        # 手机登录
        api_response = api_instance.user_phone_sign_in(app_key, phone_sign_in_request=phone_sign_in_request)
        print("The response of UserApi->user_phone_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_phone_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **phone_sign_in_request** | [**PhoneSignInRequest**](PhoneSignInRequest.md)| 登录请求参数 | [optional] 

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

# **user_phone_sign_up**
> TokenModelApiResponse user_phone_sign_up(app_key, phone_sign_up_request=phone_sign_up_request)

手机注册

使用手机号码进行注册

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.phone_sign_up_request import PhoneSignUpRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    phone_sign_up_request = ZSGF.Client.PhoneSignUpRequest() # PhoneSignUpRequest | 注册请求参数 (optional)

    try:
        # 手机注册
        api_response = api_instance.user_phone_sign_up(app_key, phone_sign_up_request=phone_sign_up_request)
        print("The response of UserApi->user_phone_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_phone_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **phone_sign_up_request** | [**PhoneSignUpRequest**](PhoneSignUpRequest.md)| 注册请求参数 | [optional] 

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

# **user_profile**
> UserProfileResultApiResponse user_profile(app_key)

获取个人资料

获取当前用户的个人资料

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_profile_result_api_response import UserProfileResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 获取个人资料
        api_response = api_instance.user_profile(app_key)
        print("The response of UserApi->user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 

### Return type

[**UserProfileResultApiResponse**](UserProfileResultApiResponse.md)

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

# **user_reset_email**
> BooleanApiResponse user_reset_email(app_key, app_user_reset_email_request=app_user_reset_email_request)

重置邮箱

通过邮箱验证码重置邮箱

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.app_user_reset_email_request import AppUserResetEmailRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    app_user_reset_email_request = ZSGF.Client.AppUserResetEmailRequest() # AppUserResetEmailRequest | 重置邮箱的请求参数 (optional)

    try:
        # 重置邮箱
        api_response = api_instance.user_reset_email(app_key, app_user_reset_email_request=app_user_reset_email_request)
        print("The response of UserApi->user_reset_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_reset_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **app_user_reset_email_request** | [**AppUserResetEmailRequest**](AppUserResetEmailRequest.md)| 重置邮箱的请求参数 | [optional] 

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

# **user_reset_phone**
> BooleanApiResponse user_reset_phone(app_key, app_user_reset_phone_request=app_user_reset_phone_request)

重置手机号

通过手机号验证码重置手机号

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.app_user_reset_phone_request import AppUserResetPhoneRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    app_user_reset_phone_request = ZSGF.Client.AppUserResetPhoneRequest() # AppUserResetPhoneRequest | 重置手机号的请求参数 (optional)

    try:
        # 重置手机号
        api_response = api_instance.user_reset_phone(app_key, app_user_reset_phone_request=app_user_reset_phone_request)
        print("The response of UserApi->user_reset_phone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_reset_phone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **app_user_reset_phone_request** | [**AppUserResetPhoneRequest**](AppUserResetPhoneRequest.md)| 重置手机号的请求参数 | [optional] 

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

# **user_reset_pwd**
> BooleanApiResponse user_reset_pwd(app_key, app_user_reset_pwd_request=app_user_reset_pwd_request)

重置密码

通过手机号或邮箱重置密码

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.app_user_reset_pwd_request import AppUserResetPwdRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    app_user_reset_pwd_request = ZSGF.Client.AppUserResetPwdRequest() # AppUserResetPwdRequest | 重置密码的请求参数 (optional)

    try:
        # 重置密码
        api_response = api_instance.user_reset_pwd(app_key, app_user_reset_pwd_request=app_user_reset_pwd_request)
        print("The response of UserApi->user_reset_pwd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_reset_pwd: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **app_user_reset_pwd_request** | [**AppUserResetPwdRequest**](AppUserResetPwdRequest.md)| 重置密码的请求参数 | [optional] 

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

# **user_send_email_code**
> BooleanApiResponse user_send_email_code(app_key, send_email_code_request=send_email_code_request)

发送邮箱验证码

发送邮箱验证码用于注册或找回密码

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.send_email_code_request import SendEmailCodeRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    send_email_code_request = ZSGF.Client.SendEmailCodeRequest() # SendEmailCodeRequest | 发送邮箱验证码的请求参数 (optional)

    try:
        # 发送邮箱验证码
        api_response = api_instance.user_send_email_code(app_key, send_email_code_request=send_email_code_request)
        print("The response of UserApi->user_send_email_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_send_email_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **send_email_code_request** | [**SendEmailCodeRequest**](SendEmailCodeRequest.md)| 发送邮箱验证码的请求参数 | [optional] 

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

# **user_send_sms_code**
> BooleanApiResponse user_send_sms_code(app_key, send_sms_code_request=send_sms_code_request)

发送手机验证码

发送手机验证码用于注册或找回密码

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.send_sms_code_request import SendSMSCodeRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    send_sms_code_request = ZSGF.Client.SendSMSCodeRequest() # SendSMSCodeRequest | 发送手机验证码的请求参数 (optional)

    try:
        # 发送手机验证码
        api_response = api_instance.user_send_sms_code(app_key, send_sms_code_request=send_sms_code_request)
        print("The response of UserApi->user_send_sms_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_send_sms_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **send_sms_code_request** | [**SendSMSCodeRequest**](SendSMSCodeRequest.md)| 发送手机验证码的请求参数 | [optional] 

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

# **user_sign_in**
> TokenModelApiResponse user_sign_in(app_key, sign_in_request=sign_in_request)

密码登录

使用账号密码进行登录

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.sign_in_request import SignInRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    sign_in_request = ZSGF.Client.SignInRequest() # SignInRequest | 登录请求参数 (optional)

    try:
        # 密码登录
        api_response = api_instance.user_sign_in(app_key, sign_in_request=sign_in_request)
        print("The response of UserApi->user_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **sign_in_request** | [**SignInRequest**](SignInRequest.md)| 登录请求参数 | [optional] 

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

# **user_sign_up**
> TokenModelApiResponse user_sign_up(app_key, sign_up_request=sign_up_request)

账号注册

使用账号密码进行注册

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.sign_up_request import SignUpRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    sign_up_request = ZSGF.Client.SignUpRequest() # SignUpRequest | 注册请求参数 (optional)

    try:
        # 账号注册
        api_response = api_instance.user_sign_up(app_key, sign_up_request=sign_up_request)
        print("The response of UserApi->user_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **sign_up_request** | [**SignUpRequest**](SignUpRequest.md)| 注册请求参数 | [optional] 

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

# **user_two_factor_auth**
> SetupCodeApiResponse user_two_factor_auth(app_key)

二次验证

获取当前用户在指定应用下启用二次验证（2FA）所需的设置信息，主要包括二维码链接和手动密钥，用户可以将其录入在 Google Authenticator 等 TOTP 应用中，用于后续动态验证码验证。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.setup_code_api_response import SetupCodeApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 二次验证
        api_response = api_instance.user_two_factor_auth(app_key)
        print("The response of UserApi->user_two_factor_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_two_factor_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 

### Return type

[**SetupCodeApiResponse**](SetupCodeApiResponse.md)

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

# **user_union_id_sign_in**
> TokenModelApiResponse user_union_id_sign_in(app_key, union_id_sign_in_request=union_id_sign_in_request)

UnionID登录

使用UnionID进行登录

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.token_model_api_response import TokenModelApiResponse
from ZSGF.Client.models.union_id_sign_in_request import UnionIDSignInRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    union_id_sign_in_request = ZSGF.Client.UnionIDSignInRequest() # UnionIDSignInRequest | 登录请求参数 (optional)

    try:
        # UnionID登录
        api_response = api_instance.user_union_id_sign_in(app_key, union_id_sign_in_request=union_id_sign_in_request)
        print("The response of UserApi->user_union_id_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_union_id_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **union_id_sign_in_request** | [**UnionIDSignInRequest**](UnionIDSignInRequest.md)| 登录请求参数 | [optional] 

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

# **user_union_id_sign_up**
> TokenModelApiResponse user_union_id_sign_up(app_key, union_id_sign_up_request=union_id_sign_up_request)

UnionID注册

使用UnionID进行注册

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.token_model_api_response import TokenModelApiResponse
from ZSGF.Client.models.union_id_sign_up_request import UnionIDSignUpRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    union_id_sign_up_request = ZSGF.Client.UnionIDSignUpRequest() # UnionIDSignUpRequest | 注册请求参数 (optional)

    try:
        # UnionID注册
        api_response = api_instance.user_union_id_sign_up(app_key, union_id_sign_up_request=union_id_sign_up_request)
        print("The response of UserApi->user_union_id_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_union_id_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **union_id_sign_up_request** | [**UnionIDSignUpRequest**](UnionIDSignUpRequest.md)| 注册请求参数 | [optional] 

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

# **user_update_profile**
> BooleanApiResponse user_update_profile(app_key, update_profile_request=update_profile_request)

更新个人资料

更新当前用户的个人资料

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.update_profile_request import UpdateProfileRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    update_profile_request = ZSGF.Client.UpdateProfileRequest() # UpdateProfileRequest | 更新个人资料的请求参数 (optional)

    try:
        # 更新个人资料
        api_response = api_instance.user_update_profile(app_key, update_profile_request=update_profile_request)
        print("The response of UserApi->user_update_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_update_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **update_profile_request** | [**UpdateProfileRequest**](UpdateProfileRequest.md)| 更新个人资料的请求参数 | [optional] 

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

