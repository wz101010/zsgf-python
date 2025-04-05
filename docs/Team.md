# Team

团队

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**user_id** | **int** | 用户ID | [optional] 
**channel_code** | **str** | 渠道代码 | [optional] 
**channel_app_id** | **str** | 渠道应用ID | [optional] 
**role** | **str** | 角色 | [optional] 
**permission** | **str** | 权限 | [optional] 
**show** | **bool** | 是否显示 | [optional] 
**show_index** | **int** | 显示顺序 | [optional] 
**create_date** | **datetime** | 创建日期 | [optional] 
**last_update** | **datetime** | 最后更新日期 | [optional] 

## Example

```python
from ZSGF.Client.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


