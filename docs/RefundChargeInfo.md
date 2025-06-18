# RefundChargeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_type** | **str** |  | [optional] 
**refund_charge_fee** | **str** |  | [optional] 
**refund_sub_fee_detail_list** | [**List[RefundSubFee]**](RefundSubFee.md) |  | [optional] 
**switch_fee_rate** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.refund_charge_info import RefundChargeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RefundChargeInfo from a JSON string
refund_charge_info_instance = RefundChargeInfo.from_json(json)
# print the JSON string representation of the object
print(RefundChargeInfo.to_json())

# convert the object into a dict
refund_charge_info_dict = refund_charge_info_instance.to_dict()
# create an instance of RefundChargeInfo from a dict
refund_charge_info_from_dict = RefundChargeInfo.from_dict(refund_charge_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


