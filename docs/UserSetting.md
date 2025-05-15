# UserSetting

用户配置实体，用于存储用户的个性化设置。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 用户的唯一标识符。 | [optional] 
**user_id** | **int** | 关联的用户ID，表示该配置属于哪个用户。 | 
**provider_code** | **str** | 提供商的唯一代码，用于标识服务提供者。 | [optional] 
**group_code** | **str** | 组的唯一代码，用于分类设置项。 | [optional] 
**code** | **str** | 设置项的唯一代码或键名，用于标识具体的配置项。 | 
**value** | **str** | 设置项的具体值或选项。 | 
**tags** | **str** | 用于对设置项进行分类或标记的标签。 | [optional] 
**description** | **str** | 设置项的详细描述，说明其作用或用途。 | [optional] 
**frontend_usable** | **bool** | 指示该设置项是否在前端界面中可用。 | [optional] 
**create_date** | **datetime** | 设置项的创建时间。 | [optional] 
**last_update** | **datetime** | 设置项的最后更新时间。 | [optional] 

## Example

```python
from ZSGF.Client.models.user_setting import UserSetting

# TODO update the JSON string below
json = "{}"
# create an instance of UserSetting from a JSON string
user_setting_instance = UserSetting.from_json(json)
# print the JSON string representation of the object
print(UserSetting.to_json())

# convert the object into a dict
user_setting_dict = user_setting_instance.to_dict()
# create an instance of UserSetting from a dict
user_setting_from_dict = UserSetting.from_dict(user_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


