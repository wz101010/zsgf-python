# AuthorizeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 

## Example

```python
from ZSGF.Client.models.authorize_result import AuthorizeResult

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeResult from a JSON string
authorize_result_instance = AuthorizeResult.from_json(json)
# print the JSON string representation of the object
print(AuthorizeResult.to_json())

# convert the object into a dict
authorize_result_dict = authorize_result_instance.to_dict()
# create an instance of AuthorizeResult from a dict
authorize_result_from_dict = AuthorizeResult.from_dict(authorize_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


