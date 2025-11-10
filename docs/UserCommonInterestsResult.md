# UserCommonInterestsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_followers** | **int** |  | [optional] 
**data** | [**List[CommonFriendModel]**](CommonFriendModel.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.user_common_interests_result import UserCommonInterestsResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserCommonInterestsResult from a JSON string
user_common_interests_result_instance = UserCommonInterestsResult.from_json(json)
# print the JSON string representation of the object
print(UserCommonInterestsResult.to_json())

# convert the object into a dict
user_common_interests_result_dict = user_common_interests_result_instance.to_dict()
# create an instance of UserCommonInterestsResult from a dict
user_common_interests_result_from_dict = UserCommonInterestsResult.from_dict(user_common_interests_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


