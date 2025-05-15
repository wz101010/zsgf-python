# Order

订单实体，用于记录用户的订单信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 订单的唯一标识符。 | [optional] 
**user_id** | **int** | 创建订单的用户ID。 | [optional] 
**pay_type** | **str** | 订单的支付类型，例如 &#39;信用卡&#39;, &#39;支付宝&#39;, &#39;微信支付&#39; 等。 | [optional] 
**amount** | **float** | 订单的总金额。 | [optional] 
**order_no** | **str** | 订单的唯一编号，通常由系统生成。 | [optional] 
**trade_no** | **str** | 与订单关联的交易编号，通常由支付平台提供。 | [optional] 
**status** | **str** | 订单的当前状态，例如 &#39;待支付&#39;, &#39;已完成&#39;, &#39;已取消&#39; 等。 | [optional] 
**product_type** | **str** | 订单中商品的类型分类。 | [optional] 
**product_id** | **str** | 订单中商品的唯一标识符。 | [optional] 
**product_name** | **str** | 订单中商品的名称。 | [optional] 
**allow_refund** | **bool** | 指示订单是否允许进行退款操作。 | [optional] 
**allow_refund_until** | **datetime** | 订单允许进行退款操作的截止时间。 | [optional] 
**tags** | **str** | 用于分类或标记订单的标签。 | [optional] 
**remark** | **str** | 订单的额外备注信息。 | [optional] 
**description** | **str** | 订单的详细描述信息。 | [optional] 
**order_pay_time** | **datetime** | 订单完成支付的时间。 | [optional] 
**expire_time** | **datetime** | 订单的过期时间，超过该时间订单将自动取消。 | [optional] 
**create_date** | **datetime** | 订单的创建时间，默认为当前时间。 | [optional] 
**last_update** | **datetime** | 订单的最后更新时间，默认为当前时间。 | [optional] 

## Example

```python
from ZSGF.Client.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


