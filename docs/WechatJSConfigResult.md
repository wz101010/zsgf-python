# WechatJSConfigResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**noncestr** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**app_key** | **str** |  | [optional] 
**js_api_list** | **List[str]** |  | [optional] 

## Example

```python
from ZSGF.Client.models.wechat_js_config_result import WechatJSConfigResult

# TODO update the JSON string below
json = "{}"
# create an instance of WechatJSConfigResult from a JSON string
wechat_js_config_result_instance = WechatJSConfigResult.from_json(json)
# print the JSON string representation of the object
print(WechatJSConfigResult.to_json())

# convert the object into a dict
wechat_js_config_result_dict = wechat_js_config_result_instance.to_dict()
# create an instance of WechatJSConfigResult from a dict
wechat_js_config_result_from_dict = WechatJSConfigResult.from_dict(wechat_js_config_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


