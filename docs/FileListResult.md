# FileListResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directories** | [**List[DirectoryItem]**](DirectoryItem.md) |  | [optional] 
**files** | [**List[FileItem]**](FileItem.md) |  | [optional] 
**total_directories** | **int** |  | [optional] 
**total_files** | **int** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from ZSGF.Client.models.file_list_result import FileListResult

# TODO update the JSON string below
json = "{}"
# create an instance of FileListResult from a JSON string
file_list_result_instance = FileListResult.from_json(json)
# print the JSON string representation of the object
print(FileListResult.to_json())

# convert the object into a dict
file_list_result_dict = file_list_result_instance.to_dict()
# create an instance of FileListResult from a dict
file_list_result_from_dict = FileListResult.from_dict(file_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


