# AppUserResetPhoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | 手机号码 | [optional] 
**code** | **str** | 手机验证码 | 

## Example

```python
from ZSGF.Client.models.app_user_reset_phone_request import AppUserResetPhoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserResetPhoneRequest from a JSON string
app_user_reset_phone_request_instance = AppUserResetPhoneRequest.from_json(json)
# print the JSON string representation of the object
print(AppUserResetPhoneRequest.to_json())

# convert the object into a dict
app_user_reset_phone_request_dict = app_user_reset_phone_request_instance.to_dict()
# create an instance of AppUserResetPhoneRequest from a dict
app_user_reset_phone_request_from_dict = AppUserResetPhoneRequest.from_dict(app_user_reset_phone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


