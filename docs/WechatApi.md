# ZSGF.Client.WechatApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_qr_code_login**](WechatApi.md#confirm_qr_code_login) | **POST** /Wechat/{appKey}/QR-Auth/Confirm-Login | 确认二维码登录请求
[**confirm_qr_code_registration**](WechatApi.md#confirm_qr_code_registration) | **POST** /Wechat/{appKey}/QR-Auth/Confirm-Register | 确认二维码注册请求
[**initiate_qr_auth_session**](WechatApi.md#initiate_qr_auth_session) | **POST** /Wechat/{appKey}/QR-Auth/Initiate | 初始化二维码认证会话
[**scan_qr_code_for_auth**](WechatApi.md#scan_qr_code_for_auth) | **POST** /Wechat/{appKey}/QR-Auth/Scan | 验证二维码扫描结果
[**wechat_decrypt**](WechatApi.md#wechat_decrypt) | **GET** /Wechat/{appKey}/Decrypt | 解密小程序用户数据
[**wechat_generate_scheme**](WechatApi.md#wechat_generate_scheme) | **POST** /Wechat/{appKey}/GenerateScheme | 生成小程序Scheme码
[**wechat_js_code2_session**](WechatApi.md#wechat_js_code2_session) | **GET** /Wechat/{appKey}/JSCode2Session | 校验小程序登录状态
[**wechat_js_config**](WechatApi.md#wechat_js_config) | **GET** /Wechat/{appKey}/JSConfig | 配置公众号JS SDK
[**wechat_msg_sec_check**](WechatApi.md#wechat_msg_sec_check) | **POST** /Wechat/{appKey}/MsgSecCheck | 小程序内容安全检测
[**wechat_subscribe_msg**](WechatApi.md#wechat_subscribe_msg) | **POST** /Wechat/{appKey}/SubscribeMSG | 发送公众号一次性订阅消息
[**wechat_subscribe_send**](WechatApi.md#wechat_subscribe_send) | **POST** /Wechat/{appKey}/SubscribeSend | 发送小程序订阅消息
[**wechat_url_link_generate**](WechatApi.md#wechat_url_link_generate) | **POST** /Wechat/{appKey}/UrlLinkGenerate | 生成小程序URL跳转链接
[**wechat_user_info**](WechatApi.md#wechat_user_info) | **GET** /Wechat/{appKey}/UserInfo | 获取公众号H5 UnionID
[**wechat_wxa_code_get**](WechatApi.md#wechat_wxa_code_get) | **POST** /Wechat/{appKey}/WXACodeGet | 获取小程序码（普通）
[**wechat_wxa_code_get_unlimited**](WechatApi.md#wechat_wxa_code_get_unlimited) | **POST** /Wechat/{appKey}/WXACodeGetUnlimited | 获取小程序码（无限制）


# **confirm_qr_code_login**
> TokenModelApiResponse confirm_qr_code_login(app_key, qr_code_sign_in_request=qr_code_sign_in_request)

确认二维码登录请求

微信小程序用户确认二维码登录并获取访问令牌

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.qr_code_sign_in_request import QRCodeSignInRequest
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_sign_in_request = ZSGF.Client.QRCodeSignInRequest() # QRCodeSignInRequest | 登录确认请求参数 (optional)

    try:
        # 确认二维码登录请求
        api_response = api_instance.confirm_qr_code_login(app_key, qr_code_sign_in_request=qr_code_sign_in_request)
        print("The response of WechatApi->confirm_qr_code_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->confirm_qr_code_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_sign_in_request** | [**QRCodeSignInRequest**](QRCodeSignInRequest.md)| 登录确认请求参数 | [optional] 

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

# **confirm_qr_code_registration**
> TokenModelApiResponse confirm_qr_code_registration(app_key, qr_code_sign_up_request=qr_code_sign_up_request)

确认二维码注册请求

微信小程序用户通过二维码完成注册并获取访问令牌

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.qr_code_sign_up_request import QRCodeSignUpRequest
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_sign_up_request = ZSGF.Client.QRCodeSignUpRequest() # QRCodeSignUpRequest | 注册确认请求参数 (optional)

    try:
        # 确认二维码注册请求
        api_response = api_instance.confirm_qr_code_registration(app_key, qr_code_sign_up_request=qr_code_sign_up_request)
        print("The response of WechatApi->confirm_qr_code_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->confirm_qr_code_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_sign_up_request** | [**QRCodeSignUpRequest**](QRCodeSignUpRequest.md)| 注册确认请求参数 | [optional] 

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

# **initiate_qr_auth_session**
> Int64ApiResponse initiate_qr_auth_session(app_key, qr_code_pre_sign_in_request=qr_code_pre_sign_in_request)

初始化二维码认证会话

创建用于微信小程序扫码登录/注册的认证会话

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.int64_api_response import Int64ApiResponse
from ZSGF.Client.models.qr_code_pre_sign_in_request import QRCodePreSignInRequest
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_pre_sign_in_request = ZSGF.Client.QRCodePreSignInRequest() # QRCodePreSignInRequest | 认证会话初始化请求参数 (optional)

    try:
        # 初始化二维码认证会话
        api_response = api_instance.initiate_qr_auth_session(app_key, qr_code_pre_sign_in_request=qr_code_pre_sign_in_request)
        print("The response of WechatApi->initiate_qr_auth_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->initiate_qr_auth_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_pre_sign_in_request** | [**QRCodePreSignInRequest**](QRCodePreSignInRequest.md)| 认证会话初始化请求参数 | [optional] 

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

# **scan_qr_code_for_auth**
> UserQRCodeScanResultApiResponse scan_qr_code_for_auth(app_key, qr_code_scan_request=qr_code_scan_request)

验证二维码扫描结果

微信小程序扫描二维码并获取应用授权信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.qr_code_scan_request import QRCodeScanRequest
from ZSGF.Client.models.user_qr_code_scan_result_api_response import UserQRCodeScanResultApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    qr_code_scan_request = ZSGF.Client.QRCodeScanRequest() # QRCodeScanRequest | 二维码扫描请求参数 (optional)

    try:
        # 验证二维码扫描结果
        api_response = api_instance.scan_qr_code_for_auth(app_key, qr_code_scan_request=qr_code_scan_request)
        print("The response of WechatApi->scan_qr_code_for_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->scan_qr_code_for_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **qr_code_scan_request** | [**QRCodeScanRequest**](QRCodeScanRequest.md)| 二维码扫描请求参数 | [optional] 

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

# **wechat_decrypt**
> StringApiResponse wechat_decrypt(app_key, encrypted_data=encrypted_data, iv=iv, session_key=session_key)

解密小程序用户数据

解密小程序加密数据

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    encrypted_data = 'encrypted_data_example' # str | 加密的数据 (optional)
    iv = 'iv_example' # str | 加密算法的初始向量 (optional)
    session_key = 'session_key_example' # str | 会话密钥 (optional)

    try:
        # 解密小程序用户数据
        api_response = api_instance.wechat_decrypt(app_key, encrypted_data=encrypted_data, iv=iv, session_key=session_key)
        print("The response of WechatApi->wechat_decrypt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_decrypt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **encrypted_data** | **str**| 加密的数据 | [optional] 
 **iv** | **str**| 加密算法的初始向量 | [optional] 
 **session_key** | **str**| 会话密钥 | [optional] 

### Return type

[**StringApiResponse**](StringApiResponse.md)

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

# **wechat_generate_scheme**
> StringApiResponse wechat_generate_scheme(app_key, request_body=request_body)

生成小程序Scheme码

生成小程序的scheme码

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    request_body = None # List[object] | scheme码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/qrcode-link/url-scheme/generateScheme.html (optional)

    try:
        # 生成小程序Scheme码
        api_response = api_instance.wechat_generate_scheme(app_key, request_body=request_body)
        print("The response of WechatApi->wechat_generate_scheme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_generate_scheme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **request_body** | [**List[object]**](object.md)| scheme码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/qrcode-link/url-scheme/generateScheme.html | [optional] 

### Return type

[**StringApiResponse**](StringApiResponse.md)

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

# **wechat_js_code2_session**
> StringApiResponse wechat_js_code2_session(app_key, js_code=js_code)

校验小程序登录状态

校验小程序登录凭证

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    js_code = 'js_code_example' # str | 登录凭证，开发参考：https://dwz.cn/icNajFh7 (optional)

    try:
        # 校验小程序登录状态
        api_response = api_instance.wechat_js_code2_session(app_key, js_code=js_code)
        print("The response of WechatApi->wechat_js_code2_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_js_code2_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **js_code** | **str**| 登录凭证，开发参考：https://dwz.cn/icNajFh7 | [optional] 

### Return type

[**StringApiResponse**](StringApiResponse.md)

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

# **wechat_js_config**
> WechatJSConfigResultApiResponse wechat_js_config(app_key, url=url)

配置公众号JS SDK

获取公众号H5的JS SDK配置

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.wechat_js_config_result_api_response import WechatJSConfigResultApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    url = 'url_example' # str | 当前网页的URL (optional)

    try:
        # 配置公众号JS SDK
        api_response = api_instance.wechat_js_config(app_key, url=url)
        print("The response of WechatApi->wechat_js_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_js_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **url** | **str**| 当前网页的URL | [optional] 

### Return type

[**WechatJSConfigResultApiResponse**](WechatJSConfigResultApiResponse.md)

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

# **wechat_msg_sec_check**
> object wechat_msg_sec_check(app_key, request_body=request_body)

小程序内容安全检测

检测消息内容是否含有违法违规信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    request_body = None # List[object] | 消息内容数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/sec-center/sec-check/msgSecCheck.html (optional)

    try:
        # 小程序内容安全检测
        api_response = api_instance.wechat_msg_sec_check(app_key, request_body=request_body)
        print("The response of WechatApi->wechat_msg_sec_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_msg_sec_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **request_body** | [**List[object]**](object.md)| 消息内容数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/sec-center/sec-check/msgSecCheck.html | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wechat_subscribe_msg**
> StringApiResponse wechat_subscribe_msg(app_key, request_body=request_body)

发送公众号一次性订阅消息

发送公众号H5一次性订阅消息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    request_body = None # List[object] | 订阅消息数据，开发参考：https://dwz.cn/IXptek5n (optional)

    try:
        # 发送公众号一次性订阅消息
        api_response = api_instance.wechat_subscribe_msg(app_key, request_body=request_body)
        print("The response of WechatApi->wechat_subscribe_msg:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_subscribe_msg: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **request_body** | [**List[object]**](object.md)| 订阅消息数据，开发参考：https://dwz.cn/IXptek5n | [optional] 

### Return type

[**StringApiResponse**](StringApiResponse.md)

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

# **wechat_subscribe_send**
> StringApiResponse wechat_subscribe_send(app_key, request_body=request_body)

发送小程序订阅消息

发送小程序订阅消息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    request_body = None # List[object] | 订阅消息数据，开发参考：https://dwz.cn/bohXaCnp (optional)

    try:
        # 发送小程序订阅消息
        api_response = api_instance.wechat_subscribe_send(app_key, request_body=request_body)
        print("The response of WechatApi->wechat_subscribe_send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_subscribe_send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **request_body** | [**List[object]**](object.md)| 订阅消息数据，开发参考：https://dwz.cn/bohXaCnp | [optional] 

### Return type

[**StringApiResponse**](StringApiResponse.md)

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

# **wechat_url_link_generate**
> StringApiResponse wechat_url_link_generate(app_key, request_body=request_body)

生成小程序URL跳转链接

生成小程序的网页跳转地址

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    request_body = None # List[object] | 跳转地址数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/url-link/urllink.generate.html (optional)

    try:
        # 生成小程序URL跳转链接
        api_response = api_instance.wechat_url_link_generate(app_key, request_body=request_body)
        print("The response of WechatApi->wechat_url_link_generate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_url_link_generate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **request_body** | [**List[object]**](object.md)| 跳转地址数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/url-link/urllink.generate.html | [optional] 

### Return type

[**StringApiResponse**](StringApiResponse.md)

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

# **wechat_user_info**
> StringApiResponse wechat_user_info(app_key, openid=openid)

获取公众号H5 UnionID

获取公众号H5用户的UnionID

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    openid = 'openid_example' # str | 用户的OpenID (optional)

    try:
        # 获取公众号H5 UnionID
        api_response = api_instance.wechat_user_info(app_key, openid=openid)
        print("The response of WechatApi->wechat_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_user_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **openid** | **str**| 用户的OpenID | [optional] 

### Return type

[**StringApiResponse**](StringApiResponse.md)

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

# **wechat_wxa_code_get**
> bytearray wechat_wxa_code_get(app_key, request_body=request_body)

获取小程序码（普通）

获取小程序码

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    request_body = None # List[object] | 小程序码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/qr-code/wxacode.get.html (optional)

    try:
        # 获取小程序码（普通）
        api_response = api_instance.wechat_wxa_code_get(app_key, request_body=request_body)
        print("The response of WechatApi->wechat_wxa_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_wxa_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **request_body** | [**List[object]**](object.md)| 小程序码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/qr-code/wxacode.get.html | [optional] 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: image/jpeg

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wechat_wxa_code_get_unlimited**
> bytearray wechat_wxa_code_get_unlimited(app_key, request_body=request_body)

获取小程序码（无限制）

获取无限制的小程序码

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    request_body = None # List[object] | 小程序码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/qr-code/wxacode.getUnlimited.html (optional)

    try:
        # 获取小程序码（无限制）
        api_response = api_instance.wechat_wxa_code_get_unlimited(app_key, request_body=request_body)
        print("The response of WechatApi->wechat_wxa_code_get_unlimited:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_wxa_code_get_unlimited: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **request_body** | [**List[object]**](object.md)| 小程序码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/qr-code/wxacode.getUnlimited.html | [optional] 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: image/jpeg

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

