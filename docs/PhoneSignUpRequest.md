# PhoneSignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | 用户手机号 | 
**phone_code** | **str** | 手机验证码，长度为4到8位的数字 | 
**pwd** | **str** | 用户密码，长度为6到32个字符 | 
**email** | **str** | 用户邮箱 | [optional] 
**email_code** | **str** | 邮箱验证码（只有启用的邮箱验证码功能时，才需要传入），长度为4到8位的数字 | [optional] 
**nick_name** | **str** | 用户昵称 | [optional] 
**avatar** | **str** | 用户头像URL | [optional] 
**data** | **str** | 自定义数据 | [optional] 

## Example

```python
from ZSGF.Client.models.phone_sign_up_request import PhoneSignUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneSignUpRequest from a JSON string
phone_sign_up_request_instance = PhoneSignUpRequest.from_json(json)
# print the JSON string representation of the object
print(PhoneSignUpRequest.to_json())

# convert the object into a dict
phone_sign_up_request_dict = phone_sign_up_request_instance.to_dict()
# create an instance of PhoneSignUpRequest from a dict
phone_sign_up_request_from_dict = PhoneSignUpRequest.from_dict(phone_sign_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


