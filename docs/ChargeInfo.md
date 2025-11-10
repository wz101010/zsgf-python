# ChargeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_fee** | **str** |  | [optional] 
**charge_type** | **str** |  | [optional] 
**is_rating_on_switch** | **str** |  | [optional] 
**is_rating_on_trade_receiver** | **str** |  | [optional] 
**original_charge_fee** | **str** |  | [optional] 
**sub_fee_detail_list** | [**List[SubFee]**](SubFee.md) |  | [optional] 
**switch_fee_rate** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.charge_info import ChargeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeInfo from a JSON string
charge_info_instance = ChargeInfo.from_json(json)
# print the JSON string representation of the object
print(ChargeInfo.to_json())

# convert the object into a dict
charge_info_dict = charge_info_instance.to_dict()
# create an instance of ChargeInfo from a dict
charge_info_from_dict = ChargeInfo.from_dict(charge_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


