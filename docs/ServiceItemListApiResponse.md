# ServiceItemListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[ServiceItem]**](ServiceItem.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.service_item_list_api_response import ServiceItemListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceItemListApiResponse from a JSON string
service_item_list_api_response_instance = ServiceItemListApiResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceItemListApiResponse.to_json())

# convert the object into a dict
service_item_list_api_response_dict = service_item_list_api_response_instance.to_dict()
# create an instance of ServiceItemListApiResponse from a dict
service_item_list_api_response_from_dict = ServiceItemListApiResponse.from_dict(service_item_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


