# UnionIDSignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | 登录账号，可空，只能包含字母、数字、下划线和连字符 | [optional] 
**union_id** | **str** | UnionID，长度不能超过99个字符，只能包含字母、数字、下划线和连字符 | 
**platform** | **str** | 平台标识，长度必须在1到20个字符之间，只能包含字母和数字 | 
**pwd** | **str** | 密码，长度必须在6到32个字符之间，只允许英文大小写、数字、标点符号 | 
**nick_name** | **str** | 用户昵称 | [optional] 
**avatar** | **str** | 用户头像URL | [optional] 
**data** | **str** | 自定义数据 | [optional] 
**email** | **str** | 用户邮箱 | [optional] 
**email_code** | **str** | 邮箱验证码（只有启用的邮箱验证码功能时，才需要传入），长度为4到8位的数字 | [optional] 
**phone** | **str** | 用户手机号，必须为11位数字 | [optional] 
**phone_code** | **str** | 手机验证码（只有启用的手机验证码功能时，才需要传入），长度为4到8位的数字 | [optional] 

## Example

```python
from ZSGF.Client.models.union_id_sign_up_request import UnionIDSignUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnionIDSignUpRequest from a JSON string
union_id_sign_up_request_instance = UnionIDSignUpRequest.from_json(json)
# print the JSON string representation of the object
print(UnionIDSignUpRequest.to_json())

# convert the object into a dict
union_id_sign_up_request_dict = union_id_sign_up_request_instance.to_dict()
# create an instance of UnionIDSignUpRequest from a dict
union_id_sign_up_request_from_dict = UnionIDSignUpRequest.from_dict(union_id_sign_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


