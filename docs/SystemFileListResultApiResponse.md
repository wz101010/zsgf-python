# SystemFileListResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**SystemFileListResult**](SystemFileListResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.system_file_list_result_api_response import SystemFileListResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemFileListResultApiResponse from a JSON string
system_file_list_result_api_response_instance = SystemFileListResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(SystemFileListResultApiResponse.to_json())

# convert the object into a dict
system_file_list_result_api_response_dict = system_file_list_result_api_response_instance.to_dict()
# create an instance of SystemFileListResultApiResponse from a dict
system_file_list_result_api_response_from_dict = SystemFileListResultApiResponse.from_dict(system_file_list_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


