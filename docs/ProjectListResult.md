# ProjectListResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[Project]**](Project.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.project_list_result import ProjectListResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectListResult from a JSON string
project_list_result_instance = ProjectListResult.from_json(json)
# print the JSON string representation of the object
print(ProjectListResult.to_json())

# convert the object into a dict
project_list_result_dict = project_list_result_instance.to_dict()
# create an instance of ProjectListResult from a dict
project_list_result_from_dict = ProjectListResult.from_dict(project_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


