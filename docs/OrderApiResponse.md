# OrderApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**Order**](Order.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.order_api_response import OrderApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderApiResponse from a JSON string
order_api_response_instance = OrderApiResponse.from_json(json)
# print the JSON string representation of the object
print(OrderApiResponse.to_json())

# convert the object into a dict
order_api_response_dict = order_api_response_instance.to_dict()
# create an instance of OrderApiResponse from a dict
order_api_response_from_dict = OrderApiResponse.from_dict(order_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


