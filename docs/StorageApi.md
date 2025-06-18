# ZSGF.Client.StorageApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_aggregate**](StorageApi.md#storage_aggregate) | **GET** /Storage/{appKey}/{table}/Aggregate | 聚合查询
[**storage_delete**](StorageApi.md#storage_delete) | **DELETE** /Storage/{appKey}/{table}/{id} | 删除数据
[**storage_detail**](StorageApi.md#storage_detail) | **GET** /Storage/{appKey}/{table}/{id} | 数据详情
[**storage_list**](StorageApi.md#storage_list) | **GET** /Storage/{appKey}/{table} | 查询数据
[**storage_post**](StorageApi.md#storage_post) | **POST** /Storage/{appKey}/{table} | 添加数据
[**storage_put**](StorageApi.md#storage_put) | **PUT** /Storage/{appKey}/{table}/{id} | 更新数据


# **storage_aggregate**
> ObjectListApiResponse storage_aggregate(table, app_key, pipeline=pipeline)

聚合查询

根据聚合管道查询指定表中的数据

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.object_list_api_response import ObjectListApiResponse
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
    api_instance = ZSGF.Client.StorageApi(api_client)
    table = 'table_example' # str | 表名称
    app_key = 'app_key_example' # str | 
    pipeline = 'pipeline_example' # str | 构建聚合查询 (optional)

    try:
        # 聚合查询
        api_response = api_instance.storage_aggregate(table, app_key, pipeline=pipeline)
        print("The response of StorageApi->storage_aggregate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_aggregate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| 表名称 | 
 **app_key** | **str**|  | 
 **pipeline** | **str**| 构建聚合查询 | [optional] 

### Return type

[**ObjectListApiResponse**](ObjectListApiResponse.md)

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

# **storage_delete**
> BooleanApiResponse storage_delete(table, id, app_key)

删除数据

删除指定表中指定ID的数据

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
    api_instance = ZSGF.Client.StorageApi(api_client)
    table = 'table_example' # str | 表名称
    id = 'id_example' # str | 数据ID
    app_key = 'app_key_example' # str | 

    try:
        # 删除数据
        api_response = api_instance.storage_delete(table, id, app_key)
        print("The response of StorageApi->storage_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| 表名称 | 
 **id** | **str**| 数据ID | 
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

# **storage_detail**
> ObjectApiResponse storage_detail(table, id, app_key, project=project)

数据详情

获取指定表中指定ID的数据详情

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.object_api_response import ObjectApiResponse
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
    api_instance = ZSGF.Client.StorageApi(api_client)
    table = 'table_example' # str | 表名称
    id = 'id_example' # str | 数据ID
    app_key = 'app_key_example' # str | 
    project = 'project_example' # str | json格式 (optional)

    try:
        # 数据详情
        api_response = api_instance.storage_detail(table, id, app_key, project=project)
        print("The response of StorageApi->storage_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| 表名称 | 
 **id** | **str**| 数据ID | 
 **app_key** | **str**|  | 
 **project** | **str**| json格式 | [optional] 

### Return type

[**ObjectApiResponse**](ObjectApiResponse.md)

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

# **storage_list**
> StorageListResultApiResponse storage_list(table, app_key, filter=filter, project=project, sort=sort, start_time=start_time, end_time=end_time, explain=explain, take=take, skip=skip)

查询数据

根据条件查询指定表中的数据

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.storage_list_result_api_response import StorageListResultApiResponse
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
    api_instance = ZSGF.Client.StorageApi(api_client)
    table = 'table_example' # str | 表名称
    app_key = 'app_key_example' # str | 
    filter = 'filter_example' # str | 过滤，json格式 (optional)
    project = 'project_example' # str | 字段映射，json格式 (optional)
    sort = 'sort_example' # str | 排序，json格式 (optional)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | 开始时间 (optional)
    end_time = '2013-10-20T19:20:30+01:00' # datetime | 结束时间 (optional)
    explain = False # bool | 查看执行计划 (optional) (default to False)
    take = 10 # int | 默认为10 (optional) (default to 10)
    skip = 0 # int | 默认为0 (optional) (default to 0)

    try:
        # 查询数据
        api_response = api_instance.storage_list(table, app_key, filter=filter, project=project, sort=sort, start_time=start_time, end_time=end_time, explain=explain, take=take, skip=skip)
        print("The response of StorageApi->storage_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| 表名称 | 
 **app_key** | **str**|  | 
 **filter** | **str**| 过滤，json格式 | [optional] 
 **project** | **str**| 字段映射，json格式 | [optional] 
 **sort** | **str**| 排序，json格式 | [optional] 
 **start_time** | **datetime**| 开始时间 | [optional] 
 **end_time** | **datetime**| 结束时间 | [optional] 
 **explain** | **bool**| 查看执行计划 | [optional] [default to False]
 **take** | **int**| 默认为10 | [optional] [default to 10]
 **skip** | **int**| 默认为0 | [optional] [default to 0]

### Return type

[**StorageListResultApiResponse**](StorageListResultApiResponse.md)

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

# **storage_post**
> StringApiResponse storage_post(table, app_key, request_body)

添加数据

向指定表中添加数据，可以是单个json对象或json数组

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
    api_instance = ZSGF.Client.StorageApi(api_client)
    table = 'table_example' # str | 表名称（小写字母加数字,1-50位）
    app_key = 'app_key_example' # str | 
    request_body = None # List[object] | json对象 / json数组

    try:
        # 添加数据
        api_response = api_instance.storage_post(table, app_key, request_body)
        print("The response of StorageApi->storage_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| 表名称（小写字母加数字,1-50位） | 
 **app_key** | **str**|  | 
 **request_body** | [**List[object]**](object.md)| json对象 / json数组 | 

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

# **storage_put**
> BooleanApiResponse storage_put(table, id, app_key, request_body, replace=replace)

更新数据

更新指定表中指定ID的数据，可以选择全量更新或部分更新

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
    api_instance = ZSGF.Client.StorageApi(api_client)
    table = 'table_example' # str | 表名称
    id = 'id_example' # str | 数据ID
    app_key = 'app_key_example' # str | 
    request_body = None # List[object] | json格式
    replace = False # bool | 是否为全量更新，默认为false (optional) (default to False)

    try:
        # 更新数据
        api_response = api_instance.storage_put(table, id, app_key, request_body, replace=replace)
        print("The response of StorageApi->storage_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| 表名称 | 
 **id** | **str**| 数据ID | 
 **app_key** | **str**|  | 
 **request_body** | [**List[object]**](object.md)| json格式 | 
 **replace** | **bool**| 是否为全量更新，默认为false | [optional] [default to False]

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

