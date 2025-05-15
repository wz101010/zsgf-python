# UserLoginsListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[UserLogins]**](UserLogins.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.user_logins_list_api_response import UserLoginsListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserLoginsListApiResponse from a JSON string
user_logins_list_api_response_instance = UserLoginsListApiResponse.from_json(json)
# print the JSON string representation of the object
print(UserLoginsListApiResponse.to_json())

# convert the object into a dict
user_logins_list_api_response_dict = user_logins_list_api_response_instance.to_dict()
# create an instance of UserLoginsListApiResponse from a dict
user_logins_list_api_response_from_dict = UserLoginsListApiResponse.from_dict(user_logins_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


