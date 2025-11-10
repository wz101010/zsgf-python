# DirectoryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**file_size** | **int** |  | [optional] 

## Example

```python
from ZSGF.Client.models.directory_item import DirectoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of DirectoryItem from a JSON string
directory_item_instance = DirectoryItem.from_json(json)
# print the JSON string representation of the object
print(DirectoryItem.to_json())

# convert the object into a dict
directory_item_dict = directory_item_instance.to_dict()
# create an instance of DirectoryItem from a dict
directory_item_from_dict = DirectoryItem.from_dict(directory_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


