# UserLogins

用户外部账号

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 唯一标识符 | [optional] 
**user_id** | **int** | 关联的用户ID | [optional] 
**platform_name** | **str** | 第三方平台名称 | [optional] 
**platform** | **str** | 第三方平台 | [optional] 
**union_id** | **str** | 第三方平台唯一标识 | [optional] 
**avatar** | **str** | 用户头像 | [optional] 
**data** | **str** | 扩展数据 | [optional] 
**enable** | **bool** | 启用 | [optional] 
**create_date** | **datetime** | 创建时间 | [optional] 
**last_update** | **datetime** | 最后更新时间 | [optional] 

## Example

```python
from ZSGF.Client.models.user_logins import UserLogins

# TODO update the JSON string below
json = "{}"
# create an instance of UserLogins from a JSON string
user_logins_instance = UserLogins.from_json(json)
# print the JSON string representation of the object
print(UserLogins.to_json())

# convert the object into a dict
user_logins_dict = user_logins_instance.to_dict()
# create an instance of UserLogins from a dict
user_logins_from_dict = UserLogins.from_dict(user_logins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


