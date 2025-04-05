# ZSGF.Client.CurrencyApi

All URIs are relative to *https://api.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currencies**](CurrencyApi.md#currencies) | **GET** /Currency/{appKey} | 获取货币列表
[**currency**](CurrencyApi.md#currency) | **GET** /Currency/{appKey}/{id} | 获取货币详情
[**currency_delete**](CurrencyApi.md#currency_delete) | **DELETE** /Currency/{appKey}/{id} | 删除货币
[**currency_exchange_rate_delete**](CurrencyApi.md#currency_exchange_rate_delete) | **DELETE** /Currency/{appKey}/ExchangeRates/{id} | 删除汇率
[**currency_exchange_rate_put**](CurrencyApi.md#currency_exchange_rate_put) | **PUT** /Currency/{appKey}/ExchangeRates/{code} | 更新汇率
[**currency_exchange_rates**](CurrencyApi.md#currency_exchange_rates) | **GET** /Currency/{appKey}/ExchangeRates/{code} | 获取汇率列表
[**currency_post**](CurrencyApi.md#currency_post) | **POST** /Currency/{appKey} | 创建新货币
[**currency_put**](CurrencyApi.md#currency_put) | **PUT** /Currency/{appKey}/{id} | 更新货币信息
[**currency_transactions**](CurrencyApi.md#currency_transactions) | **GET** /Currency/{appKey}/Transactions | 获取货币交易记录


# **currencies**
> CurrencyListApiResponse currencies(app_key)

获取货币列表

获取所有货币的列表，按ID降序排列。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.currency_list_api_response import CurrencyListApiResponse
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
    api_instance = ZSGF.Client.CurrencyApi(api_client)
    app_key = 'app_key_example' # str | 

    try:
        # 获取货币列表
        api_response = api_instance.currencies(app_key)
        print("The response of CurrencyApi->currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 

### Return type

[**CurrencyListApiResponse**](CurrencyListApiResponse.md)

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

# **currency**
> CurrencyApiResponse currency(id, app_key)

获取货币详情

根据货币ID获取货币的详细信息。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.currency_api_response import CurrencyApiResponse
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
    api_instance = ZSGF.Client.CurrencyApi(api_client)
    id = 56 # int | 货币ID
    app_key = 'app_key_example' # str | 

    try:
        # 获取货币详情
        api_response = api_instance.currency(id, app_key)
        print("The response of CurrencyApi->currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 货币ID | 
 **app_key** | **str**|  | 

### Return type

[**CurrencyApiResponse**](CurrencyApiResponse.md)

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

# **currency_delete**
> BooleanApiResponse currency_delete(id, app_key)

删除货币

根据货币ID删除货币。

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
    api_instance = ZSGF.Client.CurrencyApi(api_client)
    id = 56 # int | 货币ID
    app_key = 'app_key_example' # str | 

    try:
        # 删除货币
        api_response = api_instance.currency_delete(id, app_key)
        print("The response of CurrencyApi->currency_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 货币ID | 
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

# **currency_exchange_rate_delete**
> BooleanApiResponse currency_exchange_rate_delete(id, app_key)

删除汇率

根据汇率ID删除汇率。

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
    api_instance = ZSGF.Client.CurrencyApi(api_client)
    id = 56 # int | 汇率ID
    app_key = 'app_key_example' # str | 

    try:
        # 删除汇率
        api_response = api_instance.currency_exchange_rate_delete(id, app_key)
        print("The response of CurrencyApi->currency_exchange_rate_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_exchange_rate_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 汇率ID | 
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

# **currency_exchange_rate_put**
> Int64ApiResponse currency_exchange_rate_put(code, app_key, exchange_rate_put_request=exchange_rate_put_request)

更新汇率

根据货币代码更新汇率信息。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.exchange_rate_put_request import ExchangeRatePutRequest
from ZSGF.Client.models.int64_api_response import Int64ApiResponse
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
    api_instance = ZSGF.Client.CurrencyApi(api_client)
    code = 'code_example' # str | 货币代码
    app_key = 'app_key_example' # str | 
    exchange_rate_put_request = ZSGF.Client.ExchangeRatePutRequest() # ExchangeRatePutRequest | 汇率信息 (optional)

    try:
        # 更新汇率
        api_response = api_instance.currency_exchange_rate_put(code, app_key, exchange_rate_put_request=exchange_rate_put_request)
        print("The response of CurrencyApi->currency_exchange_rate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_exchange_rate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| 货币代码 | 
 **app_key** | **str**|  | 
 **exchange_rate_put_request** | [**ExchangeRatePutRequest**](ExchangeRatePutRequest.md)| 汇率信息 | [optional] 

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

# **currency_exchange_rates**
> CurrencyExchangeRateApiResponse currency_exchange_rates(code, app_key)

获取汇率列表

根据货币代码获取该货币的汇率列表。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.currency_exchange_rate_api_response import CurrencyExchangeRateApiResponse
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
    api_instance = ZSGF.Client.CurrencyApi(api_client)
    code = 'code_example' # str | 货币代码
    app_key = 'app_key_example' # str | 

    try:
        # 获取汇率列表
        api_response = api_instance.currency_exchange_rates(code, app_key)
        print("The response of CurrencyApi->currency_exchange_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_exchange_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| 货币代码 | 
 **app_key** | **str**|  | 

### Return type

[**CurrencyExchangeRateApiResponse**](CurrencyExchangeRateApiResponse.md)

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

# **currency_post**
> Int64ApiResponse currency_post(app_key, currency=currency)

创建新货币

创建一个新的货币并返回其ID。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.currency import Currency
from ZSGF.Client.models.int64_api_response import Int64ApiResponse
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
    api_instance = ZSGF.Client.CurrencyApi(api_client)
    app_key = 'app_key_example' # str | 
    currency = ZSGF.Client.Currency() # Currency | 货币信息 (optional)

    try:
        # 创建新货币
        api_response = api_instance.currency_post(app_key, currency=currency)
        print("The response of CurrencyApi->currency_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **currency** | [**Currency**](Currency.md)| 货币信息 | [optional] 

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

# **currency_put**
> BooleanApiResponse currency_put(id, app_key, currency=currency)

更新货币信息

根据货币ID更新货币的详细信息。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.currency import Currency
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
    api_instance = ZSGF.Client.CurrencyApi(api_client)
    id = 56 # int | 货币ID
    app_key = 'app_key_example' # str | 
    currency = ZSGF.Client.Currency() # Currency | 货币信息 (optional)

    try:
        # 更新货币信息
        api_response = api_instance.currency_put(id, app_key, currency=currency)
        print("The response of CurrencyApi->currency_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 货币ID | 
 **app_key** | **str**|  | 
 **currency** | [**Currency**](Currency.md)| 货币信息 | [optional] 

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

# **currency_transactions**
> CurrencyTransactionListApiResponse currency_transactions(app_key, user_id=user_id, trans_type=trans_type, cur_code=cur_code, start_time=start_time, end_time=end_time, skip=skip, take=take)

获取货币交易记录

根据用户ID、交易类型、货币代码、时间范围等条件获取货币交易记录。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.currency_transaction_list_api_response import CurrencyTransactionListApiResponse
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
    api_instance = ZSGF.Client.CurrencyApi(api_client)
    app_key = 'app_key_example' # str | 
    user_id = 56 # int | 用户ID (optional)
    trans_type = 'trans_type_example' # str | 交易类型 (optional)
    cur_code = 'cur_code_example' # str | 货币代码 (optional)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | 开始时间 (optional)
    end_time = '2013-10-20T19:20:30+01:00' # datetime | 结束时间 (optional)
    skip = 56 # int | 跳过的条数 (optional)
    take = 56 # int | 拉取的条数 (optional)

    try:
        # 获取货币交易记录
        api_response = api_instance.currency_transactions(app_key, user_id=user_id, trans_type=trans_type, cur_code=cur_code, start_time=start_time, end_time=end_time, skip=skip, take=take)
        print("The response of CurrencyApi->currency_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **user_id** | **int**| 用户ID | [optional] 
 **trans_type** | **str**| 交易类型 | [optional] 
 **cur_code** | **str**| 货币代码 | [optional] 
 **start_time** | **datetime**| 开始时间 | [optional] 
 **end_time** | **datetime**| 结束时间 | [optional] 
 **skip** | **int**| 跳过的条数 | [optional] 
 **take** | **int**| 拉取的条数 | [optional] 

### Return type

[**CurrencyTransactionListApiResponse**](CurrencyTransactionListApiResponse.md)

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

