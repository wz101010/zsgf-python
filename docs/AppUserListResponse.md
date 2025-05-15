# AppUserListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 用户ID | [optional] 
**union_id** | **str** | 用户的联合ID | [optional] 
**platform** | **str** | 用户所在平台 | [optional] 
**user_name** | **str** | 用户名 | [optional] 
**nick_name** | **str** | 用户昵称 | [optional] 
**email** | **str** | 用户邮箱 | [optional] 
**phone** | **str** | 用户电话 | [optional] 
**avatar** | **str** | 用户头像URL | [optional] 
**role** | **str** | 用户角色 | [optional] 
**role_id** | **int** | 用户角色ID | [optional] 
**create_date** | **datetime** | 用户创建日期 | [optional] 
**last_update** | **datetime** | 用户最后更新日期 | [optional] 

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


