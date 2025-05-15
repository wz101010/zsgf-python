# TradeFundBill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**bank_code** | **str** |  | [optional] 
**fund_channel** | **str** |  | [optional] 
**fund_type** | **str** |  | [optional] 
**real_amount** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.trade_fund_bill import TradeFundBill

# TODO update the JSON string below
json = "{}"
# create an instance of TradeFundBill from a JSON string
trade_fund_bill_instance = TradeFundBill.from_json(json)
# print the JSON string representation of the object
print(TradeFundBill.to_json())

# convert the object into a dict
trade_fund_bill_dict = trade_fund_bill_instance.to_dict()
# create an instance of TradeFundBill from a dict
trade_fund_bill_from_dict = TradeFundBill.from_dict(trade_fund_bill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


