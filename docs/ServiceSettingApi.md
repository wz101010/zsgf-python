# ZSGF.Client.ServiceSettingApi

All URIs are relative to *https://api.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_setting**](ServiceSettingApi.md#service_setting) | **GET** /ServiceSetting/{id} | 获取配置详情
[**service_setting_delete**](ServiceSettingApi.md#service_setting_delete) | **DELETE** /ServiceSetting/{id} | 删除配置
[**service_setting_group**](ServiceSettingApi.md#service_setting_group) | **GET** /ServiceSetting/Groups/{id} | 获取服务分组详情
[**service_setting_group_delete**](ServiceSettingApi.md#service_setting_group_delete) | **DELETE** /ServiceSetting/Groups/{id} | 删除服务分组
[**service_setting_group_post**](ServiceSettingApi.md#service_setting_group_post) | **POST** /ServiceSetting/Groups | 添加服务分组
[**service_setting_group_put**](ServiceSettingApi.md#service_setting_group_put) | **PUT** /ServiceSetting/Groups/{id} | 更新服务分组
[**service_setting_groups**](ServiceSettingApi.md#service_setting_groups) | **GET** /ServiceSetting/Groups | 获取服务分组列表
[**service_setting_item**](ServiceSettingApi.md#service_setting_item) | **GET** /ServiceSetting/Items/{id} | 服务配置详情
[**service_setting_item_delete**](ServiceSettingApi.md#service_setting_item_delete) | **DELETE** /ServiceSetting/Items/{id} | 删除服务配置
[**service_setting_item_post**](ServiceSettingApi.md#service_setting_item_post) | **POST** /ServiceSetting/Items | 添加服务配置
[**service_setting_item_put**](ServiceSettingApi.md#service_setting_item_put) | **PUT** /ServiceSetting/Items/{id} | 更新服务配置
[**service_setting_items**](ServiceSettingApi.md#service_setting_items) | **GET** /ServiceSetting/Items | 服务配置列表
[**service_setting_post**](ServiceSettingApi.md#service_setting_post) | **POST** /ServiceSetting | 增加配置
[**service_setting_provider**](ServiceSettingApi.md#service_setting_provider) | **GET** /ServiceSetting/Providers/{id} | 获取服务商详情
[**service_setting_provider_delete**](ServiceSettingApi.md#service_setting_provider_delete) | **DELETE** /ServiceSetting/Providers/{id} | 删除服务商
[**service_setting_provider_post**](ServiceSettingApi.md#service_setting_provider_post) | **POST** /ServiceSetting/Providers | 添加服务商
[**service_setting_provider_put**](ServiceSettingApi.md#service_setting_provider_put) | **PUT** /ServiceSetting/Providers/{id} | 更新服务商
[**service_setting_providers**](ServiceSettingApi.md#service_setting_providers) | **GET** /ServiceSetting/Providers | 获取服务商列表
[**service_setting_put**](ServiceSettingApi.md#service_setting_put) | **PUT** /ServiceSetting/{id} | 更新配置
[**service_settings**](ServiceSettingApi.md#service_settings) | **GET** /ServiceSetting | 获取配置列表


# **service_setting**
> SettingsApiResponse service_setting(id)

获取配置详情

根据配置ID获取配置详情

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.settings_api_response import SettingsApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 配置ID

    try:
        # 获取配置详情
        api_response = api_instance.service_setting(id)
        print("The response of ServiceSettingApi->service_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 配置ID | 

### Return type

[**SettingsApiResponse**](SettingsApiResponse.md)

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

# **service_setting_delete**
> BooleanApiResponse service_setting_delete(id)

删除配置

根据配置ID删除配置

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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 配置ID

    try:
        # 删除配置
        api_response = api_instance.service_setting_delete(id)
        print("The response of ServiceSettingApi->service_setting_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 配置ID | 

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

# **service_setting_group**
> ServiceGroupApiResponse service_setting_group(id)

获取服务分组详情

根据服务分组ID获取服务分组详情

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.service_group_api_response import ServiceGroupApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 服务分组ID

    try:
        # 获取服务分组详情
        api_response = api_instance.service_setting_group(id)
        print("The response of ServiceSettingApi->service_setting_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 服务分组ID | 

### Return type

[**ServiceGroupApiResponse**](ServiceGroupApiResponse.md)

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

# **service_setting_group_delete**
> BooleanApiResponse service_setting_group_delete(id)

删除服务分组

根据服务分组ID删除服务分组

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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 服务分组ID

    try:
        # 删除服务分组
        api_response = api_instance.service_setting_group_delete(id)
        print("The response of ServiceSettingApi->service_setting_group_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_group_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 服务分组ID | 

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

# **service_setting_group_post**
> ServiceSettingGroupPostResultApiResponse service_setting_group_post(service_group=service_group)

添加服务分组

添加新的服务分组

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.service_group import ServiceGroup
from ZSGF.Client.models.service_setting_group_post_result_api_response import ServiceSettingGroupPostResultApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    service_group = ZSGF.Client.ServiceGroup() # ServiceGroup | 服务分组实体 (optional)

    try:
        # 添加服务分组
        api_response = api_instance.service_setting_group_post(service_group=service_group)
        print("The response of ServiceSettingApi->service_setting_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_group** | [**ServiceGroup**](ServiceGroup.md)| 服务分组实体 | [optional] 

### Return type

[**ServiceSettingGroupPostResultApiResponse**](ServiceSettingGroupPostResultApiResponse.md)

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

# **service_setting_group_put**
> BooleanApiResponse service_setting_group_put(id, service_group=service_group)

更新服务分组

根据服务分组ID更新服务分组信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.service_group import ServiceGroup
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 服务分组ID
    service_group = ZSGF.Client.ServiceGroup() # ServiceGroup | 服务分组实体 (optional)

    try:
        # 更新服务分组
        api_response = api_instance.service_setting_group_put(id, service_group=service_group)
        print("The response of ServiceSettingApi->service_setting_group_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_group_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 服务分组ID | 
 **service_group** | [**ServiceGroup**](ServiceGroup.md)| 服务分组实体 | [optional] 

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

# **service_setting_groups**
> ServiceGroupListApiResponse service_setting_groups(provider_id=provider_id, show_flag=show_flag)

获取服务分组列表

根据服务商ID和显示标志获取服务分组列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.service_group_list_api_response import ServiceGroupListApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    provider_id = 56 # int | 服务商ID (optional)
    show_flag = False # bool | 是否显示 (optional) (default to False)

    try:
        # 获取服务分组列表
        api_response = api_instance.service_setting_groups(provider_id=provider_id, show_flag=show_flag)
        print("The response of ServiceSettingApi->service_setting_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**| 服务商ID | [optional] 
 **show_flag** | **bool**| 是否显示 | [optional] [default to False]

### Return type

[**ServiceGroupListApiResponse**](ServiceGroupListApiResponse.md)

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

# **service_setting_item**
> ServiceItemApiResponse service_setting_item(id)

服务配置详情

根据服务配置ID获取服务配置详情

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.service_item_api_response import ServiceItemApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 服务配置ID

    try:
        # 服务配置详情
        api_response = api_instance.service_setting_item(id)
        print("The response of ServiceSettingApi->service_setting_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 服务配置ID | 

### Return type

[**ServiceItemApiResponse**](ServiceItemApiResponse.md)

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

# **service_setting_item_delete**
> BooleanApiResponse service_setting_item_delete(id)

删除服务配置

根据服务配置ID删除服务配置

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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 服务配置ID

    try:
        # 删除服务配置
        api_response = api_instance.service_setting_item_delete(id)
        print("The response of ServiceSettingApi->service_setting_item_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_item_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 服务配置ID | 

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

# **service_setting_item_post**
> ServiceSettingItemPostResultApiResponse service_setting_item_post(service_item=service_item)

添加服务配置

添加新的服务配置

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.service_item import ServiceItem
from ZSGF.Client.models.service_setting_item_post_result_api_response import ServiceSettingItemPostResultApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    service_item = ZSGF.Client.ServiceItem() # ServiceItem | 服务配置实体 (optional)

    try:
        # 添加服务配置
        api_response = api_instance.service_setting_item_post(service_item=service_item)
        print("The response of ServiceSettingApi->service_setting_item_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_item_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_item** | [**ServiceItem**](ServiceItem.md)| 服务配置实体 | [optional] 

### Return type

[**ServiceSettingItemPostResultApiResponse**](ServiceSettingItemPostResultApiResponse.md)

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

# **service_setting_item_put**
> BooleanApiResponse service_setting_item_put(id, service_item=service_item)

更新服务配置

根据服务配置ID更新服务配置信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.service_item import ServiceItem
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 服务配置ID
    service_item = ZSGF.Client.ServiceItem() # ServiceItem | 服务配置实体 (optional)

    try:
        # 更新服务配置
        api_response = api_instance.service_setting_item_put(id, service_item=service_item)
        print("The response of ServiceSettingApi->service_setting_item_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_item_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 服务配置ID | 
 **service_item** | [**ServiceItem**](ServiceItem.md)| 服务配置实体 | [optional] 

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

# **service_setting_items**
> ServiceItemListApiResponse service_setting_items(biz_code=biz_code, provider_code=provider_code, group_code=group_code, show_flag=show_flag)

服务配置列表

根据业务代码、服务商代码、分组代码和显示标志获取服务配置列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.service_item_list_api_response import ServiceItemListApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    biz_code = 'biz_code_example' # str | 业务代码 (optional)
    provider_code = 'provider_code_example' # str | 服务商代码 (optional)
    group_code = 'group_code_example' # str | 分组代码 (optional)
    show_flag = False # bool | 是否显示 (optional) (default to False)

    try:
        # 服务配置列表
        api_response = api_instance.service_setting_items(biz_code=biz_code, provider_code=provider_code, group_code=group_code, show_flag=show_flag)
        print("The response of ServiceSettingApi->service_setting_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biz_code** | **str**| 业务代码 | [optional] 
 **provider_code** | **str**| 服务商代码 | [optional] 
 **group_code** | **str**| 分组代码 | [optional] 
 **show_flag** | **bool**| 是否显示 | [optional] [default to False]

### Return type

[**ServiceItemListApiResponse**](ServiceItemListApiResponse.md)

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

# **service_setting_post**
> ServiceSettingSettingPostResultApiResponse service_setting_post(settings=settings)

增加配置

添加新的配置

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.service_setting_setting_post_result_api_response import ServiceSettingSettingPostResultApiResponse
from ZSGF.Client.models.settings import Settings
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    settings = ZSGF.Client.Settings() # Settings | 配置实体 (optional)

    try:
        # 增加配置
        api_response = api_instance.service_setting_post(settings=settings)
        print("The response of ServiceSettingApi->service_setting_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**Settings**](Settings.md)| 配置实体 | [optional] 

### Return type

[**ServiceSettingSettingPostResultApiResponse**](ServiceSettingSettingPostResultApiResponse.md)

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

# **service_setting_provider**
> ServiceProviderApiResponse service_setting_provider(id)

获取服务商详情

根据服务商ID获取服务商详情

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.service_provider_api_response import ServiceProviderApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 服务商ID

    try:
        # 获取服务商详情
        api_response = api_instance.service_setting_provider(id)
        print("The response of ServiceSettingApi->service_setting_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 服务商ID | 

### Return type

[**ServiceProviderApiResponse**](ServiceProviderApiResponse.md)

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

# **service_setting_provider_delete**
> BooleanApiResponse service_setting_provider_delete(id)

删除服务商

根据服务商ID删除服务商

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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 服务商ID

    try:
        # 删除服务商
        api_response = api_instance.service_setting_provider_delete(id)
        print("The response of ServiceSettingApi->service_setting_provider_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_provider_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 服务商ID | 

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

# **service_setting_provider_post**
> ServiceSettingProviderPostResultApiResponse service_setting_provider_post(service_provider=service_provider)

添加服务商

添加新的服务商

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.service_provider import ServiceProvider
from ZSGF.Client.models.service_setting_provider_post_result_api_response import ServiceSettingProviderPostResultApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    service_provider = ZSGF.Client.ServiceProvider() # ServiceProvider | 服务商实体 (optional)

    try:
        # 添加服务商
        api_response = api_instance.service_setting_provider_post(service_provider=service_provider)
        print("The response of ServiceSettingApi->service_setting_provider_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_provider_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_provider** | [**ServiceProvider**](ServiceProvider.md)| 服务商实体 | [optional] 

### Return type

[**ServiceSettingProviderPostResultApiResponse**](ServiceSettingProviderPostResultApiResponse.md)

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

# **service_setting_provider_put**
> BooleanApiResponse service_setting_provider_put(id, service_provider=service_provider)

更新服务商

根据服务商ID更新服务商信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.service_provider import ServiceProvider
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 服务商ID
    service_provider = ZSGF.Client.ServiceProvider() # ServiceProvider | 服务商实体 (optional)

    try:
        # 更新服务商
        api_response = api_instance.service_setting_provider_put(id, service_provider=service_provider)
        print("The response of ServiceSettingApi->service_setting_provider_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_provider_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 服务商ID | 
 **service_provider** | [**ServiceProvider**](ServiceProvider.md)| 服务商实体 | [optional] 

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

# **service_setting_providers**
> ServiceProviderListApiResponse service_setting_providers(biz_code=biz_code, show_flag=show_flag)

获取服务商列表

根据业务代码和显示标志获取服务商列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.service_provider_list_api_response import ServiceProviderListApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    biz_code = 'biz_code_example' # str | 业务代码 (optional)
    show_flag = False # bool | 是否显示 (optional) (default to False)

    try:
        # 获取服务商列表
        api_response = api_instance.service_setting_providers(biz_code=biz_code, show_flag=show_flag)
        print("The response of ServiceSettingApi->service_setting_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biz_code** | **str**| 业务代码 | [optional] 
 **show_flag** | **bool**| 是否显示 | [optional] [default to False]

### Return type

[**ServiceProviderListApiResponse**](ServiceProviderListApiResponse.md)

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

# **service_setting_put**
> BooleanApiResponse service_setting_put(id, settings=settings)

更新配置

根据配置ID更新配置信息

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse
from ZSGF.Client.models.settings import Settings
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    id = 56 # int | 配置ID
    settings = ZSGF.Client.Settings() # Settings | 配置实体 (optional)

    try:
        # 更新配置
        api_response = api_instance.service_setting_put(id, settings=settings)
        print("The response of ServiceSettingApi->service_setting_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_setting_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 配置ID | 
 **settings** | [**Settings**](Settings.md)| 配置实体 | [optional] 

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

# **service_settings**
> SettingsListApiResponse service_settings(biz_code, biz_id, provider_code=provider_code, group_code=group_code, tag=tag, code=code)

获取配置列表

根据业务代码、业务标识、服务商代码、分组代码、标签和配置项代码获取配置列表

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.settings_list_api_response import SettingsListApiResponse
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
    api_instance = ZSGF.Client.ServiceSettingApi(api_client)
    biz_code = 'biz_code_example' # str | 业务代码
    biz_id = 'biz_id_example' # str | 业务标识
    provider_code = 'provider_code_example' # str | 服务商代码 (optional)
    group_code = 'group_code_example' # str | 分组代码 (optional)
    tag = 'tag_example' # str | 标签 (optional)
    code = 'code_example' # str | 配置项代码 (optional)

    try:
        # 获取配置列表
        api_response = api_instance.service_settings(biz_code, biz_id, provider_code=provider_code, group_code=group_code, tag=tag, code=code)
        print("The response of ServiceSettingApi->service_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSettingApi->service_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biz_code** | **str**| 业务代码 | 
 **biz_id** | **str**| 业务标识 | 
 **provider_code** | **str**| 服务商代码 | [optional] 
 **group_code** | **str**| 分组代码 | [optional] 
 **tag** | **str**| 标签 | [optional] 
 **code** | **str**| 配置项代码 | [optional] 

### Return type

[**SettingsListApiResponse**](SettingsListApiResponse.md)

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

