# UserFollowingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_followers** | **int** |  | [optional] 
**data** | [**List[FollowerModel]**](FollowerModel.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.user_following_result import UserFollowingResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserFollowingResult from a JSON string
user_following_result_instance = UserFollowingResult.from_json(json)
# print the JSON string representation of the object
print(UserFollowingResult.to_json())

# convert the object into a dict
user_following_result_dict = user_following_result_instance.to_dict()
# create an instance of UserFollowingResult from a dict
user_following_result_from_dict = UserFollowingResult.from_dict(user_following_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


