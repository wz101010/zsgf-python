# FollowerModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**target_user_id** | **int** |  | [optional] 
**alias** | **str** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**is_mutual** | **bool** |  | [optional] 
**closeness_score** | **int** |  | [optional] 
**attention_score** | **int** |  | [optional] 
**tags** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 

## Example

```python
from ZSGF.Client.models.follower_model import FollowerModel

# TODO update the JSON string below
json = "{}"
# create an instance of FollowerModel from a JSON string
follower_model_instance = FollowerModel.from_json(json)
# print the JSON string representation of the object
print(FollowerModel.to_json())

# convert the object into a dict
follower_model_dict = follower_model_instance.to_dict()
# create an instance of FollowerModel from a dict
follower_model_from_dict = FollowerModel.from_dict(follower_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


