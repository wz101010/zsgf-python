# ServiceGroupListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[ServiceGroup]**](ServiceGroup.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.service_group_list_api_response import ServiceGroupListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceGroupListApiResponse from a JSON string
service_group_list_api_response_instance = ServiceGroupListApiResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceGroupListApiResponse.to_json())

# convert the object into a dict
service_group_list_api_response_dict = service_group_list_api_response_instance.to_dict()
# create an instance of ServiceGroupListApiResponse from a dict
service_group_list_api_response_from_dict = ServiceGroupListApiResponse.from_dict(service_group_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


