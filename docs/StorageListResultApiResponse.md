# StorageListResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**StorageListResult**](StorageListResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.storage_list_result_api_response import StorageListResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StorageListResultApiResponse from a JSON string
storage_list_result_api_response_instance = StorageListResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(StorageListResultApiResponse.to_json())

# convert the object into a dict
storage_list_result_api_response_dict = storage_list_result_api_response_instance.to_dict()
# create an instance of StorageListResultApiResponse from a dict
storage_list_result_api_response_from_dict = StorageListResultApiResponse.from_dict(storage_list_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


