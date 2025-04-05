# SystemFileListResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directories** | [**List[SystemDirectoryItem]**](SystemDirectoryItem.md) |  | [optional] 
**files** | [**List[SystemFileItem]**](SystemFileItem.md) |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from ZSGF.Client.models.system_file_list_result import SystemFileListResult

# TODO update the JSON string below
json = "{}"
# create an instance of SystemFileListResult from a JSON string
system_file_list_result_instance = SystemFileListResult.from_json(json)
# print the JSON string representation of the object
print(SystemFileListResult.to_json())

# convert the object into a dict
system_file_list_result_dict = system_file_list_result_instance.to_dict()
# create an instance of SystemFileListResult from a dict
system_file_list_result_from_dict = SystemFileListResult.from_dict(system_file_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


