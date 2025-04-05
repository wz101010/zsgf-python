# AppInfoResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**AppInfoResult**](AppInfoResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.app_info_result_api_response import AppInfoResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppInfoResultApiResponse from a JSON string
app_info_result_api_response_instance = AppInfoResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(AppInfoResultApiResponse.to_json())

# convert the object into a dict
app_info_result_api_response_dict = app_info_result_api_response_instance.to_dict()
# create an instance of AppInfoResultApiResponse from a dict
app_info_result_api_response_from_dict = AppInfoResultApiResponse.from_dict(app_info_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


