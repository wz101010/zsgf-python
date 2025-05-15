# CreateOrderResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**order_no** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.create_order_result import CreateOrderResult

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderResult from a JSON string
create_order_result_instance = CreateOrderResult.from_json(json)
# print the JSON string representation of the object
print(CreateOrderResult.to_json())

# convert the object into a dict
create_order_result_dict = create_order_result_instance.to_dict()
# create an instance of CreateOrderResult from a dict
create_order_result_from_dict = CreateOrderResult.from_dict(create_order_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


