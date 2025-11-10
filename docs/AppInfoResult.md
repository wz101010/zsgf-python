# AppInfoResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**AppInfoItem**](AppInfoItem.md) |  | [optional] 
**props** | [**List[AppProperty]**](AppProperty.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.app_info_result import AppInfoResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppInfoResult from a JSON string
app_info_result_instance = AppInfoResult.from_json(json)
# print the JSON string representation of the object
print(AppInfoResult.to_json())

# convert the object into a dict
app_info_result_dict = app_info_result_instance.to_dict()
# create an instance of AppInfoResult from a dict
app_info_result_from_dict = AppInfoResult.from_dict(app_info_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


