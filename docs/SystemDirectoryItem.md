# SystemDirectoryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**file_size** | **int** |  | [optional] 

## Example

```python
from ZSGF.Client.models.system_directory_item import SystemDirectoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of SystemDirectoryItem from a JSON string
system_directory_item_instance = SystemDirectoryItem.from_json(json)
# print the JSON string representation of the object
print(SystemDirectoryItem.to_json())

# convert the object into a dict
system_directory_item_dict = system_directory_item_instance.to_dict()
# create an instance of SystemDirectoryItem from a dict
system_directory_item_from_dict = SystemDirectoryItem.from_dict(system_directory_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


