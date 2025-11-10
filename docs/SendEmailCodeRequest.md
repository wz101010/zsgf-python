# SendEmailCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | 用户邮箱地址 | 
**type** | **str** | 用途。可选值：signup、forgetpwd、signin、reset | 

## Example

```python
from ZSGF.Client.models.send_email_code_request import SendEmailCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailCodeRequest from a JSON string
send_email_code_request_instance = SendEmailCodeRequest.from_json(json)
# print the JSON string representation of the object
print(SendEmailCodeRequest.to_json())

# convert the object into a dict
send_email_code_request_dict = send_email_code_request_instance.to_dict()
# create an instance of SendEmailCodeRequest from a dict
send_email_code_request_from_dict = SendEmailCodeRequest.from_dict(send_email_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


