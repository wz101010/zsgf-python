# OrderListResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**OrderListResult**](OrderListResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.order_list_result_api_response import OrderListResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderListResultApiResponse from a JSON string
order_list_result_api_response_instance = OrderListResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(OrderListResultApiResponse.to_json())

# convert the object into a dict
order_list_result_api_response_dict = order_list_result_api_response_instance.to_dict()
# create an instance of OrderListResultApiResponse from a dict
order_list_result_api_response_from_dict = OrderListResultApiResponse.from_dict(order_list_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


