# ZSGF.Client.SystemFileApi

All URIs are relative to *https://api.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_file_create_folder**](SystemFileApi.md#system_file_create_folder) | **POST** /SystemFile/CreateFolder | 创建文件夹
[**system_file_delete**](SystemFileApi.md#system_file_delete) | **DELETE** /SystemFile | 删除文件
[**system_file_rename**](SystemFileApi.md#system_file_rename) | **POST** /SystemFile/Rename | 重命名文件
[**system_file_upload**](SystemFileApi.md#system_file_upload) | **POST** /SystemFile | 上传文件
[**system_files**](SystemFileApi.md#system_files) | **GET** /SystemFile | 获取文件列表


# **system_file_create_folder**
> BooleanApiResponse system_file_create_folder(path=path)

创建文件夹

根据指定路径创建文件夹

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
    api_instance = ZSGF.Client.SystemFileApi(api_client)
    path = 'path_example' # str | 文件夹路径 (optional)

    try:
        # 创建文件夹
        api_response = api_instance.system_file_create_folder(path=path)
        print("The response of SystemFileApi->system_file_create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFileApi->system_file_create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| 文件夹路径 | [optional] 

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

# **system_file_delete**
> BooleanApiResponse system_file_delete(path=path)

删除文件

根据指定路径删除文件

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
    api_instance = ZSGF.Client.SystemFileApi(api_client)
    path = 'path_example' # str | 文件路径 (optional)

    try:
        # 删除文件
        api_response = api_instance.system_file_delete(path=path)
        print("The response of SystemFileApi->system_file_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFileApi->system_file_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| 文件路径 | [optional] 

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

# **system_file_rename**
> BooleanApiResponse system_file_rename(source_name=source_name, dest_name=dest_name)

重命名文件

根据指定的源文件名和目标文件名重命名文件

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
    api_instance = ZSGF.Client.SystemFileApi(api_client)
    source_name = 'source_name_example' # str | 源文件名 (optional)
    dest_name = 'dest_name_example' # str | 目标文件名 (optional)

    try:
        # 重命名文件
        api_response = api_instance.system_file_rename(source_name=source_name, dest_name=dest_name)
        print("The response of SystemFileApi->system_file_rename:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFileApi->system_file_rename: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_name** | **str**| 源文件名 | [optional] 
 **dest_name** | **str**| 目标文件名 | [optional] 

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

# **system_file_upload**
> StringApiResponse system_file_upload(path=path, file=file)

上传文件

根据指定路径上传文件

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
    api_instance = ZSGF.Client.SystemFileApi(api_client)
    path = 'path_example' # str | 上传的路径 (optional)
    file = None # bytearray | 上传的文件 (optional)

    try:
        # 上传文件
        api_response = api_instance.system_file_upload(path=path, file=file)
        print("The response of SystemFileApi->system_file_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFileApi->system_file_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| 上传的路径 | [optional] 
 **file** | **bytearray**| 上传的文件 | [optional] 

### Return type

[**StringApiResponse**](StringApiResponse.md)

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

# **system_files**
> SystemFileListResultApiResponse system_files(path=path)

获取文件列表

根据指定路径获取文件列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.system_file_list_result_api_response import SystemFileListResultApiResponse
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
    api_instance = ZSGF.Client.SystemFileApi(api_client)
    path = 'path_example' # str | 文件路径 (optional)

    try:
        # 获取文件列表
        api_response = api_instance.system_files(path=path)
        print("The response of SystemFileApi->system_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFileApi->system_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| 文件路径 | [optional] 

### Return type

[**SystemFileListResultApiResponse**](SystemFileListResultApiResponse.md)

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

