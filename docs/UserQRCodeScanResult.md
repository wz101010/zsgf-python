# UserQRCodeScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**scopes** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 
**scheme** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.user_qr_code_scan_result import UserQRCodeScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserQRCodeScanResult from a JSON string
user_qr_code_scan_result_instance = UserQRCodeScanResult.from_json(json)
# print the JSON string representation of the object
print(UserQRCodeScanResult.to_json())

# convert the object into a dict
user_qr_code_scan_result_dict = user_qr_code_scan_result_instance.to_dict()
# create an instance of UserQRCodeScanResult from a dict
user_qr_code_scan_result_from_dict = UserQRCodeScanResult.from_dict(user_qr_code_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


