# GeoLocation

地理位置

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 唯一标识 | [optional] 
**biz_code** | **str** | 业务代码 | 
**biz_id** | **int** | 业务ID | 
**coordinates** | [**MySqlGeometry**](MySqlGeometry.md) |  | 
**location_name** | **str** | 地点的名称 | [optional] 
**location_type** | **str** | 地点类型 | [optional] 
**recipient_name** | **str** | 收货人姓名 | [optional] 
**phone_number** | **str** | 收货人联系电话 | [optional] 
**email** | **str** | 收货人电子邮件 | [optional] 
**country** | **str** | 国家 | [optional] 
**state** | **str** | 州/省 | [optional] 
**city** | **str** | 城市 | [optional] 
**district** | **str** | 区/县 | [optional] 
**street** | **str** | 街道 | [optional] 
**zip_code** | **str** | 邮政编码 | [optional] 
**address** | **str** | 详细的地址信息 | [optional] 
**map_type** | **str** | 地址类型 | [optional] 
**remark** | **str** | 备注 | [optional] 
**tags** | **str** | 标签 | [optional] 
**enable** | **bool** | 是否启用 | [optional] 
**show_index** | **int** | 排序索引 | [optional] 
**create_date** | **datetime** | 创建时间 | [optional] 
**last_update** | **datetime** | 最后更新时间 | [optional] 

## Example

```python
from ZSGF.Client.models.geo_location import GeoLocation

# TODO update the JSON string below
json = "{}"
# create an instance of GeoLocation from a JSON string
geo_location_instance = GeoLocation.from_json(json)
# print the JSON string representation of the object
print(GeoLocation.to_json())

# convert the object into a dict
geo_location_dict = geo_location_instance.to_dict()
# create an instance of GeoLocation from a dict
geo_location_from_dict = GeoLocation.from_dict(geo_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


