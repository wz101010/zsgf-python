# OAuthAccountSignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**union_id** | **str** | UnionID，长度必须在1到50个字符之间，只能包含字母、数字、下划线和连字符 | 
**platform** | **str** | 平台，长度必须在1到20个字符之间，只能包含字母和数字 | 
**two_factor_code** | **str** | 双因素认证代码，如果启用双因素认证登录，则必填，长度必须为6个字符，只能包含数字 | [optional] 

## Example

```python
from ZSGF.Client.models.o_auth_account_sign_in_request import OAuthAccountSignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthAccountSignInRequest from a JSON string
o_auth_account_sign_in_request_instance = OAuthAccountSignInRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthAccountSignInRequest.to_json())

# convert the object into a dict
o_auth_account_sign_in_request_dict = o_auth_account_sign_in_request_instance.to_dict()
# create an instance of OAuthAccountSignInRequest from a dict
o_auth_account_sign_in_request_from_dict = OAuthAccountSignInRequest.from_dict(o_auth_account_sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


