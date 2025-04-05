# Project

项目

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 状态码 | [optional] 
**user_id** | **int** | 用户 ID | [optional] 
**name** | **str** | 名称 | [optional] 
**logo** | **str** | Logo | [optional] 
**description** | **str** | 描述 | [optional] 
**show** | **bool** | 是否显示 | [optional] 
**show_index** | **int** | 显示索引 | [optional] 
**create_date** | **datetime** | 创建时间 | [optional] 
**last_update** | **datetime** | 最后更新时间 | [optional] 

## Example

```python
from ZSGF.Client.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


