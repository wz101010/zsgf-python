# UserFollowersResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_followers** | **int** |  | [optional] 
**data** | [**List[FollowerModel]**](FollowerModel.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.user_followers_result import UserFollowersResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserFollowersResult from a JSON string
user_followers_result_instance = UserFollowersResult.from_json(json)
# print the JSON string representation of the object
print(UserFollowersResult.to_json())

# convert the object into a dict
user_followers_result_dict = user_followers_result_instance.to_dict()
# create an instance of UserFollowersResult from a dict
user_followers_result_from_dict = UserFollowersResult.from_dict(user_followers_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


