# Currency

货币实体，用于表示和管理不同类型的货币信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 货币的唯一标识符。 | [optional] 
**name** | **str** | 货币的名称，例如 &#39;人民币&#39;, &#39;美元&#39; 等。 | [optional] 
**code** | **str** | 货币的ISO标准代码，例如 &#39;CNY&#39;, &#39;USD&#39; 等。 | [optional] 
**symbol** | **str** | 货币的符号，例如 &#39;$&#39;, &#39;€&#39;, &#39;¥&#39; 等。 | [optional] 
**issuer** | **str** | 发行该货币的机构或国家名称。 | [optional] 
**currency_type** | **str** | 货币的类型，例如 &#39;法定货币&#39;, &#39;加密货币&#39; 等。 | [optional] 
**tags** | **str** | 用于分类或标记货币的标签。 | [optional] 
**status** | **bool** | 指示货币当前是否可用。 | [optional] 
**enable_virtual_recharge** | **bool** | 指示该货币是否允许进行虚拟充值。 | [optional] 
**enable_virtual_consume** | **bool** | 指示该货币是否允许进行虚拟消费。 | [optional] 
**description** | **str** | 货币的详细描述信息。 | [optional] 
**fiat_exchange_rate** | **int** | 该货币与法定货币的兑换比率。 | [optional] 
**fiat_daily_recharge_limit** | **int** | 每日通过法定货币充值的最大限额。 | [optional] 
**total_supply** | **int** | 货币的总供应量，0 表示无限制。 | [optional] 
**create_date** | **datetime** | 货币记录的创建日期，默认为当前时间。 | [optional] 
**last_update** | **datetime** | 货币记录的最后更新日期，默认为当前时间。 | [optional] 

## Example

```python
from ZSGF.Client.models.currency import Currency

# TODO update the JSON string below
json = "{}"
# create an instance of Currency from a JSON string
currency_instance = Currency.from_json(json)
# print the JSON string representation of the object
print(Currency.to_json())

# convert the object into a dict
currency_dict = currency_instance.to_dict()
# create an instance of Currency from a dict
currency_from_dict = Currency.from_dict(currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


