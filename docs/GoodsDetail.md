# GoodsDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alipay_goods_id** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**categories_tree** | **str** |  | [optional] 
**goods_category** | **str** |  | [optional] 
**goods_id** | **str** |  | [optional] 
**goods_name** | **str** |  | [optional] 
**out_item_id** | **str** |  | [optional] 
**out_sku_id** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**show_url** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.goods_detail import GoodsDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GoodsDetail from a JSON string
goods_detail_instance = GoodsDetail.from_json(json)
# print the JSON string representation of the object
print(GoodsDetail.to_json())

# convert the object into a dict
goods_detail_dict = goods_detail_instance.to_dict()
# create an instance of GoodsDetail from a dict
goods_detail_from_dict = GoodsDetail.from_dict(goods_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


