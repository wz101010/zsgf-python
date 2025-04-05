# FileListResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**FileListResult**](FileListResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.file_list_result_api_response import FileListResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileListResultApiResponse from a JSON string
file_list_result_api_response_instance = FileListResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(FileListResultApiResponse.to_json())

# convert the object into a dict
file_list_result_api_response_dict = file_list_result_api_response_instance.to_dict()
# create an instance of FileListResultApiResponse from a dict
file_list_result_api_response_from_dict = FileListResultApiResponse.from_dict(file_list_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


