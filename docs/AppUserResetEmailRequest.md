# AppUserResetEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | 邮箱 | [optional] 
**code** | **str** | 邮箱验证码 | 

## Example

```python
from ZSGF.Client.models.app_user_reset_email_request import AppUserResetEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserResetEmailRequest from a JSON string
app_user_reset_email_request_instance = AppUserResetEmailRequest.from_json(json)
# print the JSON string representation of the object
print(AppUserResetEmailRequest.to_json())

# convert the object into a dict
app_user_reset_email_request_dict = app_user_reset_email_request_instance.to_dict()
# create an instance of AppUserResetEmailRequest from a dict
app_user_reset_email_request_from_dict = AppUserResetEmailRequest.from_dict(app_user_reset_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


