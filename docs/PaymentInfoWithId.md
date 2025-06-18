# PaymentInfoWithId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_ids** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.payment_info_with_id import PaymentInfoWithId

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInfoWithId from a JSON string
payment_info_with_id_instance = PaymentInfoWithId.from_json(json)
# print the JSON string representation of the object
print(PaymentInfoWithId.to_json())

# convert the object into a dict
payment_info_with_id_dict = payment_info_with_id_instance.to_dict()
# create an instance of PaymentInfoWithId from a dict
payment_info_with_id_from_dict = PaymentInfoWithId.from_dict(payment_info_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


