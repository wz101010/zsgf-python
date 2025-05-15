# AppSettingProviderPostResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**AppSettingProviderPostResult**](AppSettingProviderPostResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.app_setting_provider_post_result_api_response import AppSettingProviderPostResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingProviderPostResultApiResponse from a JSON string
app_setting_provider_post_result_api_response_instance = AppSettingProviderPostResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(AppSettingProviderPostResultApiResponse.to_json())

# convert the object into a dict
app_setting_provider_post_result_api_response_dict = app_setting_provider_post_result_api_response_instance.to_dict()
# create an instance of AppSettingProviderPostResultApiResponse from a dict
app_setting_provider_post_result_api_response_from_dict = AppSettingProviderPostResultApiResponse.from_dict(app_setting_provider_post_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


