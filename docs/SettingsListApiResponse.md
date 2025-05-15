# SettingsListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[Settings]**](Settings.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.settings_list_api_response import SettingsListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsListApiResponse from a JSON string
settings_list_api_response_instance = SettingsListApiResponse.from_json(json)
# print the JSON string representation of the object
print(SettingsListApiResponse.to_json())

# convert the object into a dict
settings_list_api_response_dict = settings_list_api_response_instance.to_dict()
# create an instance of SettingsListApiResponse from a dict
settings_list_api_response_from_dict = SettingsListApiResponse.from_dict(settings_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


