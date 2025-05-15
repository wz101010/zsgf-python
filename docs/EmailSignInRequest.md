# EmailSignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | 用户邮箱地址 | 
**verify_code** | **str** | 验证码，长度为4到8位的数字 | 
**two_factor_code** | **str** | 双因素认证代码，如果启用双因素认证登录，则必填 | [optional] 

## Example

```python
from ZSGF.Client.models.email_sign_in_request import EmailSignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSignInRequest from a JSON string
email_sign_in_request_instance = EmailSignInRequest.from_json(json)
# print the JSON string representation of the object
print(EmailSignInRequest.to_json())

# convert the object into a dict
email_sign_in_request_dict = email_sign_in_request_instance.to_dict()
# create an instance of EmailSignInRequest from a dict
email_sign_in_request_from_dict = EmailSignInRequest.from_dict(email_sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


