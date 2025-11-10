# HbFqPayInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fq_amount** | **str** |  | [optional] 
**fq_inst_id** | **str** |  | [optional] 
**user_install_num** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.hb_fq_pay_info import HbFqPayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HbFqPayInfo from a JSON string
hb_fq_pay_info_instance = HbFqPayInfo.from_json(json)
# print the JSON string representation of the object
print(HbFqPayInfo.to_json())

# convert the object into a dict
hb_fq_pay_info_dict = hb_fq_pay_info_instance.to_dict()
# create an instance of HbFqPayInfo from a dict
hb_fq_pay_info_from_dict = HbFqPayInfo.from_dict(hb_fq_pay_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


