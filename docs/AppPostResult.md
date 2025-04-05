# AppPostResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**server_path** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.app_post_result import AppPostResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppPostResult from a JSON string
app_post_result_instance = AppPostResult.from_json(json)
# print the JSON string representation of the object
print(AppPostResult.to_json())

# convert the object into a dict
app_post_result_dict = app_post_result_instance.to_dict()
# create an instance of AppPostResult from a dict
app_post_result_from_dict = AppPostResult.from_dict(app_post_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


