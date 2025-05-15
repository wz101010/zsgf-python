# ServiceProvider

服务商实体，用于表示和管理系统中的服务提供方信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 服务商的唯一标识符。 | [optional] 
**biz_code** | **str** | 服务商的业务代码，用于标识其所属业务领域。 | [optional] 
**name** | **str** | 服务商的名称。 | [optional] 
**code** | **str** | 服务商的唯一代码，用于系统内部标识。 | [optional] 
**icon** | **str** | 服务商图标的URL或路径。 | [optional] 
**description** | **str** | 服务商的详细描述信息。 | [optional] 
**tags** | **str** | 用于分类或标记服务商的标签。 | [optional] 
**show** | **bool** | 指示服务商是否在界面上显示。 | [optional] 
**show_index** | **int** | 服务商在界面上的显示顺序。 | [optional] 
**create_date** | **datetime** | 服务商记录的创建日期，默认为当前时间。 | [optional] 
**last_update** | **datetime** | 服务商记录的最后更新日期，默认为当前时间。 | [optional] 

## Example

```python
from ZSGF.Client.models.service_provider import ServiceProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProvider from a JSON string
service_provider_instance = ServiceProvider.from_json(json)
# print the JSON string representation of the object
print(ServiceProvider.to_json())

# convert the object into a dict
service_provider_dict = service_provider_instance.to_dict()
# create an instance of ServiceProvider from a dict
service_provider_from_dict = ServiceProvider.from_dict(service_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


