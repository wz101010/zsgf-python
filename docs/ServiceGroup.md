# ServiceGroup

服务功能分组实体，用于对服务功能进行分类和管理。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 服务功能分组的唯一标识符。 | [optional] 
**provider_id** | **int** | 关联的服务商的唯一标识符。 | [optional] 
**name** | **str** | 服务功能分组的名称。 | [optional] 
**code** | **str** | 服务功能分组的唯一代码，用于系统内部标识。 | [optional] 
**icon** | **str** | 服务功能分组的图标URL或路径。 | [optional] 
**description** | **str** | 服务功能分组的详细描述信息。 | [optional] 
**show** | **bool** | 指示服务功能分组是否在界面上显示。 | [optional] 
**show_index** | **int** | 服务功能分组在界面上的显示顺序。 | [optional] 
**create_date** | **datetime** | 服务功能分组的创建日期，默认为当前时间。 | [optional] 
**last_update** | **datetime** | 服务功能分组的最后更新日期，默认为当前时间。 | [optional] 

## Example

```python
from ZSGF.Client.models.service_group import ServiceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceGroup from a JSON string
service_group_instance = ServiceGroup.from_json(json)
# print the JSON string representation of the object
print(ServiceGroup.to_json())

# convert the object into a dict
service_group_dict = service_group_instance.to_dict()
# create an instance of ServiceGroup from a dict
service_group_from_dict = ServiceGroup.from_dict(service_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


