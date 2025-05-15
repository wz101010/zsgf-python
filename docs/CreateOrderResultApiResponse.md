# CreateOrderResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**CreateOrderResult**](CreateOrderResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.create_order_result_api_response import CreateOrderResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderResultApiResponse from a JSON string
create_order_result_api_response_instance = CreateOrderResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrderResultApiResponse.to_json())

# convert the object into a dict
create_order_result_api_response_dict = create_order_result_api_response_instance.to_dict()
# create an instance of CreateOrderResultApiResponse from a dict
create_order_result_api_response_from_dict = CreateOrderResultApiResponse.from_dict(create_order_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


