# CurrencyTransaction

货币交易记录实体，用于记录用户的货币交易详情。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 货币交易记录的唯一标识符。 | [optional] 
**from_user_id** | **int** | 发起交易的发送方用户ID，若为转账交易时必填。 | [optional] 
**user_id** | **int** | 进行货币交易的用户ID。 | [optional] 
**transaction_type** | **str** | 货币交易的类型，例如 &#39;消费&#39;, &#39;奖励&#39;, &#39;兑换&#39;, &#39;转账&#39; 等。 | [optional] 
**currency_type** | **str** | 交易的货币类型，例如 &#39;USD&#39;, &#39;CNY&#39; 等。 | [optional] 
**currency_change** | **int** | 货币的变动数量，正数表示增加，负数表示减少。 | [optional] 
**currency_balance** | **float** | 交易完成后的货币余额。 | [optional] 
**description** | **str** | 描述货币变动的具体原因或相关交易详情。 | [optional] 
**status** | **str** | 货币交易的当前状态，例如 &#39;成功&#39;, &#39;失败&#39;, &#39;待审核&#39; 等。 | [optional] 
**remark** | **str** | 交易的额外信息或管理员的备注。 | [optional] 
**tags** | **str** | 用于分类或标记交易的标签。 | [optional] 
**create_date** | **datetime** | 货币交易发生的时间，默认为当前时间。 | [optional] 

## Example

```python
from ZSGF.Client.models.currency_transaction import CurrencyTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyTransaction from a JSON string
currency_transaction_instance = CurrencyTransaction.from_json(json)
# print the JSON string representation of the object
print(CurrencyTransaction.to_json())

# convert the object into a dict
currency_transaction_dict = currency_transaction_instance.to_dict()
# create an instance of CurrencyTransaction from a dict
currency_transaction_from_dict = CurrencyTransaction.from_dict(currency_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


