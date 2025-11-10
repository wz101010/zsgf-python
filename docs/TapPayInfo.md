# TapPayInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_medium_type** | **str** |  | [optional] 
**total_discount_amount** | **str** |  | [optional] 
**total_discount_name** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.tap_pay_info import TapPayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TapPayInfo from a JSON string
tap_pay_info_instance = TapPayInfo.from_json(json)
# print the JSON string representation of the object
print(TapPayInfo.to_json())

# convert the object into a dict
tap_pay_info_dict = tap_pay_info_instance.to_dict()
# create an instance of TapPayInfo from a dict
tap_pay_info_from_dict = TapPayInfo.from_dict(tap_pay_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


