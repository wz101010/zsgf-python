# AppSettingSettingPostResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**AppSettingSettingPostResult**](AppSettingSettingPostResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.app_setting_setting_post_result_api_response import AppSettingSettingPostResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingSettingPostResultApiResponse from a JSON string
app_setting_setting_post_result_api_response_instance = AppSettingSettingPostResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(AppSettingSettingPostResultApiResponse.to_json())

# convert the object into a dict
app_setting_setting_post_result_api_response_dict = app_setting_setting_post_result_api_response_instance.to_dict()
# create an instance of AppSettingSettingPostResultApiResponse from a dict
app_setting_setting_post_result_api_response_from_dict = AppSettingSettingPostResultApiResponse.from_dict(app_setting_setting_post_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


