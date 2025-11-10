# AccessTokenListResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[UserAccessToken]**](UserAccessToken.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.access_token_list_result import AccessTokenListResult

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenListResult from a JSON string
access_token_list_result_instance = AccessTokenListResult.from_json(json)
# print the JSON string representation of the object
print(AccessTokenListResult.to_json())

# convert the object into a dict
access_token_list_result_dict = access_token_list_result_instance.to_dict()
# create an instance of AccessTokenListResult from a dict
access_token_list_result_from_dict = AccessTokenListResult.from_dict(access_token_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


