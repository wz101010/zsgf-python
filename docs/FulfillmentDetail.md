# FulfillmentDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_amount** | **str** |  | [optional] 
**gmt_payment** | **str** |  | [optional] 
**out_request_no** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.fulfillment_detail import FulfillmentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillmentDetail from a JSON string
fulfillment_detail_instance = FulfillmentDetail.from_json(json)
# print the JSON string representation of the object
print(FulfillmentDetail.to_json())

# convert the object into a dict
fulfillment_detail_dict = fulfillment_detail_instance.to_dict()
# create an instance of FulfillmentDetail from a dict
fulfillment_detail_from_dict = FulfillmentDetail.from_dict(fulfillment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


