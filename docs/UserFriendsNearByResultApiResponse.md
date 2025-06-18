# UserFriendsNearByResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**UserFriendsNearByResult**](UserFriendsNearByResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.user_friends_near_by_result_api_response import UserFriendsNearByResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserFriendsNearByResultApiResponse from a JSON string
user_friends_near_by_result_api_response_instance = UserFriendsNearByResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(UserFriendsNearByResultApiResponse.to_json())

# convert the object into a dict
user_friends_near_by_result_api_response_dict = user_friends_near_by_result_api_response_instance.to_dict()
# create an instance of UserFriendsNearByResultApiResponse from a dict
user_friends_near_by_result_api_response_from_dict = UserFriendsNearByResultApiResponse.from_dict(user_friends_near_by_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


