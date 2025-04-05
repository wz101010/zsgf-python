# UserSettingListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[UserSetting]**](UserSetting.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.user_setting_list_api_response import UserSettingListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingListApiResponse from a JSON string
user_setting_list_api_response_instance = UserSettingListApiResponse.from_json(json)
# print the JSON string representation of the object
print(UserSettingListApiResponse.to_json())

# convert the object into a dict
user_setting_list_api_response_dict = user_setting_list_api_response_instance.to_dict()
# create an instance of UserSettingListApiResponse from a dict
user_setting_list_api_response_from_dict = UserSettingListApiResponse.from_dict(user_setting_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


