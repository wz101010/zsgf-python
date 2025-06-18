# ZSGF.Client.AlipayApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alipay_create_order**](AlipayApi.md#alipay_create_order) | **POST** /Alipay/{appKey}/CreateOrder | 创建当面付订单
[**alipay_create_order_page_pay**](AlipayApi.md#alipay_create_order_page_pay) | **POST** /Alipay/{appKey}/CreateOrderPagePay | 创建PC支付订单
[**alipay_create_order_wap_pay**](AlipayApi.md#alipay_create_order_wap_pay) | **POST** /Alipay/{appKey}/CreateOrderWapPay | 创建WAP支付订单
[**alipay_order_detail**](AlipayApi.md#alipay_order_detail) | **GET** /Alipay/{appKey}/OrderDetail | 获取订单详情
[**alipay_order_refund**](AlipayApi.md#alipay_order_refund) | **POST** /Alipay/{appKey}/OrderRefund | 发起订单退款
[**alipay_return_page_notify**](AlipayApi.md#alipay_return_page_notify) | **POST** /Alipay/{appKey}/ReturnPageNotify | 支付成功回调通知


# **alipay_create_order**
> StringApiResponse alipay_create_order(app_key, alipay_create_order_request=alipay_create_order_request)

创建当面付订单

创建一个当面付订单，并返回支付二维码。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.alipay_create_order_request import AlipayCreateOrderRequest
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
    api_instance = ZSGF.Client.AlipayApi(api_client)
    app_key = 'app_key_example' # str | 
    alipay_create_order_request = ZSGF.Client.AlipayCreateOrderRequest() # AlipayCreateOrderRequest |  (optional)

    try:
        # 创建当面付订单
        api_response = api_instance.alipay_create_order(app_key, alipay_create_order_request=alipay_create_order_request)
        print("The response of AlipayApi->alipay_create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlipayApi->alipay_create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **alipay_create_order_request** | [**AlipayCreateOrderRequest**](AlipayCreateOrderRequest.md)|  | [optional] 

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

# **alipay_create_order_page_pay**
> StringApiResponse alipay_create_order_page_pay(app_key, alipay_create_order_page_pay_request=alipay_create_order_page_pay_request)

创建PC支付订单

创建一个PC支付订单，并返回支付页面。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.alipay_create_order_page_pay_request import AlipayCreateOrderPagePayRequest
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
    api_instance = ZSGF.Client.AlipayApi(api_client)
    app_key = 'app_key_example' # str | 
    alipay_create_order_page_pay_request = ZSGF.Client.AlipayCreateOrderPagePayRequest() # AlipayCreateOrderPagePayRequest |  (optional)

    try:
        # 创建PC支付订单
        api_response = api_instance.alipay_create_order_page_pay(app_key, alipay_create_order_page_pay_request=alipay_create_order_page_pay_request)
        print("The response of AlipayApi->alipay_create_order_page_pay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlipayApi->alipay_create_order_page_pay: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **alipay_create_order_page_pay_request** | [**AlipayCreateOrderPagePayRequest**](AlipayCreateOrderPagePayRequest.md)|  | [optional] 

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

# **alipay_create_order_wap_pay**
> StringApiResponse alipay_create_order_wap_pay(app_key, alipay_create_order_wap_pay_request=alipay_create_order_wap_pay_request)

创建WAP支付订单

创建一个WAP支付订单，并返回支付页面。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.alipay_create_order_wap_pay_request import AlipayCreateOrderWapPayRequest
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
    api_instance = ZSGF.Client.AlipayApi(api_client)
    app_key = 'app_key_example' # str | 
    alipay_create_order_wap_pay_request = ZSGF.Client.AlipayCreateOrderWapPayRequest() # AlipayCreateOrderWapPayRequest |  (optional)

    try:
        # 创建WAP支付订单
        api_response = api_instance.alipay_create_order_wap_pay(app_key, alipay_create_order_wap_pay_request=alipay_create_order_wap_pay_request)
        print("The response of AlipayApi->alipay_create_order_wap_pay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlipayApi->alipay_create_order_wap_pay: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **alipay_create_order_wap_pay_request** | [**AlipayCreateOrderWapPayRequest**](AlipayCreateOrderWapPayRequest.md)|  | [optional] 

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

# **alipay_order_detail**
> AlipayTradeQueryResponseApiResponse alipay_order_detail(app_key, order_no=order_no)

获取订单详情

查询订单详情，包括订单状态和支付信息。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.alipay_trade_query_response_api_response import AlipayTradeQueryResponseApiResponse
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
    api_instance = ZSGF.Client.AlipayApi(api_client)
    app_key = 'app_key_example' # str | 
    order_no = 'order_no_example' # str | 订单号 (optional)

    try:
        # 获取订单详情
        api_response = api_instance.alipay_order_detail(app_key, order_no=order_no)
        print("The response of AlipayApi->alipay_order_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlipayApi->alipay_order_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **order_no** | **str**| 订单号 | [optional] 

### Return type

[**AlipayTradeQueryResponseApiResponse**](AlipayTradeQueryResponseApiResponse.md)

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

# **alipay_order_refund**
> AlipayTradeRefundResponseApiResponse alipay_order_refund(app_key, amount=amount, order_no=order_no)

发起订单退款

对指定订单进行退款操作。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.alipay_trade_refund_response_api_response import AlipayTradeRefundResponseApiResponse
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
    api_instance = ZSGF.Client.AlipayApi(api_client)
    app_key = 'app_key_example' # str | 
    amount = 'amount_example' # str | 退款金额 (optional)
    order_no = 'order_no_example' # str | 订单号 (optional)

    try:
        # 发起订单退款
        api_response = api_instance.alipay_order_refund(app_key, amount=amount, order_no=order_no)
        print("The response of AlipayApi->alipay_order_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlipayApi->alipay_order_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **amount** | **str**| 退款金额 | [optional] 
 **order_no** | **str**| 订单号 | [optional] 

### Return type

[**AlipayTradeRefundResponseApiResponse**](AlipayTradeRefundResponseApiResponse.md)

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

# **alipay_return_page_notify**
> BooleanApiResponse alipay_return_page_notify(app_key, return_page_notify_request=return_page_notify_request)

支付成功回调通知

处理支付宝支付成功的同步通知。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.return_page_notify_request import ReturnPageNotifyRequest
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
    api_instance = ZSGF.Client.AlipayApi(api_client)
    app_key = 'app_key_example' # str | 
    return_page_notify_request = ZSGF.Client.ReturnPageNotifyRequest() # ReturnPageNotifyRequest |  (optional)

    try:
        # 支付成功回调通知
        api_response = api_instance.alipay_return_page_notify(app_key, return_page_notify_request=return_page_notify_request)
        print("The response of AlipayApi->alipay_return_page_notify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlipayApi->alipay_return_page_notify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **return_page_notify_request** | [**ReturnPageNotifyRequest**](ReturnPageNotifyRequest.md)|  | [optional] 

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

