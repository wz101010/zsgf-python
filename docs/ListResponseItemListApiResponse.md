# ListResponseItemListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[ListResponseItem]**](ListResponseItem.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.list_response_item_list_api_response import ListResponseItemListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseItemListApiResponse from a JSON string
list_response_item_list_api_response_instance = ListResponseItemListApiResponse.from_json(json)
# print the JSON string representation of the object
print(ListResponseItemListApiResponse.to_json())

# convert the object into a dict
list_response_item_list_api_response_dict = list_response_item_list_api_response_instance.to_dict()
# create an instance of ListResponseItemListApiResponse from a dict
list_response_item_list_api_response_from_dict = ListResponseItemListApiResponse.from_dict(list_response_item_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


