# ProjectListResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**ProjectListResult**](ProjectListResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.project_list_result_api_response import ProjectListResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectListResultApiResponse from a JSON string
project_list_result_api_response_instance = ProjectListResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectListResultApiResponse.to_json())

# convert the object into a dict
project_list_result_api_response_dict = project_list_result_api_response_instance.to_dict()
# create an instance of ProjectListResultApiResponse from a dict
project_list_result_api_response_from_dict = ProjectListResultApiResponse.from_dict(project_list_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


