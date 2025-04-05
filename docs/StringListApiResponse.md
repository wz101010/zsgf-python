# StringListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | **List[str]** | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.string_list_api_response import StringListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StringListApiResponse from a JSON string
string_list_api_response_instance = StringListApiResponse.from_json(json)
# print the JSON string representation of the object
print(StringListApiResponse.to_json())

# convert the object into a dict
string_list_api_response_dict = string_list_api_response_instance.to_dict()
# create an instance of StringListApiResponse from a dict
string_list_api_response_from_dict = StringListApiResponse.from_dict(string_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


