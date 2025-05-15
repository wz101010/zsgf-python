# StringApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | **str** | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.string_api_response import StringApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StringApiResponse from a JSON string
string_api_response_instance = StringApiResponse.from_json(json)
# print the JSON string representation of the object
print(StringApiResponse.to_json())

# convert the object into a dict
string_api_response_dict = string_api_response_instance.to_dict()
# create an instance of StringApiResponse from a dict
string_api_response_from_dict = StringApiResponse.from_dict(string_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


