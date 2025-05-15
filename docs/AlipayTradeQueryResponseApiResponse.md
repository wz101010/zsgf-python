# AlipayTradeQueryResponseApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**AlipayTradeQueryResponse**](AlipayTradeQueryResponse.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.alipay_trade_query_response_api_response import AlipayTradeQueryResponseApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlipayTradeQueryResponseApiResponse from a JSON string
alipay_trade_query_response_api_response_instance = AlipayTradeQueryResponseApiResponse.from_json(json)
# print the JSON string representation of the object
print(AlipayTradeQueryResponseApiResponse.to_json())

# convert the object into a dict
alipay_trade_query_response_api_response_dict = alipay_trade_query_response_api_response_instance.to_dict()
# create an instance of AlipayTradeQueryResponseApiResponse from a dict
alipay_trade_query_response_api_response_from_dict = AlipayTradeQueryResponseApiResponse.from_dict(alipay_trade_query_response_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


