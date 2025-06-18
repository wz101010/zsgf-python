# UserFriendsNearByResult

附近用户推荐结果

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | 符合条件的总记录数 | [optional] 
**data** | [**List[RecommendFriend]**](RecommendFriend.md) | 当前分页的用户数据列表 | [optional] 

## Example

```python
from ZSGF.Client.models.user_friends_near_by_result import UserFriendsNearByResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserFriendsNearByResult from a JSON string
user_friends_near_by_result_instance = UserFriendsNearByResult.from_json(json)
# print the JSON string representation of the object
print(UserFriendsNearByResult.to_json())

# convert the object into a dict
user_friends_near_by_result_dict = user_friends_near_by_result_instance.to_dict()
# create an instance of UserFriendsNearByResult from a dict
user_friends_near_by_result_from_dict = UserFriendsNearByResult.from_dict(user_friends_near_by_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


