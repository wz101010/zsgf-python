# AlipayTradeRefundResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**msg** | **str** |  | [optional] 
**sub_code** | **str** |  | [optional] 
**sub_msg** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**is_error** | **bool** |  | [optional] [readonly] 
**buyer_logon_id** | **str** |  | [optional] 
**buyer_open_id** | **str** |  | [optional] 
**buyer_user_id** | **str** |  | [optional] 
**fund_change** | **str** |  | [optional] 
**gmt_refund_pay** | **str** |  | [optional] 
**has_deposit_back** | **str** |  | [optional] 
**open_id** | **str** |  | [optional] 
**out_trade_no** | **str** |  | [optional] 
**pre_auth_cancel_fee** | **str** |  | [optional] 
**present_refund_buyer_amount** | **str** |  | [optional] 
**present_refund_discount_amount** | **str** |  | [optional] 
**present_refund_mdiscount_amount** | **str** |  | [optional] 
**refund_charge_amount** | **str** |  | [optional] 
**refund_charge_info_list** | [**List[RefundChargeInfo]**](RefundChargeInfo.md) |  | [optional] 
**refund_currency** | **str** |  | [optional] 
**refund_detail_item_list** | [**List[TradeFundBill]**](TradeFundBill.md) |  | [optional] 
**refund_fee** | **str** |  | [optional] 
**refund_hyb_amount** | **str** |  | [optional] 
**refund_preset_paytool_list** | [**PresetPayToolInfo**](PresetPayToolInfo.md) |  | [optional] 
**refund_settlement_id** | **str** |  | [optional] 
**refund_voucher_detail_list** | [**List[VoucherDetail]**](VoucherDetail.md) |  | [optional] 
**send_back_fee** | **str** |  | [optional] 
**store_name** | **str** |  | [optional] 
**trade_no** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.alipay_trade_refund_response import AlipayTradeRefundResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlipayTradeRefundResponse from a JSON string
alipay_trade_refund_response_instance = AlipayTradeRefundResponse.from_json(json)
# print the JSON string representation of the object
print(AlipayTradeRefundResponse.to_json())

# convert the object into a dict
alipay_trade_refund_response_dict = alipay_trade_refund_response_instance.to_dict()
# create an instance of AlipayTradeRefundResponse from a dict
alipay_trade_refund_response_from_dict = AlipayTradeRefundResponse.from_dict(alipay_trade_refund_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


