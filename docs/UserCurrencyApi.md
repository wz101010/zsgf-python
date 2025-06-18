# ZSGF.Client.UserCurrencyApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_currencies**](UserCurrencyApi.md#user_currencies) | **GET** /UserCurrency/{appKey}/{id} | 获取用户资产
[**user_currency_consume**](UserCurrencyApi.md#user_currency_consume) | **POST** /UserCurrency/{appKey}/CurrencyConsume | 消费虚拟币
[**user_currency_exchange**](UserCurrencyApi.md#user_currency_exchange) | **POST** /UserCurrency/{appKey}/CurrencyExchange | 兑换虚拟币
[**user_currency_recharge**](UserCurrencyApi.md#user_currency_recharge) | **POST** /UserCurrency/{appKey}/CurrencyRecharge | 充值虚拟币
[**user_currency_transactions**](UserCurrencyApi.md#user_currency_transactions) | **GET** /UserCurrency/{appKey}/CurrencyTransactions | 虚拟币交易记录


# **user_currencies**
> UserCurrencyListApiResponse user_currencies(id, app_key)

获取用户资产

根据用户ID获取用户的资产列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_currency_list_api_response import UserCurrencyListApiResponse
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
    api_instance = ZSGF.Client.UserCurrencyApi(api_client)
    id = 56 # int | 用户ID
    app_key = 'app_key_example' # str | 

    try:
        # 获取用户资产
        api_response = api_instance.user_currencies(id, app_key)
        print("The response of UserCurrencyApi->user_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCurrencyApi->user_currencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 用户ID | 
 **app_key** | **str**|  | 

### Return type

[**UserCurrencyListApiResponse**](UserCurrencyListApiResponse.md)

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

# **user_currency_consume**
> BooleanApiResponse user_currency_consume(nonce, timestamp, signature, app_key, currency_consume_request=currency_consume_request)

消费虚拟币

根据提供的参数进行虚拟币消费

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.currency_consume_request import CurrencyConsumeRequest
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
    api_instance = ZSGF.Client.UserCurrencyApi(api_client)
    nonce = 'nonce_example' # str | 随机数
    timestamp = 56 # int | 时间戳（允许与服务器时间误差在1分钟内）
    signature = 'signature_example' # str | 签名
    app_key = 'app_key_example' # str | 
    currency_consume_request = ZSGF.Client.CurrencyConsumeRequest() # CurrencyConsumeRequest | 消费请求参数 (optional)

    try:
        # 消费虚拟币
        api_response = api_instance.user_currency_consume(nonce, timestamp, signature, app_key, currency_consume_request=currency_consume_request)
        print("The response of UserCurrencyApi->user_currency_consume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCurrencyApi->user_currency_consume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nonce** | **str**| 随机数 | 
 **timestamp** | **int**| 时间戳（允许与服务器时间误差在1分钟内） | 
 **signature** | **str**| 签名 | 
 **app_key** | **str**|  | 
 **currency_consume_request** | [**CurrencyConsumeRequest**](CurrencyConsumeRequest.md)| 消费请求参数 | [optional] 

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

# **user_currency_exchange**
> BooleanApiResponse user_currency_exchange(nonce, timestamp, signature, app_key, exchange_currency_request=exchange_currency_request)

兑换虚拟币

根据提供的参数进行虚拟币兑换

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.exchange_currency_request import ExchangeCurrencyRequest
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
    api_instance = ZSGF.Client.UserCurrencyApi(api_client)
    nonce = 'nonce_example' # str | 随机数
    timestamp = 56 # int | 时间戳（允许与服务器时间误差在1分钟内）
    signature = 'signature_example' # str | 签名
    app_key = 'app_key_example' # str | 
    exchange_currency_request = ZSGF.Client.ExchangeCurrencyRequest() # ExchangeCurrencyRequest | 兑换请求参数 (optional)

    try:
        # 兑换虚拟币
        api_response = api_instance.user_currency_exchange(nonce, timestamp, signature, app_key, exchange_currency_request=exchange_currency_request)
        print("The response of UserCurrencyApi->user_currency_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCurrencyApi->user_currency_exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nonce** | **str**| 随机数 | 
 **timestamp** | **int**| 时间戳（允许与服务器时间误差在1分钟内） | 
 **signature** | **str**| 签名 | 
 **app_key** | **str**|  | 
 **exchange_currency_request** | [**ExchangeCurrencyRequest**](ExchangeCurrencyRequest.md)| 兑换请求参数 | [optional] 

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

# **user_currency_recharge**
> BooleanApiResponse user_currency_recharge(nonce, timestamp, signature, app_key, recharge_point_request=recharge_point_request)

充值虚拟币

根据提供的参数进行虚拟币充值

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.recharge_point_request import RechargePointRequest
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
    api_instance = ZSGF.Client.UserCurrencyApi(api_client)
    nonce = 'nonce_example' # str | 随机数
    timestamp = 56 # int | 时间戳（允许与服务器时间误差在1分钟内）
    signature = 'signature_example' # str | 签名
    app_key = 'app_key_example' # str | 
    recharge_point_request = ZSGF.Client.RechargePointRequest() # RechargePointRequest | 充值请求参数 (optional)

    try:
        # 充值虚拟币
        api_response = api_instance.user_currency_recharge(nonce, timestamp, signature, app_key, recharge_point_request=recharge_point_request)
        print("The response of UserCurrencyApi->user_currency_recharge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCurrencyApi->user_currency_recharge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nonce** | **str**| 随机数 | 
 **timestamp** | **int**| 时间戳（允许与服务器时间误差在1分钟内） | 
 **signature** | **str**| 签名 | 
 **app_key** | **str**|  | 
 **recharge_point_request** | [**RechargePointRequest**](RechargePointRequest.md)| 充值请求参数 | [optional] 

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

# **user_currency_transactions**
> UserCurrencyCurrencyTransResultApiResponse user_currency_transactions(app_key, trans_type=trans_type, cur_code=cur_code, start_time=start_time, end_time=end_time, skip=skip, take=take)

虚拟币交易记录

根据提供的参数获取虚拟币交易记录

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_currency_currency_trans_result_api_response import UserCurrencyCurrencyTransResultApiResponse
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
    api_instance = ZSGF.Client.UserCurrencyApi(api_client)
    app_key = 'app_key_example' # str | 
    trans_type = 'trans_type_example' # str | 交易类型 (optional)
    cur_code = 'cur_code_example' # str | 货币代码 (optional)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | 开始时间 (optional)
    end_time = '2013-10-20T19:20:30+01:00' # datetime | 结束时间 (optional)
    skip = 56 # int | 跳过的条数 (optional)
    take = 56 # int | 拉取的条数 (optional)

    try:
        # 虚拟币交易记录
        api_response = api_instance.user_currency_transactions(app_key, trans_type=trans_type, cur_code=cur_code, start_time=start_time, end_time=end_time, skip=skip, take=take)
        print("The response of UserCurrencyApi->user_currency_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCurrencyApi->user_currency_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **trans_type** | **str**| 交易类型 | [optional] 
 **cur_code** | **str**| 货币代码 | [optional] 
 **start_time** | **datetime**| 开始时间 | [optional] 
 **end_time** | **datetime**| 结束时间 | [optional] 
 **skip** | **int**| 跳过的条数 | [optional] 
 **take** | **int**| 拉取的条数 | [optional] 

### Return type

[**UserCurrencyCurrencyTransResultApiResponse**](UserCurrencyCurrencyTransResultApiResponse.md)

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

