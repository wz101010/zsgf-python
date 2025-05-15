# ZSGF.Client.UserApi

All URIs are relative to *https://api.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user**](UserApi.md#user) | **GET** /User/{appKey}/{id} | 获取用户详情
[**user_clear**](UserApi.md#user_clear) | **DELETE** /User/{appKey}/Clear | 清空用户数据
[**user_common_interests**](UserApi.md#user_common_interests) | **GET** /User/{appKey}/Friends/CommonInterests | 有共同爱好的用户推荐
[**user_deactivate_hard**](UserApi.md#user_deactivate_hard) | **DELETE** /User/{appKey}/DeactivateHard | 注销账号
[**user_delete**](UserApi.md#user_delete) | **DELETE** /User/{appKey}/{id} | 删除用户
[**user_email_sign_in**](UserApi.md#user_email_sign_in) | **POST** /User/{appKey}/EmailSignIn | 邮箱登录
[**user_email_sign_up**](UserApi.md#user_email_sign_up) | **POST** /User/{appKey}/EmailSignUp | 邮箱注册
[**user_export**](UserApi.md#user_export) | **GET** /User/{appKey}/Export | 导出用户数据
[**user_follow_user**](UserApi.md#user_follow_user) | **POST** /User/{appKey}/Follower/{userId} | 关注用户
[**user_follower_put**](UserApi.md#user_follower_put) | **PUT** /User/{appKey}/Follower/{id} | 更新粉丝
[**user_followers**](UserApi.md#user_followers) | **GET** /User/{appKey}/Followers | 获取我的粉丝列表
[**user_following**](UserApi.md#user_following) | **GET** /User/{appKey}/Following | 获取当前用户的关注列表，或者判断是否关注某个特定用户。
[**user_friends_near_by**](UserApi.md#user_friends_near_by) | **GET** /User/{appKey}/Friends/NearBy | 获取附近的用户推荐列表
[**user_import**](UserApi.md#user_import) | **POST** /User/{appKey}/Import | 导入用户数据
[**user_location**](UserApi.md#user_location) | **GET** /User/{appKey}/Location/{id} | 获取位置详情
[**user_location_delete**](UserApi.md#user_location_delete) | **DELETE** /User/{appKey}/Location/{id} | 删除位置
[**user_location_post**](UserApi.md#user_location_post) | **POST** /User/{appKey}/Location | 添加位置
[**user_location_put**](UserApi.md#user_location_put) | **PUT** /User/{appKey}/Location/{id} | 更新位置
[**user_locations**](UserApi.md#user_locations) | **GET** /User/{appKey}/Locations | 获取位置列表
[**user_mutual_followers**](UserApi.md#user_mutual_followers) | **GET** /User/{appKey}/Friends/MutualFollowers | 有共同粉丝的用户推荐
[**user_mutual_followings**](UserApi.md#user_mutual_followings) | **GET** /User/{appKey}/Friends/MutualFollowings | 有共同关注的用户推荐
[**user_o_auth_account_bind**](UserApi.md#user_o_auth_account_bind) | **POST** /User/{appKey}/OAuthAccountBind | 外部账号 绑定，如果已存在绑定则直接返回成功
[**user_o_auth_account_sign_in**](UserApi.md#user_o_auth_account_sign_in) | **POST** /User/{appKey}/OAuthAccountSignIn | 外部账号 登录
[**user_o_auth_accounts**](UserApi.md#user_o_auth_accounts) | **GET** /User/{appKey}/OAuthAccounts | 外部账号 绑定列表
[**user_o_auth_accounts_put_bind**](UserApi.md#user_o_auth_accounts_put_bind) | **PUT** /User/{appKey}/OAuthAccounts/{id} | 外部账号 更新绑定
[**user_o_auth_accounts_un_bind**](UserApi.md#user_o_auth_accounts_un_bind) | **DELETE** /User/{appKey}/OAuthAccounts/{id} | 外部账号 删除绑定
[**user_phone_sign_in**](UserApi.md#user_phone_sign_in) | **POST** /User/{appKey}/PhoneSignIn | 手机登录
[**user_phone_sign_up**](UserApi.md#user_phone_sign_up) | **POST** /User/{appKey}/PhoneSignUp | 手机注册
[**user_profile**](UserApi.md#user_profile) | **GET** /User/{appKey}/Profile | 获取个人资料
[**user_profile_by_id**](UserApi.md#user_profile_by_id) | **GET** /User/{appKey}/Profile/{userId} | 获取指定用户资料
[**user_put**](UserApi.md#user_put) | **PUT** /User/{appKey}/{id} | 更新用户信息
[**user_qr_code_pre_sign_in**](UserApi.md#user_qr_code_pre_sign_in) | **POST** /User/{appKey}/QRCodePreSignIn | 微信小程序 - 预登陆
[**user_qr_code_scan**](UserApi.md#user_qr_code_scan) | **POST** /User/{appKey}/QRCodeScan | 微信小程序 - 扫码
[**user_qr_code_sign_in**](UserApi.md#user_qr_code_sign_in) | **POST** /User/{appKey}/QRCodeSignIn | 微信小程序 - 网页登录
[**user_qr_code_sign_up**](UserApi.md#user_qr_code_sign_up) | **POST** /User/{appKey}/QRCodeSignUp | 微信小程序 - 注册
[**user_reset_email**](UserApi.md#user_reset_email) | **PUT** /User/{appKey}/ResetEmail | 重置邮箱
[**user_reset_phone**](UserApi.md#user_reset_phone) | **PUT** /User/{appKey}/ResetPhone | 重置手机号
[**user_reset_pwd**](UserApi.md#user_reset_pwd) | **POST** /User/{appKey}/ResetPwd | 重置密码
[**user_send_email_code**](UserApi.md#user_send_email_code) | **POST** /User/{appKey}/SendEmailCode | 发送邮箱验证码
[**user_send_sms_code**](UserApi.md#user_send_sms_code) | **POST** /User/{appKey}/SendSMSCode | 发送手机验证码
[**user_sign_in**](UserApi.md#user_sign_in) | **POST** /User/{appKey}/SignIn | 账号密码 登录
[**user_sign_up**](UserApi.md#user_sign_up) | **POST** /User/{appKey}/SignUp | 账号密码 注册
[**user_two_factor_auth**](UserApi.md#user_two_factor_auth) | **GET** /User/{appKey}/TwoFactorAuth | 双因素验证
[**user_unfollow_user**](UserApi.md#user_unfollow_user) | **DELETE** /User/{appKey}/Follower/{userId} | 取消关注
[**user_union_id_sign_in**](UserApi.md#user_union_id_sign_in) | **POST** /User/{appKey}/UnionIDSignIn | UnionID登录
[**user_union_id_sign_up**](UserApi.md#user_union_id_sign_up) | **POST** /User/{appKey}/UnionIDSignUp | UnionID注册
[**user_update_profile**](UserApi.md#user_update_profile) | **PUT** /User/{appKey}/Profile | 更新个人资料
[**users**](UserApi.md#users) | **GET** /User/{appKey} | 获取用户列表


# **user**
> UserApiResponse user(id, app_key)

获取用户详情

根据用户ID获取用户详情

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_api_response import UserApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    id = 56 # int | 用户ID
    app_key = 'app_key_example' # str | 

    try:
        # 获取用户详情
        api_response = api_instance.user(id, app_key)
        print("The response of UserApi->user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 用户ID | 
 **app_key** | **str**|  | 

### Return type

[**UserApiResponse**](UserApiResponse.md)

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

# **user_clear**
> BooleanApiResponse user_clear(app_key)

清空用户数据

清空用户数据

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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 清空用户数据
        api_response = api_instance.user_clear(app_key)
        print("The response of UserApi->user_clear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_clear: %s\n" % e)
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

# **user_common_interests**
> UserCommonInterestsResultApiResponse user_common_interests(app_key, tag=tag, skip=skip, take=take)

有共同爱好的用户推荐

推荐有共同爱好的用户

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_common_interests_result_api_response import UserCommonInterestsResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str | 兴趣标签 (optional)
    skip = 0 # int | 跳过的记录数 (optional) (default to 0)
    take = 10 # int | 获取的记录数 (optional) (default to 10)

    try:
        # 有共同爱好的用户推荐
        api_response = api_instance.user_common_interests(app_key, tag=tag, skip=skip, take=take)
        print("The response of UserApi->user_common_interests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_common_interests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**| 兴趣标签 | [optional] 
 **skip** | **int**| 跳过的记录数 | [optional] [default to 0]
 **take** | **int**| 获取的记录数 | [optional] [default to 10]

### Return type

[**UserCommonInterestsResultApiResponse**](UserCommonInterestsResultApiResponse.md)

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

# **user_delete**
> BooleanApiResponse user_delete(id, app_key)

删除用户

根据用户ID删除用户

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
    api_instance = ZSGF.Client.UserApi(api_client)
    id = 56 # int | 用户ID
    app_key = 'app_key_example' # str | 

    try:
        # 删除用户
        api_response = api_instance.user_delete(id, app_key)
        print("The response of UserApi->user_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 用户ID | 
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

# **user_export**
> bytearray user_export(app_key)

导出用户数据

导出所有用户数据为Excel文件

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 导出用户数据
        api_response = api_instance.user_export(app_key)
        print("The response of UserApi->user_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_follow_user**
> BooleanApiResponse user_follow_user(user_id, app_key)

关注用户

关注指定用户

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
    api_instance = ZSGF.Client.UserApi(api_client)
    user_id = 56 # int | 要关注的用户ID
    app_key = 'app_key_example' # str | 

    try:
        # 关注用户
        api_response = api_instance.user_follow_user(user_id, app_key)
        print("The response of UserApi->user_follow_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_follow_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| 要关注的用户ID | 
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

# **user_follower_put**
> BooleanApiResponse user_follower_put(id, app_key, follower_put_model=follower_put_model)

更新粉丝

根据粉丝ID更新粉丝信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.follower_put_model import FollowerPutModel
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
    api_instance = ZSGF.Client.UserApi(api_client)
    id = 56 # int | 粉丝ID
    app_key = 'app_key_example' # str | 
    follower_put_model = ZSGF.Client.FollowerPutModel() # FollowerPutModel | 更新粉丝的请求参数 (optional)

    try:
        # 更新粉丝
        api_response = api_instance.user_follower_put(id, app_key, follower_put_model=follower_put_model)
        print("The response of UserApi->user_follower_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_follower_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 粉丝ID | 
 **app_key** | **str**|  | 
 **follower_put_model** | [**FollowerPutModel**](FollowerPutModel.md)| 更新粉丝的请求参数 | [optional] 

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

# **user_followers**
> UserFollowersResultApiResponse user_followers(app_key, tag=tag, status=status, target_user_id=target_user_id, skip=skip, take=take)

获取我的粉丝列表

根据条件获取我的粉丝列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_followers_result_api_response import UserFollowersResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str | 标签 (optional)
    status = 'status_example' # str | 状态 (optional)
    target_user_id = 0 # int | 指定用户的粉丝 (optional) (default to 0)
    skip = 0 # int | 跳过的记录数 (optional) (default to 0)
    take = 10 # int | 获取的记录数 (optional) (default to 10)

    try:
        # 获取我的粉丝列表
        api_response = api_instance.user_followers(app_key, tag=tag, status=status, target_user_id=target_user_id, skip=skip, take=take)
        print("The response of UserApi->user_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**| 标签 | [optional] 
 **status** | **str**| 状态 | [optional] 
 **target_user_id** | **int**| 指定用户的粉丝 | [optional] [default to 0]
 **skip** | **int**| 跳过的记录数 | [optional] [default to 0]
 **take** | **int**| 获取的记录数 | [optional] [default to 10]

### Return type

[**UserFollowersResultApiResponse**](UserFollowersResultApiResponse.md)

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

# **user_following**
> BooleanApiResponse user_following(app_key, tag=tag, status=status, target_user_id=target_user_id, skip=skip, take=take, check_user_id=check_user_id, only_ids=only_ids)

获取当前用户的关注列表，或者判断是否关注某个特定用户。

根据条件获取我的关注列表，或判断是否关注某个用户

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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str | 用于过滤关注列表的标签（可选）。 (optional)
    status = 'status_example' # str | 用于过滤关注列表的状态（可选）。 (optional)
    target_user_id = 0 # int | 指定用户的关注记录，如果不提供则默认为当前用户的关注。 (optional) (default to 0)
    skip = 0 # int | 跳过的记录数，用于分页（默认0）。 (optional) (default to 0)
    take = 10 # int | 获取的记录数，用于分页（默认10）。 (optional) (default to 10)
    check_user_id = 56 # int | 要判断是否关注的目标用户ID。如果提供此参数，方法将返回一个布尔值，表示当前用户是否关注该目标用户。 (optional)
    only_ids = False # bool | 是否只返回关注用户的ID集合，默认为false（即返回完整的关注用户信息）。 (optional) (default to False)

    try:
        # 获取当前用户的关注列表，或者判断是否关注某个特定用户。
        api_response = api_instance.user_following(app_key, tag=tag, status=status, target_user_id=target_user_id, skip=skip, take=take, check_user_id=check_user_id, only_ids=only_ids)
        print("The response of UserApi->user_following:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_following: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**| 用于过滤关注列表的标签（可选）。 | [optional] 
 **status** | **str**| 用于过滤关注列表的状态（可选）。 | [optional] 
 **target_user_id** | **int**| 指定用户的关注记录，如果不提供则默认为当前用户的关注。 | [optional] [default to 0]
 **skip** | **int**| 跳过的记录数，用于分页（默认0）。 | [optional] [default to 0]
 **take** | **int**| 获取的记录数，用于分页（默认10）。 | [optional] [default to 10]
 **check_user_id** | **int**| 要判断是否关注的目标用户ID。如果提供此参数，方法将返回一个布尔值，表示当前用户是否关注该目标用户。 | [optional] 
 **only_ids** | **bool**| 是否只返回关注用户的ID集合，默认为false（即返回完整的关注用户信息）。 | [optional] [default to False]

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

# **user_friends_near_by**
> UserFriendsNearByResultApiResponse user_friends_near_by(longitude, latitude, app_key, country=country, state=state, city=city, district=district, gender=gender, age_s=age_s, age_e=age_e, tag=tag, distance=distance, skip=skip, take=take)

获取附近的用户推荐列表

根据地理位置坐标和多种筛选条件，查询附近满足条件的用户列表，支持分页和按距离排序。
地理位置查询使用MySQL的ST_Distance_Sphere函数计算球面距离。
注意：longitude为经度(X轴)，latitude为纬度(Y轴)，参数顺序与常规坐标系一致

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_friends_near_by_result_api_response import UserFriendsNearByResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    longitude = 3.4 # float | 当前用户经度坐标(WGS84坐标系)
    latitude = 3.4 # float | 当前用户纬度坐标(WGS84坐标系)
    app_key = 'app_key_example' # str | 
    country = 'country_example' # str | 国家过滤条件（精确匹配） (optional)
    state = 'state_example' # str | 省份过滤条件（精确匹配） (optional)
    city = 'city_example' # str | 城市过滤条件（精确匹配） (optional)
    district = 'district_example' # str | 区县过滤条件（精确匹配） (optional)
    gender = 'gender_example' # str | 性别过滤条件（可选值示例：Male/Female/Other） (optional)
    age_s = 56 # int | 年龄起始范围（包含，0表示不限制） (optional)
    age_e = 56 # int | 年龄结束范围（包含，0表示不限制） (optional)
    tag = 'tag_example' # str | 兴趣标签过滤（支持模糊匹配，如：\"运动\"） (optional)
    distance = 0 # int | 搜索半径（单位：米，0表示不限制距离） (optional) (default to 0)
    skip = 0 # int | 跳过的记录数（分页起始位置，默认0） (optional) (default to 0)
    take = 10 # int | 获取的记录数（分页大小，默认10，最大100） (optional) (default to 10)

    try:
        # 获取附近的用户推荐列表
        api_response = api_instance.user_friends_near_by(longitude, latitude, app_key, country=country, state=state, city=city, district=district, gender=gender, age_s=age_s, age_e=age_e, tag=tag, distance=distance, skip=skip, take=take)
        print("The response of UserApi->user_friends_near_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_friends_near_by: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **float**| 当前用户经度坐标(WGS84坐标系) | 
 **latitude** | **float**| 当前用户纬度坐标(WGS84坐标系) | 
 **app_key** | **str**|  | 
 **country** | **str**| 国家过滤条件（精确匹配） | [optional] 
 **state** | **str**| 省份过滤条件（精确匹配） | [optional] 
 **city** | **str**| 城市过滤条件（精确匹配） | [optional] 
 **district** | **str**| 区县过滤条件（精确匹配） | [optional] 
 **gender** | **str**| 性别过滤条件（可选值示例：Male/Female/Other） | [optional] 
 **age_s** | **int**| 年龄起始范围（包含，0表示不限制） | [optional] 
 **age_e** | **int**| 年龄结束范围（包含，0表示不限制） | [optional] 
 **tag** | **str**| 兴趣标签过滤（支持模糊匹配，如：\&quot;运动\&quot;） | [optional] 
 **distance** | **int**| 搜索半径（单位：米，0表示不限制距离） | [optional] [default to 0]
 **skip** | **int**| 跳过的记录数（分页起始位置，默认0） | [optional] [default to 0]
 **take** | **int**| 获取的记录数（分页大小，默认10，最大100） | [optional] [default to 10]

### Return type

[**UserFriendsNearByResultApiResponse**](UserFriendsNearByResultApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 返回推荐用户列表数据 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_import**
> BooleanApiResponse user_import(app_key, check=check, file=file)

导入用户数据

导入用户数据

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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    check = True # bool | 是否进行检查 (optional)
    file = None # bytearray | 导入的文件 (optional)

    try:
        # 导入用户数据
        api_response = api_instance.user_import(app_key, check=check, file=file)
        print("The response of UserApi->user_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **check** | **bool**| 是否进行检查 | [optional] 
 **file** | **bytearray**| 导入的文件 | [optional] 

### Return type

[**BooleanApiResponse**](BooleanApiResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_location**
> GeoLocationModelApiResponse user_location(id, app_key)

获取位置详情

根据位置ID获取位置详情

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.geo_location_model_api_response import GeoLocationModelApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    id = 56 # int | 位置ID
    app_key = 'app_key_example' # str | 

    try:
        # 获取位置详情
        api_response = api_instance.user_location(id, app_key)
        print("The response of UserApi->user_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 位置ID | 
 **app_key** | **str**|  | 

### Return type

[**GeoLocationModelApiResponse**](GeoLocationModelApiResponse.md)

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

# **user_location_delete**
> BooleanApiResponse user_location_delete(id, app_key)

删除位置

根据位置ID删除位置信息

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
    api_instance = ZSGF.Client.UserApi(api_client)
    id = 56 # int | 位置ID
    app_key = 'app_key_example' # str | 

    try:
        # 删除位置
        api_response = api_instance.user_location_delete(id, app_key)
        print("The response of UserApi->user_location_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_location_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 位置ID | 
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

# **user_location_post**
> UserLocationPostResultApiResponse user_location_post(app_key, geo_location_model=geo_location_model)

添加位置

添加新的位置信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.geo_location_model import GeoLocationModel
from ZSGF.Client.models.user_location_post_result_api_response import UserLocationPostResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    geo_location_model = ZSGF.Client.GeoLocationModel() # GeoLocationModel | 位置信息 (optional)

    try:
        # 添加位置
        api_response = api_instance.user_location_post(app_key, geo_location_model=geo_location_model)
        print("The response of UserApi->user_location_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_location_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **geo_location_model** | [**GeoLocationModel**](GeoLocationModel.md)| 位置信息 | [optional] 

### Return type

[**UserLocationPostResultApiResponse**](UserLocationPostResultApiResponse.md)

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

# **user_location_put**
> BooleanApiResponse user_location_put(id, app_key, geo_location_model=geo_location_model)

更新位置

此方法用于更新指定位置ID的位置信息。如果位置不存在，则创建一个新的位置。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.geo_location_model import GeoLocationModel
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
    api_instance = ZSGF.Client.UserApi(api_client)
    id = 56 # int | 位置ID
    app_key = 'app_key_example' # str | 
    geo_location_model = ZSGF.Client.GeoLocationModel() # GeoLocationModel | 位置信息 (optional)

    try:
        # 更新位置
        api_response = api_instance.user_location_put(id, app_key, geo_location_model=geo_location_model)
        print("The response of UserApi->user_location_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_location_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 位置ID | 
 **app_key** | **str**|  | 
 **geo_location_model** | [**GeoLocationModel**](GeoLocationModel.md)| 位置信息 | [optional] 

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

# **user_locations**
> UserLocationsResultApiResponse user_locations(app_key, tag=tag, type=type, x=x, y=y, sphere=sphere, skip=skip, take=take)

获取位置列表

根据条件获取位置列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_locations_result_api_response import UserLocationsResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str | 标签 (optional)
    type = 'type_example' # str | 分类 (optional)
    x = 3.4 # float | 纬度 (optional)
    y = 3.4 # float | 经度 (optional)
    sphere = 56 # int | 附近距离，单位：米 (optional)
    skip = 56 # int | 跳过的记录数 (optional)
    take = 10 # int | 获取的记录数 (optional) (default to 10)

    try:
        # 获取位置列表
        api_response = api_instance.user_locations(app_key, tag=tag, type=type, x=x, y=y, sphere=sphere, skip=skip, take=take)
        print("The response of UserApi->user_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **tag** | **str**| 标签 | [optional] 
 **type** | **str**| 分类 | [optional] 
 **x** | **float**| 纬度 | [optional] 
 **y** | **float**| 经度 | [optional] 
 **sphere** | **int**| 附近距离，单位：米 | [optional] 
 **skip** | **int**| 跳过的记录数 | [optional] 
 **take** | **int**| 获取的记录数 | [optional] [default to 10]

### Return type

[**UserLocationsResultApiResponse**](UserLocationsResultApiResponse.md)

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

# **user_mutual_followers**
> UserMutualFollowersResultApiResponse user_mutual_followers(app_key, skip=skip, take=take)

有共同粉丝的用户推荐

推荐有共同粉丝的用户

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_mutual_followers_result_api_response import UserMutualFollowersResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    skip = 0 # int | 跳过的记录数 (optional) (default to 0)
    take = 10 # int | 获取的记录数 (optional) (default to 10)

    try:
        # 有共同粉丝的用户推荐
        api_response = api_instance.user_mutual_followers(app_key, skip=skip, take=take)
        print("The response of UserApi->user_mutual_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_mutual_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **skip** | **int**| 跳过的记录数 | [optional] [default to 0]
 **take** | **int**| 获取的记录数 | [optional] [default to 10]

### Return type

[**UserMutualFollowersResultApiResponse**](UserMutualFollowersResultApiResponse.md)

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

# **user_mutual_followings**
> UserMutualFollowingsResultApiResponse user_mutual_followings(app_key, skip=skip, take=take)

有共同关注的用户推荐

推荐有共同关注的用户

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_mutual_followings_result_api_response import UserMutualFollowingsResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    skip = 0 # int | 跳过的记录数 (optional) (default to 0)
    take = 10 # int | 获取的记录数 (optional) (default to 10)

    try:
        # 有共同关注的用户推荐
        api_response = api_instance.user_mutual_followings(app_key, skip=skip, take=take)
        print("The response of UserApi->user_mutual_followings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_mutual_followings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **skip** | **int**| 跳过的记录数 | [optional] [default to 0]
 **take** | **int**| 获取的记录数 | [optional] [default to 10]

### Return type

[**UserMutualFollowingsResultApiResponse**](UserMutualFollowingsResultApiResponse.md)

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

# **user_o_auth_account_bind**
> BooleanApiResponse user_o_auth_account_bind(app_key, o_auth_account_bind_request=o_auth_account_bind_request)

外部账号 绑定，如果已存在绑定则直接返回成功

绑定外部账号

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.o_auth_account_bind_request import OAuthAccountBindRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    o_auth_account_bind_request = ZSGF.Client.OAuthAccountBindRequest() # OAuthAccountBindRequest | 绑定请求参数 (optional)

    try:
        # 外部账号 绑定，如果已存在绑定则直接返回成功
        api_response = api_instance.user_o_auth_account_bind(app_key, o_auth_account_bind_request=o_auth_account_bind_request)
        print("The response of UserApi->user_o_auth_account_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_o_auth_account_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **o_auth_account_bind_request** | [**OAuthAccountBindRequest**](OAuthAccountBindRequest.md)| 绑定请求参数 | [optional] 

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

# **user_o_auth_account_sign_in**
> TokenModelApiResponse user_o_auth_account_sign_in(app_key, o_auth_account_sign_in_request=o_auth_account_sign_in_request)

外部账号 登录

使用外部账号进行登录

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.o_auth_account_sign_in_request import OAuthAccountSignInRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    o_auth_account_sign_in_request = ZSGF.Client.OAuthAccountSignInRequest() # OAuthAccountSignInRequest | 登录请求参数 (optional)

    try:
        # 外部账号 登录
        api_response = api_instance.user_o_auth_account_sign_in(app_key, o_auth_account_sign_in_request=o_auth_account_sign_in_request)
        print("The response of UserApi->user_o_auth_account_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_o_auth_account_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **o_auth_account_sign_in_request** | [**OAuthAccountSignInRequest**](OAuthAccountSignInRequest.md)| 登录请求参数 | [optional] 

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

# **user_o_auth_accounts**
> UserLoginsListApiResponse user_o_auth_accounts(app_key)

外部账号 绑定列表

获取外部账号绑定列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_logins_list_api_response import UserLoginsListApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 外部账号 绑定列表
        api_response = api_instance.user_o_auth_accounts(app_key)
        print("The response of UserApi->user_o_auth_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_o_auth_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 

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
> BooleanApiResponse user_o_auth_accounts_put_bind(id, app_key, o_auth_account_put_bind_request=o_auth_account_put_bind_request)

外部账号 更新绑定

更新外部账号绑定信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.o_auth_account_put_bind_request import OAuthAccountPutBindRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    id = 56 # int | 绑定ID
    app_key = 'app_key_example' # str | 
    o_auth_account_put_bind_request = ZSGF.Client.OAuthAccountPutBindRequest() # OAuthAccountPutBindRequest | 更新请求参数 (optional)

    try:
        # 外部账号 更新绑定
        api_response = api_instance.user_o_auth_accounts_put_bind(id, app_key, o_auth_account_put_bind_request=o_auth_account_put_bind_request)
        print("The response of UserApi->user_o_auth_accounts_put_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_o_auth_accounts_put_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 绑定ID | 
 **app_key** | **str**|  | 
 **o_auth_account_put_bind_request** | [**OAuthAccountPutBindRequest**](OAuthAccountPutBindRequest.md)| 更新请求参数 | [optional] 

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
> BooleanApiResponse user_o_auth_accounts_un_bind(id, app_key)

外部账号 删除绑定

删除外部账号绑定

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
    api_instance = ZSGF.Client.UserApi(api_client)
    id = 56 # int | 绑定ID
    app_key = 'app_key_example' # str | 

    try:
        # 外部账号 删除绑定
        api_response = api_instance.user_o_auth_accounts_un_bind(id, app_key)
        print("The response of UserApi->user_o_auth_accounts_un_bind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_o_auth_accounts_un_bind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 绑定ID | 
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

# **user_profile_by_id**
> GetUserProfileResultApiResponse user_profile_by_id(user_id, app_key)

获取指定用户资料

用于他人主页展示

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.get_user_profile_result_api_response import GetUserProfileResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    user_id = 56 # int | 用户ID
    app_key = 'app_key_example' # str | 

    try:
        # 获取指定用户资料
        api_response = api_instance.user_profile_by_id(user_id, app_key)
        print("The response of UserApi->user_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_profile_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| 用户ID | 
 **app_key** | **str**|  | 

### Return type

[**GetUserProfileResultApiResponse**](GetUserProfileResultApiResponse.md)

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

# **user_put**
> BooleanApiResponse user_put(id, app_key, user=user)

更新用户信息

根据用户ID更新用户信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.user import User
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
    api_instance = ZSGF.Client.UserApi(api_client)
    id = 56 # int | 用户ID
    app_key = 'app_key_example' # str | 
    user = ZSGF.Client.User() # User | 用户信息 (optional)

    try:
        # 更新用户信息
        api_response = api_instance.user_put(id, app_key, user=user)
        print("The response of UserApi->user_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 用户ID | 
 **app_key** | **str**|  | 
 **user** | [**User**](User.md)| 用户信息 | [optional] 

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

# **user_qr_code_pre_sign_in**
> Int64ApiResponse user_qr_code_pre_sign_in(app_key, qr_code_pre_sign_in_request=qr_code_pre_sign_in_request)

微信小程序 - 预登陆

使用微信小程序二维码进行预登陆

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.int64_api_response import Int64ApiResponse
from ZSGF.Client.models.qr_code_pre_sign_in_request import QRCodePreSignInRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_pre_sign_in_request = ZSGF.Client.QRCodePreSignInRequest() # QRCodePreSignInRequest | 预登陆请求参数 (optional)

    try:
        # 微信小程序 - 预登陆
        api_response = api_instance.user_qr_code_pre_sign_in(app_key, qr_code_pre_sign_in_request=qr_code_pre_sign_in_request)
        print("The response of UserApi->user_qr_code_pre_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_qr_code_pre_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_pre_sign_in_request** | [**QRCodePreSignInRequest**](QRCodePreSignInRequest.md)| 预登陆请求参数 | [optional] 

### Return type

[**Int64ApiResponse**](Int64ApiResponse.md)

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

# **user_qr_code_scan**
> UserQRCodeScanResultApiResponse user_qr_code_scan(app_key, qr_code_scan_request=qr_code_scan_request)

微信小程序 - 扫码

使用微信小程序二维码进行扫码

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.qr_code_scan_request import QRCodeScanRequest
from ZSGF.Client.models.user_qr_code_scan_result_api_response import UserQRCodeScanResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_scan_request = ZSGF.Client.QRCodeScanRequest() # QRCodeScanRequest | 扫码请求参数 (optional)

    try:
        # 微信小程序 - 扫码
        api_response = api_instance.user_qr_code_scan(app_key, qr_code_scan_request=qr_code_scan_request)
        print("The response of UserApi->user_qr_code_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_qr_code_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_scan_request** | [**QRCodeScanRequest**](QRCodeScanRequest.md)| 扫码请求参数 | [optional] 

### Return type

[**UserQRCodeScanResultApiResponse**](UserQRCodeScanResultApiResponse.md)

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

# **user_qr_code_sign_in**
> TokenModelApiResponse user_qr_code_sign_in(app_key, qr_code_sign_in_request=qr_code_sign_in_request)

微信小程序 - 网页登录

使用微信小程序二维码进行网页登录

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.qr_code_sign_in_request import QRCodeSignInRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_sign_in_request = ZSGF.Client.QRCodeSignInRequest() # QRCodeSignInRequest | 登录请求参数 (optional)

    try:
        # 微信小程序 - 网页登录
        api_response = api_instance.user_qr_code_sign_in(app_key, qr_code_sign_in_request=qr_code_sign_in_request)
        print("The response of UserApi->user_qr_code_sign_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_qr_code_sign_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_sign_in_request** | [**QRCodeSignInRequest**](QRCodeSignInRequest.md)| 登录请求参数 | [optional] 

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

# **user_qr_code_sign_up**
> TokenModelApiResponse user_qr_code_sign_up(app_key, qr_code_sign_up_request=qr_code_sign_up_request)

微信小程序 - 注册

使用微信小程序二维码进行注册

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.qr_code_sign_up_request import QRCodeSignUpRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_sign_up_request = ZSGF.Client.QRCodeSignUpRequest() # QRCodeSignUpRequest | 注册请求参数 (optional)

    try:
        # 微信小程序 - 注册
        api_response = api_instance.user_qr_code_sign_up(app_key, qr_code_sign_up_request=qr_code_sign_up_request)
        print("The response of UserApi->user_qr_code_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_qr_code_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_sign_up_request** | [**QRCodeSignUpRequest**](QRCodeSignUpRequest.md)| 注册请求参数 | [optional] 

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

账号密码 登录

使用账号密码进行登录

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.sign_in_request import SignInRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    sign_in_request = ZSGF.Client.SignInRequest() # SignInRequest | 登录请求参数 (optional)

    try:
        # 账号密码 登录
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

账号密码 注册

使用账号密码进行注册

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.sign_up_request import SignUpRequest
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    sign_up_request = ZSGF.Client.SignUpRequest() # SignUpRequest | 注册请求参数 (optional)

    try:
        # 账号密码 注册
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

双因素验证

获取双因素验证的设置信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.setup_code_api_response import SetupCodeApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 双因素验证
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

# **user_unfollow_user**
> BooleanApiResponse user_unfollow_user(user_id, app_key)

取消关注

取消关注指定用户

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
    api_instance = ZSGF.Client.UserApi(api_client)
    user_id = 56 # int | 要取消关注的用户ID
    app_key = 'app_key_example' # str | 

    try:
        # 取消关注
        api_response = api_instance.user_unfollow_user(user_id, app_key)
        print("The response of UserApi->user_unfollow_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_unfollow_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| 要取消关注的用户ID | 
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

# **users**
> UserListResultApiResponse users(app_key, user_name=user_name, email=email, phone=phone, platform=platform, union_id=union_id, role=role, skip=skip, take=take)

获取用户列表

根据条件获取用户列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_list_result_api_response import UserListResultApiResponse
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
    api_instance = ZSGF.Client.UserApi(api_client)
    app_key = 'app_key_example' # str | 
    user_name = 'user_name_example' # str | 用户名 (optional)
    email = 'email_example' # str | 邮箱 (optional)
    phone = 'phone_example' # str | 电话 (optional)
    platform = 'platform_example' # str | 平台 (optional)
    union_id = 'union_id_example' # str | 联合ID (optional)
    role = 'role_example' # str | 角色 (optional)
    skip = 56 # int | 跳过的记录数 (optional)
    take = 56 # int | 获取的记录数 (optional)

    try:
        # 获取用户列表
        api_response = api_instance.users(app_key, user_name=user_name, email=email, phone=phone, platform=platform, union_id=union_id, role=role, skip=skip, take=take)
        print("The response of UserApi->users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **user_name** | **str**| 用户名 | [optional] 
 **email** | **str**| 邮箱 | [optional] 
 **phone** | **str**| 电话 | [optional] 
 **platform** | **str**| 平台 | [optional] 
 **union_id** | **str**| 联合ID | [optional] 
 **role** | **str**| 角色 | [optional] 
 **skip** | **int**| 跳过的记录数 | [optional] 
 **take** | **int**| 获取的记录数 | [optional] 

### Return type

[**UserListResultApiResponse**](UserListResultApiResponse.md)

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

