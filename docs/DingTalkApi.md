# ZSGF.Client.DingTalkApi

All URIs are relative to *https://api-dev.zashigaofa.cn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ding_talk_user_info**](DingTalkApi.md#ding_talk_user_info) | **GET** /DingTalk/{appKey}/UserInfo | 获取用户资料


# **ding_talk_user_info**
> StringApiResponse ding_talk_user_info(app_key, code=code)

获取用户资料

根据钉钉用户授权码获取用户的详细资料。

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
    api_instance = ZSGF.Client.DingTalkApi(api_client)
    app_key = 'app_key_example' # str | 
    code = 'code_example' # str | 钉钉用户授权码 (optional)

    try:
        # 获取用户资料
        api_response = api_instance.ding_talk_user_info(app_key, code=code)
        print("The response of DingTalkApi->ding_talk_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DingTalkApi->ding_talk_user_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **code** | **str**| 钉钉用户授权码 | [optional] 

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

