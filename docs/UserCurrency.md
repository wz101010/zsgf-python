# UserCurrency

用户资产实体，用于记录用户的货币余额和相关信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 用户资产的唯一标识符。 | [optional] 
**user_id** | **int** | 与用户资产关联的用户ID。 | [optional] 
**currency_code** | **str** | 用户资产的货币代码，例如 &#39;USD&#39;, &#39;CNY&#39; 等。 | [optional] 
**balance** | **int** | 用户的账户余额，表示当前持有的货币数量。 | [optional] 

## Example

```python
from ZSGF.Client.models.user_currency import UserCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of UserCurrency from a JSON string
user_currency_instance = UserCurrency.from_json(json)
# print the JSON string representation of the object
print(UserCurrency.to_json())

# convert the object into a dict
user_currency_dict = user_currency_instance.to_dict()
# create an instance of UserCurrency from a dict
user_currency_from_dict = UserCurrency.from_dict(user_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


