# AppUserConsentModelListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[AppUserConsentModel]**](AppUserConsentModel.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.app_user_consent_model_list_api_response import AppUserConsentModelListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserConsentModelListApiResponse from a JSON string
app_user_consent_model_list_api_response_instance = AppUserConsentModelListApiResponse.from_json(json)
# print the JSON string representation of the object
print(AppUserConsentModelListApiResponse.to_json())

# convert the object into a dict
app_user_consent_model_list_api_response_dict = app_user_consent_model_list_api_response_instance.to_dict()
# create an instance of AppUserConsentModelListApiResponse from a dict
app_user_consent_model_list_api_response_from_dict = AppUserConsentModelListApiResponse.from_dict(app_user_consent_model_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


