# CurrencyExchangeRate

货币兑换比率实体，用于表示不同货币之间的兑换关系。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 货币兑换比率的唯一标识符。 | [optional] 
**from_currency_code** | **str** | 兑换的源货币代码，例如 &#39;USD&#39;。 | [optional] 
**to_currency_code** | **str** | 兑换的目标货币代码，例如 &#39;CNY&#39;。 | [optional] 
**exchange_rate** | **int** | 从源货币到目标货币的兑换比率。例如，1 USD &#x3D; 6.5 CNY。 | [optional] 
**description** | **str** | 兑换比率的详细描述信息。 | [optional] 
**create_date** | **datetime** | 货币兑换比率的创建日期，默认为当前时间。 | [optional] 
**last_update** | **datetime** | 货币兑换比率的最后更新日期，默认为当前时间。 | [optional] 

## Example

```python
from ZSGF.Client.models.currency_exchange_rate import CurrencyExchangeRate

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyExchangeRate from a JSON string
currency_exchange_rate_instance = CurrencyExchangeRate.from_json(json)
# print the JSON string representation of the object
print(CurrencyExchangeRate.to_json())

# convert the object into a dict
currency_exchange_rate_dict = currency_exchange_rate_instance.to_dict()
# create an instance of CurrencyExchangeRate from a dict
currency_exchange_rate_from_dict = CurrencyExchangeRate.from_dict(currency_exchange_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


