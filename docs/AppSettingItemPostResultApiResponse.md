# AppSettingItemPostResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**AppSettingItemPostResult**](AppSettingItemPostResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.app_setting_item_post_result_api_response import AppSettingItemPostResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingItemPostResultApiResponse from a JSON string
app_setting_item_post_result_api_response_instance = AppSettingItemPostResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(AppSettingItemPostResultApiResponse.to_json())

# convert the object into a dict
app_setting_item_post_result_api_response_dict = app_setting_item_post_result_api_response_instance.to_dict()
# create an instance of AppSettingItemPostResultApiResponse from a dict
app_setting_item_post_result_api_response_from_dict = AppSettingItemPostResultApiResponse.from_dict(app_setting_item_post_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


