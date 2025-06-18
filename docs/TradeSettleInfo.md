# TradeSettleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_settle_detail_list** | [**List[TradeSettleDetail]**](TradeSettleDetail.md) |  | [optional] 
**trade_unsettled_amount** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.trade_settle_info import TradeSettleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TradeSettleInfo from a JSON string
trade_settle_info_instance = TradeSettleInfo.from_json(json)
# print the JSON string representation of the object
print(TradeSettleInfo.to_json())

# convert the object into a dict
trade_settle_info_dict = trade_settle_info_instance.to_dict()
# create an instance of TradeSettleInfo from a dict
trade_settle_info_from_dict = TradeSettleInfo.from_dict(trade_settle_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


