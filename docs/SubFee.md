# SubFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_fee** | **str** |  | [optional] 
**original_charge_fee** | **str** |  | [optional] 
**switch_fee_rate** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.sub_fee import SubFee

# TODO update the JSON string below
json = "{}"
# create an instance of SubFee from a JSON string
sub_fee_instance = SubFee.from_json(json)
# print the JSON string representation of the object
print(SubFee.to_json())

# convert the object into a dict
sub_fee_dict = sub_fee_instance.to_dict()
# create an instance of SubFee from a dict
sub_fee_from_dict = SubFee.from_dict(sub_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


