# PhoneSignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | 用户手机号 | 
**verify_code** | **str** | 验证码，长度为4到8位的数字 | 
**two_factor_code** | **str** | 双因素认证代码，如果启用双因素认证登录，则必填，长度必须为6个字符，只能包含数字 | [optional] 

## Example

```python
from ZSGF.Client.models.phone_sign_in_request import PhoneSignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneSignInRequest from a JSON string
phone_sign_in_request_instance = PhoneSignInRequest.from_json(json)
# print the JSON string representation of the object
print(PhoneSignInRequest.to_json())

# convert the object into a dict
phone_sign_in_request_dict = phone_sign_in_request_instance.to_dict()
# create an instance of PhoneSignInRequest from a dict
phone_sign_in_request_from_dict = PhoneSignInRequest.from_dict(phone_sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


