# BooleanApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | **bool** | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.boolean_api_response import BooleanApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanApiResponse from a JSON string
boolean_api_response_instance = BooleanApiResponse.from_json(json)
# print the JSON string representation of the object
print(BooleanApiResponse.to_json())

# convert the object into a dict
boolean_api_response_dict = boolean_api_response_instance.to_dict()
# create an instance of BooleanApiResponse from a dict
boolean_api_response_from_dict = BooleanApiResponse.from_dict(boolean_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


