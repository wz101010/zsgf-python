# ServiceGroupApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**ServiceGroup**](ServiceGroup.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.service_group_api_response import ServiceGroupApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceGroupApiResponse from a JSON string
service_group_api_response_instance = ServiceGroupApiResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceGroupApiResponse.to_json())

# convert the object into a dict
service_group_api_response_dict = service_group_api_response_instance.to_dict()
# create an instance of ServiceGroupApiResponse from a dict
service_group_api_response_from_dict = ServiceGroupApiResponse.from_dict(service_group_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


