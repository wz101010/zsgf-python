# UserCurrencyCurrencyTransResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**data** | [**List[CurrencyTransaction]**](CurrencyTransaction.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.user_currency_currency_trans_result import UserCurrencyCurrencyTransResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserCurrencyCurrencyTransResult from a JSON string
user_currency_currency_trans_result_instance = UserCurrencyCurrencyTransResult.from_json(json)
# print the JSON string representation of the object
print(UserCurrencyCurrencyTransResult.to_json())

# convert the object into a dict
user_currency_currency_trans_result_dict = user_currency_currency_trans_result_instance.to_dict()
# create an instance of UserCurrencyCurrencyTransResult from a dict
user_currency_currency_trans_result_from_dict = UserCurrencyCurrencyTransResult.from_dict(user_currency_currency_trans_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


