# PresetPayToolInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **List[str]** |  | [optional] 
**assert_type_code** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.preset_pay_tool_info import PresetPayToolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PresetPayToolInfo from a JSON string
preset_pay_tool_info_instance = PresetPayToolInfo.from_json(json)
# print the JSON string representation of the object
print(PresetPayToolInfo.to_json())

# convert the object into a dict
preset_pay_tool_info_dict = preset_pay_tool_info_instance.to_dict()
# create an instance of PresetPayToolInfo from a dict
preset_pay_tool_info_from_dict = PresetPayToolInfo.from_dict(preset_pay_tool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


