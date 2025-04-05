# FileItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**file_size** | **int** |  | [optional] 

## Example

```python
from ZSGF.Client.models.file_item import FileItem

# TODO update the JSON string below
json = "{}"
# create an instance of FileItem from a JSON string
file_item_instance = FileItem.from_json(json)
# print the JSON string representation of the object
print(FileItem.to_json())

# convert the object into a dict
file_item_dict = file_item_instance.to_dict()
# create an instance of FileItem from a dict
file_item_from_dict = FileItem.from_dict(file_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


