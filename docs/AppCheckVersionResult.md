# AppCheckVersionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **List[str]** |  | [optional] 
**new_versions** | **List[str]** |  | [optional] 

## Example

```python
from ZSGF.Client.models.app_check_version_result import AppCheckVersionResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppCheckVersionResult from a JSON string
app_check_version_result_instance = AppCheckVersionResult.from_json(json)
# print the JSON string representation of the object
print(AppCheckVersionResult.to_json())

# convert the object into a dict
app_check_version_result_dict = app_check_version_result_instance.to_dict()
# create an instance of AppCheckVersionResult from a dict
app_check_version_result_from_dict = AppCheckVersionResult.from_dict(app_check_version_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


