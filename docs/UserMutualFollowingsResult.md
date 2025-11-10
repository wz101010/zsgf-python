# UserMutualFollowingsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_followers** | **int** |  | [optional] 
**data** | [**List[CommonFriendModel]**](CommonFriendModel.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.user_mutual_followings_result import UserMutualFollowingsResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserMutualFollowingsResult from a JSON string
user_mutual_followings_result_instance = UserMutualFollowingsResult.from_json(json)
# print the JSON string representation of the object
print(UserMutualFollowingsResult.to_json())

# convert the object into a dict
user_mutual_followings_result_dict = user_mutual_followings_result_instance.to_dict()
# create an instance of UserMutualFollowingsResult from a dict
user_mutual_followings_result_from_dict = UserMutualFollowingsResult.from_dict(user_mutual_followings_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


