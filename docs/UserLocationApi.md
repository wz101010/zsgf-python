# ZSGF.Client.UserLocationApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_location**](UserLocationApi.md#user_location) | **GET** /UserLocation/{appKey}/{id} | 获取位置详情
[**user_location_delete**](UserLocationApi.md#user_location_delete) | **DELETE** /UserLocation/{appKey}/{id} | 删除位置
[**user_location_post**](UserLocationApi.md#user_location_post) | **POST** /UserLocation/{appKey} | 添加位置
[**user_location_put**](UserLocationApi.md#user_location_put) | **PUT** /UserLocation/{appKey}/{id} | 更新位置
[**user_locations**](UserLocationApi.md#user_locations) | **GET** /UserLocation/{appKey} | 获取位置列表


# **user_location**
> GeoLocationModelApiResponse user_location(id, app_key, user_id=user_id)

获取位置详情

根据位置ID获取位置详情

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.geo_location_model_api_response import GeoLocationModelApiResponse
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
    api_instance = ZSGF.Client.UserLocationApi(api_client)
    id = 56 # int | 位置ID
    app_key = 'app_key_example' # str | 
    user_id = '' # str |  (optional) (default to '')

    try:
        # 获取位置详情
        api_response = api_instance.user_location(id, app_key, user_id=user_id)
        print("The response of UserLocationApi->user_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLocationApi->user_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 位置ID | 
 **app_key** | **str**|  | 
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]

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
> BooleanApiResponse user_location_delete(id, app_key, user_id=user_id)

删除位置

根据位置ID删除位置信息

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
    api_instance = ZSGF.Client.UserLocationApi(api_client)
    id = 56 # int | 位置ID
    app_key = 'app_key_example' # str | 
    user_id = '' # str |  (optional) (default to '')

    try:
        # 删除位置
        api_response = api_instance.user_location_delete(id, app_key, user_id=user_id)
        print("The response of UserLocationApi->user_location_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLocationApi->user_location_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 位置ID | 
 **app_key** | **str**|  | 
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]

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
> UserLocationPostResultApiResponse user_location_post(app_key, user_id=user_id, geo_location_model=geo_location_model)

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
    api_instance = ZSGF.Client.UserLocationApi(api_client)
    app_key = 'app_key_example' # str | 
    user_id = '' # str |  (optional) (default to '')
    geo_location_model = ZSGF.Client.GeoLocationModel() # GeoLocationModel | 位置信息 (optional)

    try:
        # 添加位置
        api_response = api_instance.user_location_post(app_key, user_id=user_id, geo_location_model=geo_location_model)
        print("The response of UserLocationApi->user_location_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLocationApi->user_location_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]
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
> BooleanApiResponse user_location_put(id, app_key, user_id=user_id, geo_location_model=geo_location_model)

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
    api_instance = ZSGF.Client.UserLocationApi(api_client)
    id = 56 # int | 位置ID
    app_key = 'app_key_example' # str | 
    user_id = '' # str |  (optional) (default to '')
    geo_location_model = ZSGF.Client.GeoLocationModel() # GeoLocationModel | 位置信息 (optional)

    try:
        # 更新位置
        api_response = api_instance.user_location_put(id, app_key, user_id=user_id, geo_location_model=geo_location_model)
        print("The response of UserLocationApi->user_location_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLocationApi->user_location_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 位置ID | 
 **app_key** | **str**|  | 
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]
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
> UserLocationsResultApiResponse user_locations(app_key, tag=tag, type=type, x=x, y=y, sphere=sphere, skip=skip, take=take, user_id=user_id)

获取位置列表

根据条件获取位置列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.user_locations_result_api_response import UserLocationsResultApiResponse
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
    api_instance = ZSGF.Client.UserLocationApi(api_client)
    app_key = 'app_key_example' # str | 
    tag = 'tag_example' # str | 标签 (optional)
    type = 'type_example' # str | 分类 (optional)
    x = 3.4 # float | 纬度 (optional)
    y = 3.4 # float | 经度 (optional)
    sphere = 56 # int | 附近距离，单位：米 (optional)
    skip = 56 # int | 跳过的记录数 (optional)
    take = 10 # int | 获取的记录数 (optional) (default to 10)
    user_id = '' # str |  (optional) (default to '')

    try:
        # 获取位置列表
        api_response = api_instance.user_locations(app_key, tag=tag, type=type, x=x, y=y, sphere=sphere, skip=skip, take=take, user_id=user_id)
        print("The response of UserLocationApi->user_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLocationApi->user_locations: %s\n" % e)
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
 **user_id** | **str**|  | [optional] [default to &#39;&#39;]

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

