# ZSGF.Client.OrderApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order**](OrderApi.md#order) | **GET** /Order/{appKey}/{id} | 获取订单详情
[**order_create**](OrderApi.md#order_create) | **POST** /Order/{appKey}/Create | 创建订单
[**orders**](OrderApi.md#orders) | **GET** /Order/{appKey} | 获取订单列表


# **order**
> OrderApiResponse order(id, app_key)

获取订单详情

根据订单ID获取订单详情

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.order_api_response import OrderApiResponse
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
    api_instance = ZSGF.Client.OrderApi(api_client)
    id = 56 # int | 订单ID
    app_key = 'app_key_example' # str | 

    try:
        # 获取订单详情
        api_response = api_instance.order(id, app_key)
        print("The response of OrderApi->order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 订单ID | 
 **app_key** | **str**|  | 

### Return type

[**OrderApiResponse**](OrderApiResponse.md)

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

# **order_create**
> CreateOrderResultApiResponse order_create(app_key, create_order_request=create_order_request)

创建订单

根据请求参数创建订单

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.create_order_request import CreateOrderRequest
from ZSGF.Client.models.create_order_result_api_response import CreateOrderResultApiResponse
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
    api_instance = ZSGF.Client.OrderApi(api_client)
    app_key = 'app_key_example' # str | 
    create_order_request = ZSGF.Client.CreateOrderRequest() # CreateOrderRequest | 订单创建请求 (optional)

    try:
        # 创建订单
        api_response = api_instance.order_create(app_key, create_order_request=create_order_request)
        print("The response of OrderApi->order_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **create_order_request** | [**CreateOrderRequest**](CreateOrderRequest.md)| 订单创建请求 | [optional] 

### Return type

[**CreateOrderResultApiResponse**](CreateOrderResultApiResponse.md)

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

# **orders**
> OrderListResultApiResponse orders(app_key, status=status, order_no=order_no, trade_no=trade_no, user_id=user_id, pct_type=pct_type, pct_id=pct_id, pct_name=pct_name, skip=skip, take=take)

获取订单列表

根据查询条件获取订单列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.order_list_result_api_response import OrderListResultApiResponse
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
    api_instance = ZSGF.Client.OrderApi(api_client)
    app_key = 'app_key_example' # str | 
    status = 'status_example' # str | 订单状态 (optional)
    order_no = 'order_no_example' # str | 系统订单号 (optional)
    trade_no = 'trade_no_example' # str | 支付平台单号 (optional)
    user_id = 56 # int | 用户ID (optional)
    pct_type = 'pct_type_example' # str | 商品类型 (optional)
    pct_id = 'pct_id_example' # str | 商品ID (optional)
    pct_name = 'pct_name_example' # str | 商品名称 (optional)
    skip = 56 # int | 跳过的条数 (optional)
    take = 56 # int | 拉取的条数 (optional)

    try:
        # 获取订单列表
        api_response = api_instance.orders(app_key, status=status, order_no=order_no, trade_no=trade_no, user_id=user_id, pct_type=pct_type, pct_id=pct_id, pct_name=pct_name, skip=skip, take=take)
        print("The response of OrderApi->orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **status** | **str**| 订单状态 | [optional] 
 **order_no** | **str**| 系统订单号 | [optional] 
 **trade_no** | **str**| 支付平台单号 | [optional] 
 **user_id** | **int**| 用户ID | [optional] 
 **pct_type** | **str**| 商品类型 | [optional] 
 **pct_id** | **str**| 商品ID | [optional] 
 **pct_name** | **str**| 商品名称 | [optional] 
 **skip** | **int**| 跳过的条数 | [optional] 
 **take** | **int**| 拉取的条数 | [optional] 

### Return type

[**OrderListResultApiResponse**](OrderListResultApiResponse.md)

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

