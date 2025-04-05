# UserListResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[AppUserListResponse]**](AppUserListResponse.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.user_list_result import UserListResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserListResult from a JSON string
user_list_result_instance = UserListResult.from_json(json)
# print the JSON string representation of the object
print(UserListResult.to_json())

# convert the object into a dict
user_list_result_dict = user_list_result_instance.to_dict()
# create an instance of UserListResult from a dict
user_list_result_from_dict = UserListResult.from_dict(user_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


