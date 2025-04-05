# Settings

公共配置存储实体，用于集中管理系统的配置项。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 配置项的唯一标识符。 | [optional] 
**biz_code** | **str** | 配置项所属的业务代码，用于分类管理。 | [optional] 
**biz_identity** | **str** | 配置项所属的业务标识，用于唯一标识业务。 | [optional] 
**provider_code** | **str** | 配置项的提供者代码，用于标识配置来源。 | [optional] 
**group_code** | **str** | 配置项的分组代码，用于组织和管理相关配置。 | [optional] 
**code** | **str** | 配置项的唯一代码，用于标识具体的配置项。 | [optional] 
**value** | **str** | 配置项的具体值，存储配置内容。 | [optional] 
**tags** | **str** | 用于分类或标记配置项的标签。 | [optional] 
**description** | **str** | 配置项的详细描述，说明其用途和作用。 | [optional] 
**frontend_usable** | **bool** | 指示该配置项是否可供前端使用。 | [optional] 
**create_date** | **datetime** | 配置项的创建日期，默认为当前时间。 | [optional] 
**last_update** | **datetime** | 配置项的最后更新日期，默认为当前时间。 | [optional] 

## Example

```python
from ZSGF.Client.models.settings import Settings

# TODO update the JSON string below
json = "{}"
# create an instance of Settings from a JSON string
settings_instance = Settings.from_json(json)
# print the JSON string representation of the object
print(Settings.to_json())

# convert the object into a dict
settings_dict = settings_instance.to_dict()
# create an instance of Settings from a dict
settings_from_dict = Settings.from_dict(settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


