# AppInfoItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_key** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 

## Example

```python
from ZSGF.Client.models.app_info_item import AppInfoItem

# TODO update the JSON string below
json = "{}"
# create an instance of AppInfoItem from a JSON string
app_info_item_instance = AppInfoItem.from_json(json)
# print the JSON string representation of the object
print(AppInfoItem.to_json())

# convert the object into a dict
app_info_item_dict = app_info_item_instance.to_dict()
# create an instance of AppInfoItem from a dict
app_info_item_from_dict = AppInfoItem.from_dict(app_info_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


