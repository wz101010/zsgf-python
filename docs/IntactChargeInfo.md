# IntactChargeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_amount** | **str** |  | [optional] 
**bill_type** | **str** |  | [optional] 
**gmt_pay** | **str** |  | [optional] 
**is_refund** | **bool** |  | [optional] 
**out_biz_no** | **str** |  | [optional] 
**plan_amount** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**service_target** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**target_account_no** | **str** |  | [optional] 
**target_user_id** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.intact_charge_info import IntactChargeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IntactChargeInfo from a JSON string
intact_charge_info_instance = IntactChargeInfo.from_json(json)
# print the JSON string representation of the object
print(IntactChargeInfo.to_json())

# convert the object into a dict
intact_charge_info_dict = intact_charge_info_instance.to_dict()
# create an instance of IntactChargeInfo from a dict
intact_charge_info_from_dict = IntactChargeInfo.from_dict(intact_charge_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


