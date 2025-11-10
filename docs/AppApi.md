# ZSGF.Client.AppApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_info**](AppApi.md#app_info) | **GET** /App/{appKey}/Info | 应用详情


# **app_info**
> AppInfoResultApiResponse app_info(app_key, prop_code=prop_code)

应用详情

根据应用Key获取应用的详细信息和属性。

### Example

* Bearer Authentication (Bearer):

```python
import ZSGF.Client
from ZSGF.Client.models.app_info_result_api_response import AppInfoResultApiResponse
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
    api_instance = ZSGF.Client.AppApi(api_client)
    app_key = 'app_key_example' # str | 
    prop_code = 'prop_code_example' # str | 属性代码 (optional)

    try:
        # 应用详情
        api_response = api_instance.app_info(app_key, prop_code=prop_code)
        print("The response of AppApi->app_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->app_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **prop_code** | **str**| 属性代码 | [optional] 

### Return type

[**AppInfoResultApiResponse**](AppInfoResultApiResponse.md)

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

