# ExternalAccountPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str** | 头像 | [optional] 
**data** | **str** | 自定义数据 | [optional] 
**enable** | **bool** | 启用 | [optional] 

## Example

```python
from ZSGF.Client.models.external_account_put_request import ExternalAccountPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAccountPutRequest from a JSON string
external_account_put_request_instance = ExternalAccountPutRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalAccountPutRequest.to_json())

# convert the object into a dict
external_account_put_request_dict = external_account_put_request_instance.to_dict()
# create an instance of ExternalAccountPutRequest from a dict
external_account_put_request_from_dict = ExternalAccountPutRequest.from_dict(external_account_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


