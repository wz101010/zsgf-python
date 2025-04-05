# AlipayTradeQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**msg** | **str** |  | [optional] 
**sub_code** | **str** |  | [optional] 
**sub_msg** | **str** |  | [optional] 
**is_error** | **bool** |  | [optional] [readonly] 
**additional_status** | **str** |  | [optional] 
**alipay_store_id** | **str** |  | [optional] 
**alipay_sub_merchant_id** | **str** |  | [optional] 
**async_pay_apply_status** | **str** |  | [optional] 
**auth_trade_pay_mode** | **str** |  | [optional] 
**biz_settle_mode** | **str** |  | [optional] 
**bkagent_resp_info** | [**BkAgentRespInfo**](BkAgentRespInfo.md) |  | [optional] 
**body** | **str** |  | [optional] 
**buyer_logon_id** | **str** |  | [optional] 
**buyer_open_id** | **str** |  | [optional] 
**buyer_pay_amount** | **str** |  | [optional] 
**buyer_user_id** | **str** |  | [optional] 
**buyer_user_name** | **str** |  | [optional] 
**buyer_user_type** | **str** |  | [optional] 
**cashier_type** | **str** |  | [optional] 
**charge_amount** | **str** |  | [optional] 
**charge_flags** | **str** |  | [optional] 
**charge_info_list** | [**List[ChargeInfo]**](ChargeInfo.md) |  | [optional] 
**credit_biz_order_id** | **str** |  | [optional] 
**credit_pay_mode** | **str** |  | [optional] 
**discount_amount** | **str** |  | [optional] 
**discount_goods_detail** | **str** |  | [optional] 
**enterprise_pay_info** | [**EnterprisePayInfo**](EnterprisePayInfo.md) |  | [optional] 
**ext_infos** | **str** |  | [optional] 
**fulfillment_detail_list** | [**List[FulfillmentDetail]**](FulfillmentDetail.md) |  | [optional] 
**fund_bill_list** | [**List[TradeFundBill]**](TradeFundBill.md) |  | [optional] 
**hb_fq_pay_info** | [**HbFqPayInfo**](HbFqPayInfo.md) |  | [optional] 
**hyb_amount** | **str** |  | [optional] 
**industry_sepc_detail** | **str** |  | [optional] 
**industry_sepc_detail_acc** | **str** |  | [optional] 
**industry_sepc_detail_gov** | **str** |  | [optional] 
**intact_charge_info_list** | [**List[IntactChargeInfo]**](IntactChargeInfo.md) |  | [optional] 
**invoice_amount** | **str** |  | [optional] 
**mdiscount_amount** | **str** |  | [optional] 
**medical_insurance_info** | **str** |  | [optional] 
**open_id** | **str** |  | [optional] 
**out_trade_no** | **str** |  | [optional] 
**passback_params** | **str** |  | [optional] 
**pay_amount** | **str** |  | [optional] 
**pay_currency** | **str** |  | [optional] 
**payment_info_with_id_list** | [**List[PaymentInfoWithId]**](PaymentInfoWithId.md) |  | [optional] 
**period_scene** | **str** |  | [optional] 
**point_amount** | **str** |  | [optional] 
**pre_auth_pay_amount** | **str** |  | [optional] 
**receipt_amount** | **str** |  | [optional] 
**receipt_currency_type** | **str** |  | [optional] 
**req_goods_detail** | [**List[GoodsDetail]**](GoodsDetail.md) |  | [optional] 
**send_pay_date** | **str** |  | [optional] 
**settle_amount** | **str** |  | [optional] 
**settle_currency** | **str** |  | [optional] 
**settle_trans_rate** | **str** |  | [optional] 
**settlement_id** | **str** |  | [optional] 
**store_id** | **str** |  | [optional] 
**store_name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**tap_pay_info** | [**TapPayInfo**](TapPayInfo.md) |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**total_amount** | **str** |  | [optional] 
**trade_no** | **str** |  | [optional] 
**trade_settle_info** | [**TradeSettleInfo**](TradeSettleInfo.md) |  | [optional] 
**trade_status** | **str** |  | [optional] 
**trans_currency** | **str** |  | [optional] 
**trans_pay_rate** | **str** |  | [optional] 
**voucher_detail_list** | [**List[VoucherDetail]**](VoucherDetail.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.alipay_trade_query_response import AlipayTradeQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlipayTradeQueryResponse from a JSON string
alipay_trade_query_response_instance = AlipayTradeQueryResponse.from_json(json)
# print the JSON string representation of the object
print(AlipayTradeQueryResponse.to_json())

# convert the object into a dict
alipay_trade_query_response_dict = alipay_trade_query_response_instance.to_dict()
# create an instance of AlipayTradeQueryResponse from a dict
alipay_trade_query_response_from_dict = AlipayTradeQueryResponse.from_dict(alipay_trade_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


