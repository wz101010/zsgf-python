# ServiceItem

服务配置项实体，用于定义和管理服务相关的配置信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 服务配置项的唯一标识符。 | [optional] 
**biz_code** | **str** | 服务配置项所属的业务代码，用于分类管理。 | [optional] 
**provider_code** | **str** | 关联的服务商代码，用于标识提供该配置项的服务商。 | [optional] 
**group_code** | **str** | 服务配置项所属的功能分组代码，用于组织和管理相关配置项。 | [optional] 
**name** | **str** | 服务配置项的名称，用于描述其功能或用途。 | [optional] 
**code** | **str** | 服务配置项的唯一代码，用于系统内部标识。 | [optional] 
**value_type** | **str** | 服务配置项的值类型，例如 &#39;text&#39;, &#39;number&#39;, &#39;boolean&#39; 等。默认为 &#39;text&#39;。 | [optional] 
**icon** | **str** | 服务配置项的图标URL或路径，用于在界面上显示。 | [optional] 
**value_defaults** | **str** | 服务配置项的默认值，当未设置具体值时使用。 | [optional] 
**description** | **str** | 服务配置项的详细描述信息，用于说明其用途和配置方法。 | [optional] 
**tags** | **str** | 用于分类或标记服务配置项的标签。 | [optional] 
**is_system** | **bool** | 指示该配置项是否为系统级别的配置项，默认为 false。 | [optional] 
**show** | **bool** | 指示服务配置项是否在界面上显示，默认为 true。 | [optional] 
**show_index** | **int** | 服务配置项在界面上的显示顺序。 | [optional] 
**create_date** | **datetime** | 服务配置项的创建日期，默认为当前时间。 | [optional] 
**last_update** | **datetime** | 服务配置项的最后更新日期，默认为当前时间。 | [optional] 

## Example

```python
from ZSGF.Client.models.service_item import ServiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceItem from a JSON string
service_item_instance = ServiceItem.from_json(json)
# print the JSON string representation of the object
print(ServiceItem.to_json())

# convert the object into a dict
service_item_dict = service_item_instance.to_dict()
# create an instance of ServiceItem from a dict
service_item_from_dict = ServiceItem.from_dict(service_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


