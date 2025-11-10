# VoucherDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**memo** | **str** |  | [optional] 
**merchant_contribute** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**other_contribute** | **str** |  | [optional] 
**other_contribute_detail** | [**List[ContributeDetail]**](ContributeDetail.md) |  | [optional] 
**purchase_ant_contribute** | **str** |  | [optional] 
**purchase_buyer_contribute** | **str** |  | [optional] 
**purchase_merchant_contribute** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.voucher_detail import VoucherDetail

# TODO update the JSON string below
json = "{}"
# create an instance of VoucherDetail from a JSON string
voucher_detail_instance = VoucherDetail.from_json(json)
# print the JSON string representation of the object
print(VoucherDetail.to_json())

# convert the object into a dict
voucher_detail_dict = voucher_detail_instance.to_dict()
# create an instance of VoucherDetail from a dict
voucher_detail_from_dict = VoucherDetail.from_dict(voucher_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


