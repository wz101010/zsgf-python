# CurrencyApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**Currency**](Currency.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.currency_api_response import CurrencyApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyApiResponse from a JSON string
currency_api_response_instance = CurrencyApiResponse.from_json(json)
# print the JSON string representation of the object
print(CurrencyApiResponse.to_json())

# convert the object into a dict
currency_api_response_dict = currency_api_response_instance.to_dict()
# create an instance of CurrencyApiResponse from a dict
currency_api_response_from_dict = CurrencyApiResponse.from_dict(currency_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


