# CommonFriendModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | 用户ID | [optional] 
**nick_name** | **str** | 昵称 | [optional] 
**avatar** | **str** | 头像 | [optional] 

## Example

```python
from ZSGF.Client.models.common_friend_model import CommonFriendModel

# TODO update the JSON string below
json = "{}"
# create an instance of CommonFriendModel from a JSON string
common_friend_model_instance = CommonFriendModel.from_json(json)
# print the JSON string representation of the object
print(CommonFriendModel.to_json())

# convert the object into a dict
common_friend_model_dict = common_friend_model_instance.to_dict()
# create an instance of CommonFriendModel from a dict
common_friend_model_from_dict = CommonFriendModel.from_dict(common_friend_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


