# ServiceSettingProviderPostResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**ServiceSettingProviderPostResult**](ServiceSettingProviderPostResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.service_setting_provider_post_result_api_response import ServiceSettingProviderPostResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSettingProviderPostResultApiResponse from a JSON string
service_setting_provider_post_result_api_response_instance = ServiceSettingProviderPostResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceSettingProviderPostResultApiResponse.to_json())

# convert the object into a dict
service_setting_provider_post_result_api_response_dict = service_setting_provider_post_result_api_response_instance.to_dict()
# create an instance of ServiceSettingProviderPostResultApiResponse from a dict
service_setting_provider_post_result_api_response_from_dict = ServiceSettingProviderPostResultApiResponse.from_dict(service_setting_provider_post_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


