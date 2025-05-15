# TradeSettleDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**operation_dt** | **str** |  | [optional] 
**operation_serial_no** | **str** |  | [optional] 
**operation_type** | **str** |  | [optional] 
**ori_trans_in** | **str** |  | [optional] 
**ori_trans_out** | **str** |  | [optional] 
**trans_in** | **str** |  | [optional] 
**trans_out** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.trade_settle_detail import TradeSettleDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TradeSettleDetail from a JSON string
trade_settle_detail_instance = TradeSettleDetail.from_json(json)
# print the JSON string representation of the object
print(TradeSettleDetail.to_json())

# convert the object into a dict
trade_settle_detail_dict = trade_settle_detail_instance.to_dict()
# create an instance of TradeSettleDetail from a dict
trade_settle_detail_from_dict = TradeSettleDetail.from_dict(trade_settle_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


