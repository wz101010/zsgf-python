# AppSetting

应用设置

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 唯一标识 | [optional] 
**provider_code** | **str** | 提供商代码 | [optional] 
**group_code** | **str** | 分组代码 | [optional] 
**code** | **str** | 设置项代码 | 
**value** | **str** | 设置值 | 
**tags** | **str** | 标签 | [optional] 
**description** | **str** | 描述 | [optional] 
**frontend_usable** | **bool** | 是否在前端可用 | [optional] 
**create_date** | **datetime** | 创建时间 | [optional] 
**last_update** | **datetime** | 最后更新时间 | [optional] 

## Example

```python
from ZSGF.Client.models.app_setting import AppSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AppSetting from a JSON string
app_setting_instance = AppSetting.from_json(json)
# print the JSON string representation of the object
print(AppSetting.to_json())

# convert the object into a dict
app_setting_dict = app_setting_instance.to_dict()
# create an instance of AppSetting from a dict
app_setting_from_dict = AppSetting.from_dict(app_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


