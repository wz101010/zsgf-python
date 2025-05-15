# App

应用

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 唯一标识符 | [optional] 
**user_id** | **int** | 用户 ID | [optional] 
**project_id** | **int** | 项目 ID | [optional] 
**website** | **str** | 网站默认域名 | [optional] 
**name** | **str** | 名称 | [optional] 
**logo** | **str** | Logo | [optional] 
**description** | **str** | 描述 | [optional] 
**tags** | **str** | 标签 | [optional] 
**app_key** | **str** | 应用公钥 | [optional] 
**app_secret** | **str** | 应用私密密钥 | [optional] 
**client_secret** | **str** | 客户端密钥 | [optional] 
**ssh_publickey** | **str** | SSH公钥 | [optional] 
**share** | **bool** | 是否共享 | [optional] 
**create_date** | **datetime** | 创建时间 | [optional] 
**last_update** | **datetime** | 最后更新时间 | [optional] 
**show** | **bool** | 是否显示 | [optional] 
**show_index** | **int** | 显示索引 | [optional] 

## Example

```python
from ZSGF.Client.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print(App.to_json())

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_from_dict = App.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


