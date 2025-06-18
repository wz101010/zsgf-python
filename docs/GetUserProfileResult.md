# GetUserProfileResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | [optional] 
**currencies** | [**List[UserCurrency]**](UserCurrency.md) |  | [optional] 
**role** | **str** |  | [optional] 
**location** | [**GeoLocation**](GeoLocation.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.get_user_profile_result import GetUserProfileResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserProfileResult from a JSON string
get_user_profile_result_instance = GetUserProfileResult.from_json(json)
# print the JSON string representation of the object
print(GetUserProfileResult.to_json())

# convert the object into a dict
get_user_profile_result_dict = get_user_profile_result_instance.to_dict()
# create an instance of GetUserProfileResult from a dict
get_user_profile_result_from_dict = GetUserProfileResult.from_dict(get_user_profile_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


