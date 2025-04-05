# EnterprisePayInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biz_info** | **str** |  | [optional] 
**invoice_amount** | **str** |  | [optional] 
**is_use_enterprise_pay** | **bool** |  | [optional] 

## Example

```python
from ZSGF.Client.models.enterprise_pay_info import EnterprisePayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EnterprisePayInfo from a JSON string
enterprise_pay_info_instance = EnterprisePayInfo.from_json(json)
# print the JSON string representation of the object
print(EnterprisePayInfo.to_json())

# convert the object into a dict
enterprise_pay_info_dict = enterprise_pay_info_instance.to_dict()
# create an instance of EnterprisePayInfo from a dict
enterprise_pay_info_from_dict = EnterprisePayInfo.from_dict(enterprise_pay_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


