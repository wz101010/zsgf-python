# User

用户

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 用户唯一标识 | [optional] 
**platform** | **str** | 用户所在平台 | [optional] 
**union_id** | **str** | 用户所在平台的唯一标识 | [optional] 
**nick_name** | **str** | 昵称 | [optional] 
**avatar** | **str** | 头像 | [optional] 
**data** | **str** | 其他数据 | [optional] 
**user_name** | **str** | 用户名 | [optional] 
**pwd** | **str** | 用户密码 | [optional] 
**email** | **str** | 邮箱地址 | [optional] 
**email_is_valid** | **bool** | 邮箱已验证 | [optional] 
**phone** | **str** | 手机号码 | [optional] 
**phone_is_valid** | **bool** | 手机号码已验证 | [optional] 
**relation_chain** | **str** | 关系链 | [optional] 
**interest_tags** | **str** | 兴趣标签 | [optional] 
**biography** | **str** | 个人简介 | [optional] 
**gender** | **str** | 性别 | [optional] 
**birthday** | **datetime** | 生日 | [optional] 
**occupation** | **str** | 职业 | [optional] 
**education** | **str** | 学历 | [optional] 
**contact** | **str** | 联系方式 | [optional] 
**languages** | **str** | 语言 | [optional] 
**social_links** | **str** | 社交网络链接 | [optional] 
**relationship_status** | **str** | 婚姻状态 | [optional] 
**company** | **str** | 公司 | [optional] 
**industry** | **str** | 行业 | [optional] 
**company_position** | **str** | 行业职位 | [optional] 
**private_settings** | **str** | 私密设置 | [optional] 
**is_lock** | **bool** | 账户是否锁定 | [optional] 
**lock_until** | **datetime** | 账户锁定截止时间 | [optional] 
**enable_user_name_sign_in** | **bool** | 能使用用户名登录 | [optional] 
**enable_email_sign_in** | **bool** | 能使用邮箱登录 | [optional] 
**enable_phone_sign_in** | **bool** | 能使用电话号码登录 | [optional] 
**enable_union_id_sign_in** | **bool** | 能使用联合身份标识登录 | [optional] 
**enable_o_auth** | **bool** | 能使用OAuth认证方式登录 | [optional] 
**enable2_fa_auth** | **bool** | 启用双因素认证登录 | [optional] 
**create_date** | **datetime** | 创建时间 | [optional] 
**last_update** | **datetime** | 最后更新时间 | [optional] 

## Example

```python
from ZSGF.Client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


