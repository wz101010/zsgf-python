# FollowerModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 用户ID | [optional] 
**target_user_id** | **int** | 目标用户ID | [optional] 
**alias** | **str** | 别名 | [optional] 
**nick_name** | **str** | 昵称 | [optional] 
**avatar** | **str** | 头像 | [optional] 
**is_mutual** | **bool** | 是否互相关注 | [optional] 
**closeness_score** | **int** | 亲密度分数 | [optional] 
**attention_score** | **int** | 关注度分数 | [optional] 
**tags** | **str** | 标签 | [optional] 
**status** | **str** | 状态 | [optional] 
**remark** | **str** | 备注 | [optional] 
**create_date** | **datetime** | 创建日期 | [optional] 

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


