# ZSGF.Client.WechatApi

All URIs are relative to *https://api.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wechat_decrypt**](WechatApi.md#wechat_decrypt) | **GET** /Wechat/{appKey}/Decrypt | 小程序-解密数据
[**wechat_generate_scheme**](WechatApi.md#wechat_generate_scheme) | **POST** /Wechat/{appKey}/GenerateScheme | 小程序-生成scheme码(该接口用于获取小程序 scheme 码，适用于短信、邮件、外部网页、微信内等拉起小程序的业务场景)
[**wechat_js_code2_session**](WechatApi.md#wechat_js_code2_session) | **GET** /Wechat/{appKey}/JSCode2Session | 小程序-登录凭证校验
[**wechat_js_config**](WechatApi.md#wechat_js_config) | **GET** /Wechat/{appKey}/JSConfig | 公众号H5-JS SDK Config
[**wechat_subscribe_msg**](WechatApi.md#wechat_subscribe_msg) | **POST** /Wechat/{appKey}/SubscribeMSG | 公众号H5-发送一次性订阅消息
[**wechat_subscribe_send**](WechatApi.md#wechat_subscribe_send) | **POST** /Wechat/{appKey}/SubscribeSend | 小程序-发送订阅消息
[**wechat_url_link_generate**](WechatApi.md#wechat_url_link_generate) | **POST** /Wechat/{appKey}/UrlLinkGenerate | 小程序-生成网页跳转地址(获取小程序 URL Link，适用于短信、邮件、网页、微信内等拉起小程序的业务场景)
[**wechat_user_info**](WechatApi.md#wechat_user_info) | **GET** /Wechat/{appKey}/UserInfo | 公众号H5-获取用户UnionID
[**wechat_wxa_code_get**](WechatApi.md#wechat_wxa_code_get) | **POST** /Wechat/{appKey}/WXACodeGet | 小程序-获取小程序码
[**wechat_wxa_code_get_unlimited**](WechatApi.md#wechat_wxa_code_get_unlimited) | **POST** /Wechat/{appKey}/WXACodeGetUnlimited | 小程序-获取小程序码(无限制)


# **wechat_decrypt**
> StringApiResponse wechat_decrypt(app_key, encrypted_data=encrypted_data, iv=iv, session_key=session_key)

小程序-解密数据

解密小程序加密数据

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    encrypted_data = 'encrypted_data_example' # str | 加密的数据 (optional)
    iv = 'iv_example' # str | 加密算法的初始向量 (optional)
    session_key = 'session_key_example' # str | 会话密钥 (optional)

    try:
        # 小程序-解密数据
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
> StringApiResponse wechat_generate_scheme(app_key, body=body)

小程序-生成scheme码(该接口用于获取小程序 scheme 码，适用于短信、邮件、外部网页、微信内等拉起小程序的业务场景)

生成小程序的scheme码

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    body = None # object | scheme码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/qrcode-link/url-scheme/generateScheme.html (optional)

    try:
        # 小程序-生成scheme码(该接口用于获取小程序 scheme 码，适用于短信、邮件、外部网页、微信内等拉起小程序的业务场景)
        api_response = api_instance.wechat_generate_scheme(app_key, body=body)
        print("The response of WechatApi->wechat_generate_scheme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_generate_scheme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **body** | **object**| scheme码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/qrcode-link/url-scheme/generateScheme.html | [optional] 

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

小程序-登录凭证校验

校验小程序登录凭证

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    js_code = 'js_code_example' # str | 登录凭证，开发参考：https://dwz.cn/icNajFh7 (optional)

    try:
        # 小程序-登录凭证校验
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

公众号H5-JS SDK Config

获取公众号H5的JS SDK配置

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.wechat_js_config_result_api_response import WechatJSConfigResultApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    url = 'url_example' # str | 当前网页的URL (optional)

    try:
        # 公众号H5-JS SDK Config
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

# **wechat_subscribe_msg**
> StringApiResponse wechat_subscribe_msg(app_key, body=body)

公众号H5-发送一次性订阅消息

发送公众号H5一次性订阅消息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    body = None # object | 订阅消息数据，开发参考：https://dwz.cn/IXptek5n (optional)

    try:
        # 公众号H5-发送一次性订阅消息
        api_response = api_instance.wechat_subscribe_msg(app_key, body=body)
        print("The response of WechatApi->wechat_subscribe_msg:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_subscribe_msg: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **body** | **object**| 订阅消息数据，开发参考：https://dwz.cn/IXptek5n | [optional] 

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
> StringApiResponse wechat_subscribe_send(app_key, body=body)

小程序-发送订阅消息

发送小程序订阅消息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    body = None # object | 订阅消息数据，开发参考：https://dwz.cn/bohXaCnp (optional)

    try:
        # 小程序-发送订阅消息
        api_response = api_instance.wechat_subscribe_send(app_key, body=body)
        print("The response of WechatApi->wechat_subscribe_send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_subscribe_send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **body** | **object**| 订阅消息数据，开发参考：https://dwz.cn/bohXaCnp | [optional] 

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
> StringApiResponse wechat_url_link_generate(app_key, body=body)

小程序-生成网页跳转地址(获取小程序 URL Link，适用于短信、邮件、网页、微信内等拉起小程序的业务场景)

生成小程序的网页跳转地址

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    body = None # object | 跳转地址数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/url-link/urllink.generate.html (optional)

    try:
        # 小程序-生成网页跳转地址(获取小程序 URL Link，适用于短信、邮件、网页、微信内等拉起小程序的业务场景)
        api_response = api_instance.wechat_url_link_generate(app_key, body=body)
        print("The response of WechatApi->wechat_url_link_generate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_url_link_generate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **body** | **object**| 跳转地址数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/url-link/urllink.generate.html | [optional] 

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

公众号H5-获取用户UnionID

获取公众号H5用户的UnionID

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.string_api_response import StringApiResponse
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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    openid = 'openid_example' # str | 用户的OpenID (optional)

    try:
        # 公众号H5-获取用户UnionID
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
> bytearray wechat_wxa_code_get(app_key, body=body)

小程序-获取小程序码

获取小程序码

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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    body = None # object | 小程序码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/qr-code/wxacode.get.html (optional)

    try:
        # 小程序-获取小程序码
        api_response = api_instance.wechat_wxa_code_get(app_key, body=body)
        print("The response of WechatApi->wechat_wxa_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_wxa_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **body** | **object**| 小程序码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/qr-code/wxacode.get.html | [optional] 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: image/jpeg, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wechat_wxa_code_get_unlimited**
> bytearray wechat_wxa_code_get_unlimited(app_key, body=body)

小程序-获取小程序码(无限制)

获取无限制的小程序码

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
    api_instance = ZSGF.Client.WechatApi(api_client)
    app_key = 'app_key_example' # str | 
    body = None # object | 小程序码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/qr-code/wxacode.getUnlimited.html (optional)

    try:
        # 小程序-获取小程序码(无限制)
        api_response = api_instance.wechat_wxa_code_get_unlimited(app_key, body=body)
        print("The response of WechatApi->wechat_wxa_code_get_unlimited:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WechatApi->wechat_wxa_code_get_unlimited: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **body** | **object**| 小程序码数据，开发参考：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/qr-code/wxacode.getUnlimited.html | [optional] 

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: image/jpeg, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

