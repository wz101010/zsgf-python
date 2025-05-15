# AccessTokenPutRequest

请求更新访问令牌的模型

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | 访问令牌的标题 | [optional] [default to '']
**tags** | **str** | 访问令牌的标签 | [optional] [default to '']
**description** | **str** | 访问令牌的描述 | [optional] [default to '']
**permissions** | **str** | 访问令牌的权限 | [optional] [default to '']
**enable** | **bool** | 是否启用访问令牌 | [optional] 

## Example

```python
from ZSGF.Client.models.access_token_put_request import AccessTokenPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenPutRequest from a JSON string
access_token_put_request_instance = AccessTokenPutRequest.from_json(json)
# print the JSON string representation of the object
print(AccessTokenPutRequest.to_json())

# convert the object into a dict
access_token_put_request_dict = access_token_put_request_instance.to_dict()
# create an instance of AccessTokenPutRequest from a dict
access_token_put_request_from_dict = AccessTokenPutRequest.from_dict(access_token_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


