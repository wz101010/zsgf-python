# AuthorizePolicyListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[AuthorizePolicy]**](AuthorizePolicy.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.authorize_policy_list_api_response import AuthorizePolicyListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizePolicyListApiResponse from a JSON string
authorize_policy_list_api_response_instance = AuthorizePolicyListApiResponse.from_json(json)
# print the JSON string representation of the object
print(AuthorizePolicyListApiResponse.to_json())

# convert the object into a dict
authorize_policy_list_api_response_dict = authorize_policy_list_api_response_instance.to_dict()
# create an instance of AuthorizePolicyListApiResponse from a dict
authorize_policy_list_api_response_from_dict = AuthorizePolicyListApiResponse.from_dict(authorize_policy_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


