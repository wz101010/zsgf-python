# SystemFileItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**file_size** | **int** |  | [optional] 

## Example

```python
from ZSGF.Client.models.system_file_item import SystemFileItem

# TODO update the JSON string below
json = "{}"
# create an instance of SystemFileItem from a JSON string
system_file_item_instance = SystemFileItem.from_json(json)
# print the JSON string representation of the object
print(SystemFileItem.to_json())

# convert the object into a dict
system_file_item_dict = system_file_item_instance.to_dict()
# create an instance of SystemFileItem from a dict
system_file_item_from_dict = SystemFileItem.from_dict(system_file_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


