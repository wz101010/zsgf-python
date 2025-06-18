# RecommendFriend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | 用户ID | [optional] 
**nick_name** | **str** | 昵称 | [optional] 
**avatar** | **str** | 头像 | [optional] 
**gender** | **str** | 性别 | [optional] 
**age** | **int** | 年龄 | [optional] 
**interest_tags** | **str** | 兴趣标签 | [optional] 
**location_name** | **str** | 位置名称 | [optional] 
**latitude** | **float** | 纬度 | [optional] 
**longitude** | **float** | 经度 | [optional] 
**distance** | **int** | 距离 | [optional] 
**biography** | **str** | 个人简介 | [optional] 
**country** | **str** | 国家 | [optional] 
**state** | **str** | 省份 | [optional] 
**city** | **str** | 城市 | [optional] 
**district** | **str** | 区县 | [optional] 

## Example

```python
from ZSGF.Client.models.recommend_friend import RecommendFriend

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendFriend from a JSON string
recommend_friend_instance = RecommendFriend.from_json(json)
# print the JSON string representation of the object
print(RecommendFriend.to_json())

# convert the object into a dict
recommend_friend_dict = recommend_friend_instance.to_dict()
# create an instance of RecommendFriend from a dict
recommend_friend_from_dict = RecommendFriend.from_dict(recommend_friend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


