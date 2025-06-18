# AlipayTradeRefundResponseApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**AlipayTradeRefundResponse**](AlipayTradeRefundResponse.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.alipay_trade_refund_response_api_response import AlipayTradeRefundResponseApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlipayTradeRefundResponseApiResponse from a JSON string
alipay_trade_refund_response_api_response_instance = AlipayTradeRefundResponseApiResponse.from_json(json)
# print the JSON string representation of the object
print(AlipayTradeRefundResponseApiResponse.to_json())

# convert the object into a dict
alipay_trade_refund_response_api_response_dict = alipay_trade_refund_response_api_response_instance.to_dict()
# create an instance of AlipayTradeRefundResponseApiResponse from a dict
alipay_trade_refund_response_api_response_from_dict = AlipayTradeRefundResponseApiResponse.from_dict(alipay_trade_refund_response_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


