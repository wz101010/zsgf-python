# RefundSubFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_charge_fee** | **str** |  | [optional] 
**switch_fee_rate** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.refund_sub_fee import RefundSubFee

# TODO update the JSON string below
json = "{}"
# create an instance of RefundSubFee from a JSON string
refund_sub_fee_instance = RefundSubFee.from_json(json)
# print the JSON string representation of the object
print(RefundSubFee.to_json())

# convert the object into a dict
refund_sub_fee_dict = refund_sub_fee_instance.to_dict()
# create an instance of RefundSubFee from a dict
refund_sub_fee_from_dict = RefundSubFee.from_dict(refund_sub_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


