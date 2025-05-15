# UnionIDSignInRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**union_id** | **str** | UnionID，长度必须在1到99个字符之间，只能包含字母、数字、下划线和连字符 | 
**platform** | **str** | 平台，长度必须在1到20个字符之间，只能包含字母和数字 | 
**two_factor_code** | **str** | 双因素认证代码，如果启用双因素认证登录，则必填，长度必须为6个字符，只能包含数字 | [optional] 

## Example

```python
from ZSGF.Client.models.union_id_sign_in_request import UnionIDSignInRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnionIDSignInRequest from a JSON string
union_id_sign_in_request_instance = UnionIDSignInRequest.from_json(json)
# print the JSON string representation of the object
print(UnionIDSignInRequest.to_json())

# convert the object into a dict
union_id_sign_in_request_dict = union_id_sign_in_request_instance.to_dict()
# create an instance of UnionIDSignInRequest from a dict
union_id_sign_in_request_from_dict = UnionIDSignInRequest.from_dict(union_id_sign_in_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


