# ObjectListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | **List[object]** | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.object_list_api_response import ObjectListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectListApiResponse from a JSON string
object_list_api_response_instance = ObjectListApiResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectListApiResponse.to_json())

# convert the object into a dict
object_list_api_response_dict = object_list_api_response_instance.to_dict()
# create an instance of ObjectListApiResponse from a dict
object_list_api_response_from_dict = ObjectListApiResponse.from_dict(object_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


