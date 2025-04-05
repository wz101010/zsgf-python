# CurrencyListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[Currency]**](Currency.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.currency_list_api_response import CurrencyListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyListApiResponse from a JSON string
currency_list_api_response_instance = CurrencyListApiResponse.from_json(json)
# print the JSON string representation of the object
print(CurrencyListApiResponse.to_json())

# convert the object into a dict
currency_list_api_response_dict = currency_list_api_response_instance.to_dict()
# create an instance of CurrencyListApiResponse from a dict
currency_list_api_response_from_dict = CurrencyListApiResponse.from_dict(currency_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


