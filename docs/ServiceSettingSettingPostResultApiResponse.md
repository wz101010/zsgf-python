# ServiceSettingSettingPostResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**ServiceSettingSettingPostResult**](ServiceSettingSettingPostResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.service_setting_setting_post_result_api_response import ServiceSettingSettingPostResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettingSettingPostResultApiResponse from a JSON string
service_setting_setting_post_result_api_response_instance = ServiceSettingSettingPostResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceSettingSettingPostResultApiResponse.to_json())

# convert the object into a dict
service_setting_setting_post_result_api_response_dict = service_setting_setting_post_result_api_response_instance.to_dict()
# create an instance of ServiceSettingSettingPostResultApiResponse from a dict
service_setting_setting_post_result_api_response_from_dict = ServiceSettingSettingPostResultApiResponse.from_dict(service_setting_setting_post_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


