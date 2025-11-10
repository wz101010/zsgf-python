# SignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | 用户名，长度必须在6到32个字符之间，只能包含字母、数字、下划线和连字符 | 
**pwd** | **str** | 登录密码，长度必须在6到32个字符之间，只能包含字母和数字 | 
**nick_name** | **str** | 用户昵称，长度不能超过20个字符 | [optional] 
**avatar** | **str** | 用户头像URL | [optional] 
**data** | **str** | 自定义数据 | [optional] 
**email** | **str** | 用户邮箱 | [optional] 
**email_code** | **str** | 邮箱验证码（只有启用的邮箱验证码功能时，才需要传入），长度为4到8位的数字 | [optional] 
**phone** | **str** | 用户手机号，必须为11位数字 | [optional] 
**phone_code** | **str** | 手机验证码（只有启用的手机验证码功能时，才需要传入），长度为4到8位的数字 | [optional] 

## Example

```python
from ZSGF.Client.models.sign_up_request import SignUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignUpRequest from a JSON string
sign_up_request_instance = SignUpRequest.from_json(json)
# print the JSON string representation of the object
print(SignUpRequest.to_json())

# convert the object into a dict
sign_up_request_dict = sign_up_request_instance.to_dict()
# create an instance of SignUpRequest from a dict
sign_up_request_from_dict = SignUpRequest.from_dict(sign_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


