# UserAccessToken

用户令牌实体，用于管理用户的访问令牌及其相关信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 用户令牌的唯一标识符。 | [optional] 
**user_id** | **int** | 与令牌关联的用户ID。 | [optional] 
**enable** | **bool** | 指示令牌是否处于启用状态。 | [optional] 
**permissions** | **str** | 令牌拥有的权限列表，多个权限以逗号分隔。 | [optional] 
**title** | **str** | 令牌的标题或名称，用于标识令牌。 | [optional] 
**access_token** | **str** | 访问令牌的具体值，用于身份验证。 | [optional] 
**tags** | **str** | 用于分类或标记令牌的标签。 | [optional] 
**description** | **str** | 令牌的详细描述信息。 | [optional] 
**expire_time** | **datetime** | 令牌的过期时间，超过该时间令牌将失效。 | [optional] 
**create_date** | **datetime** | 令牌的创建日期，默认为当前时间。 | [optional] 
**last_update** | **datetime** | 令牌的最后更新日期，默认为当前时间。 | [optional] 

## Example

```python
from ZSGF.Client.models.user_access_token import UserAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccessToken from a JSON string
user_access_token_instance = UserAccessToken.from_json(json)
# print the JSON string representation of the object
print(UserAccessToken.to_json())

# convert the object into a dict
user_access_token_dict = user_access_token_instance.to_dict()
# create an instance of UserAccessToken from a dict
user_access_token_from_dict = UserAccessToken.from_dict(user_access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


