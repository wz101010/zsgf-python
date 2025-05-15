# Int64ApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | **int** | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.int64_api_response import Int64ApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Int64ApiResponse from a JSON string
int64_api_response_instance = Int64ApiResponse.from_json(json)
# print the JSON string representation of the object
print(Int64ApiResponse.to_json())

# convert the object into a dict
int64_api_response_dict = int64_api_response_instance.to_dict()
# create an instance of Int64ApiResponse from a dict
int64_api_response_from_dict = Int64ApiResponse.from_dict(int64_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


