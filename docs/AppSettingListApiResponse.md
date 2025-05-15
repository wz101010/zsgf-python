# AppSettingListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[AppSetting]**](AppSetting.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.app_setting_list_api_response import AppSettingListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingListApiResponse from a JSON string
app_setting_list_api_response_instance = AppSettingListApiResponse.from_json(json)
# print the JSON string representation of the object
print(AppSettingListApiResponse.to_json())

# convert the object into a dict
app_setting_list_api_response_dict = app_setting_list_api_response_instance.to_dict()
# create an instance of AppSettingListApiResponse from a dict
app_setting_list_api_response_from_dict = AppSettingListApiResponse.from_dict(app_setting_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


