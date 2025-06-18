# ReturnPageNotifyRequest

支付宝返回页面通知请求

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | 应用ID | [optional] 
**auth_app_id** | **str** | 授权应用ID | [optional] 
**charset** | **str** | 字符集 | [optional] 
**method** | **str** | 接口名称 | [optional] 
**out_trade_no** | **str** | 商户订单号 | [optional] 
**seller_id** | **str** | 卖家支付宝用户号 | [optional] 
**sign** | **str** | 签名 | [optional] 
**sign_type** | **str** | 签名类型 | [optional] 
**timestamp** | **str** | 时间戳 | [optional] 
**total_amount** | **str** | 订单总金额 | [optional] 
**trade_no** | **str** | 支付宝交易号 | [optional] 
**version** | **str** | 接口版本 | [optional] 

## Example

```python
from ZSGF.Client.models.return_page_notify_request import ReturnPageNotifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPageNotifyRequest from a JSON string
return_page_notify_request_instance = ReturnPageNotifyRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnPageNotifyRequest.to_json())

# convert the object into a dict
return_page_notify_request_dict = return_page_notify_request_instance.to_dict()
# create an instance of ReturnPageNotifyRequest from a dict
return_page_notify_request_from_dict = ReturnPageNotifyRequest.from_dict(return_page_notify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


