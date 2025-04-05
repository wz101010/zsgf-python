# AppUserListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**union_id** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**role_id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 

## Example

```python
from ZSGF.Client.models.app_user_list_response import AppUserListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserListResponse from a JSON string
app_user_list_response_instance = AppUserListResponse.from_json(json)
# print the JSON string representation of the object
print(AppUserListResponse.to_json())

# convert the object into a dict
app_user_list_response_dict = app_user_list_response_instance.to_dict()
# create an instance of AppUserListResponse from a dict
app_user_list_response_from_dict = AppUserListResponse.from_dict(app_user_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


