# SignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | 用户名，长度必须在6到32个字符之间，只能包含字母、数字、下划线和连字符 | 
**pwd** | **str** | 用户密码，长度必须在6到50个字符之间，可以包含数字、大小写字母、下划线、连字符和特殊符号 | 
**two_factor_code** | **str** | 双因素认证代码，如果启用双因素认证登录，则必填，长度必须为6个字符，只能包含数字 | [optional] 

## Example

```python
from ZSGF.Client.models.sign_in_request import SignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignInRequest from a JSON string
sign_in_request_instance = SignInRequest.from_json(json)
# print the JSON string representation of the object
print(SignInRequest.to_json())

# convert the object into a dict
sign_in_request_dict = sign_in_request_instance.to_dict()
# create an instance of SignInRequest from a dict
sign_in_request_from_dict = SignInRequest.from_dict(sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


