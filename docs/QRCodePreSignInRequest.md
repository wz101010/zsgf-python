# QRCodePreSignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **str** | 授权范围，长度不能超过100个字符，只能包含字母、数字和逗号 | [optional] 
**remark** | **str** | 备注，长度不能超过200个字符 | [optional] 
**scheme** | **str** | 方案，长度不能超过50个字符，只能包含字母和数字 | [optional] 

## Example

```python
from ZSGF.Client.models.qr_code_pre_sign_in_request import QRCodePreSignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QRCodePreSignInRequest from a JSON string
qr_code_pre_sign_in_request_instance = QRCodePreSignInRequest.from_json(json)
# print the JSON string representation of the object
print(QRCodePreSignInRequest.to_json())

# convert the object into a dict
qr_code_pre_sign_in_request_dict = qr_code_pre_sign_in_request_instance.to_dict()
# create an instance of QRCodePreSignInRequest from a dict
qr_code_pre_sign_in_request_from_dict = QRCodePreSignInRequest.from_dict(qr_code_pre_sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


