# UpdateProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str** | 用户头像的链接或路径，长度不能超过255个字符 | [optional] 
**data** | **str** | 用户的其他数据，可以是序列化后的对象或JSON字符串 | [optional] 
**nick_name** | **str** | 用户的昵称，长度不能超过50个字符 | [optional] 
**interest_tags** | **str** | 兴趣标签 | [optional] 
**biography** | **str** | 个人简介，长度不能超过500个字符 | [optional] 
**gender** | **str** | 性别，长度不能超过15个字符 | [optional] 
**birthday** | **datetime** | 生日 | [optional] 
**occupation** | **str** | 职业，长度不能超过50个字符 | [optional] 
**education** | **str** | 学历，长度不能超过50个字符 | [optional] 
**contact** | **str** | 联系方式，长度不能超过255个字符 | [optional] 
**languages** | **str** | 语言，长度不能超过50个字符 | [optional] 
**social_links** | **str** | 社交网络链接，长度不能超过255个字符 | [optional] 
**relationship_status** | **str** | 婚姻状态，长度不能超过20个字符 | [optional] 
**company** | **str** | 公司，长度不能超过100个字符 | [optional] 
**industry** | **str** | 行业，长度不能超过50个字符 | [optional] 
**company_position** | **str** | 行业职位，长度不能超过50个字符 | [optional] 
**private_settings** | **str** | 私密设置，长度不能超过500个字符 | [optional] 
**enable2_fa_auth** | **bool** | 是否启用二步验证 | [optional] 
**enable_user_name_sign_in** | **bool** | 是否启用账号登录 | [optional] 
**enable_email_sign_in** | **bool** | 是否启用邮箱登录 | [optional] 
**enable_phone_sign_in** | **bool** | 是否启用手机登录 | [optional] 
**enable_union_id_sign_in** | **bool** | 是否启用UnionID登录 | [optional] 
**enable_o_auth** | **bool** | 是否启用OAuth2登录 | [optional] 

## Example

```python
from ZSGF.Client.models.update_profile_request import UpdateProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProfileRequest from a JSON string
update_profile_request_instance = UpdateProfileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProfileRequest.to_json())

# convert the object into a dict
update_profile_request_dict = update_profile_request_instance.to_dict()
# create an instance of UpdateProfileRequest from a dict
update_profile_request_from_dict = UpdateProfileRequest.from_dict(update_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


