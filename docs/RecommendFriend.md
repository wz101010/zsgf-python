# RecommendFriend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**age** | **int** |  | [optional] 
**interest_tags** | **str** |  | [optional] 
**location_name** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**distance** | **int** |  | [optional] 

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


