# UserProfileResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_key** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**union_id** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**user_name** | **str** |  | [optional] 
**phone_is_valid** | **bool** |  | [optional] 
**data** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_is_valid** | **bool** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**avatar** | **str** |  | [optional] 
**currencies** | [**List[UserCurrency]**](UserCurrency.md) |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.user_profile_result import UserProfileResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileResult from a JSON string
user_profile_result_instance = UserProfileResult.from_json(json)
# print the JSON string representation of the object
print(UserProfileResult.to_json())

# convert the object into a dict
user_profile_result_dict = user_profile_result_instance.to_dict()
# create an instance of UserProfileResult from a dict
user_profile_result_from_dict = UserProfileResult.from_dict(user_profile_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


