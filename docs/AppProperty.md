# AppProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**desc** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.app_property import AppProperty

# TODO update the JSON string below
json = "{}"
# create an instance of AppProperty from a JSON string
app_property_instance = AppProperty.from_json(json)
# print the JSON string representation of the object
print(AppProperty.to_json())

# convert the object into a dict
app_property_dict = app_property_instance.to_dict()
# create an instance of AppProperty from a dict
app_property_from_dict = AppProperty.from_dict(app_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


