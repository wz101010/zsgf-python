# SettingsApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**Settings**](Settings.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.settings_api_response import SettingsApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsApiResponse from a JSON string
settings_api_response_instance = SettingsApiResponse.from_json(json)
# print the JSON string representation of the object
print(SettingsApiResponse.to_json())

# convert the object into a dict
settings_api_response_dict = settings_api_response_instance.to_dict()
# create an instance of SettingsApiResponse from a dict
settings_api_response_from_dict = SettingsApiResponse.from_dict(settings_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


