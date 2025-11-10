# WechatJSConfigResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**WechatJSConfigResult**](WechatJSConfigResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.wechat_js_config_result_api_response import WechatJSConfigResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WechatJSConfigResultApiResponse from a JSON string
wechat_js_config_result_api_response_instance = WechatJSConfigResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(WechatJSConfigResultApiResponse.to_json())

# convert the object into a dict
wechat_js_config_result_api_response_dict = wechat_js_config_result_api_response_instance.to_dict()
# create an instance of WechatJSConfigResultApiResponse from a dict
wechat_js_config_result_api_response_from_dict = WechatJSConfigResultApiResponse.from_dict(wechat_js_config_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


