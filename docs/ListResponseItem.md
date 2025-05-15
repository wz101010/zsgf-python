# ListResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 
**last_update** | **datetime** |  | [optional] 

## Example

```python
from ZSGF.Client.models.list_response_item import ListResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseItem from a JSON string
list_response_item_instance = ListResponseItem.from_json(json)
# print the JSON string representation of the object
print(ListResponseItem.to_json())

# convert the object into a dict
list_response_item_dict = list_response_item_instance.to_dict()
# create an instance of ListResponseItem from a dict
list_response_item_from_dict = ListResponseItem.from_dict(list_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


