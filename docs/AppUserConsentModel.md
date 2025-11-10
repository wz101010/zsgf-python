# AppUserConsentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**grant_type** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 
**scopes** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.app_user_consent_model import AppUserConsentModel

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserConsentModel from a JSON string
app_user_consent_model_instance = AppUserConsentModel.from_json(json)
# print the JSON string representation of the object
print(AppUserConsentModel.to_json())

# convert the object into a dict
app_user_consent_model_dict = app_user_consent_model_instance.to_dict()
# create an instance of AppUserConsentModel from a dict
app_user_consent_model_from_dict = AppUserConsentModel.from_dict(app_user_consent_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


