# GrantResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.grant_result import GrantResult

# TODO update the JSON string below
json = "{}"
# create an instance of GrantResult from a JSON string
grant_result_instance = GrantResult.from_json(json)
# print the JSON string representation of the object
print(GrantResult.to_json())

# convert the object into a dict
grant_result_dict = grant_result_instance.to_dict()
# create an instance of GrantResult from a dict
grant_result_from_dict = GrantResult.from_dict(grant_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


