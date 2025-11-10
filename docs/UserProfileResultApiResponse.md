# UserProfileResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**UserProfileResult**](UserProfileResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.user_profile_result_api_response import UserProfileResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileResultApiResponse from a JSON string
user_profile_result_api_response_instance = UserProfileResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(UserProfileResultApiResponse.to_json())

# convert the object into a dict
user_profile_result_api_response_dict = user_profile_result_api_response_instance.to_dict()
# create an instance of UserProfileResultApiResponse from a dict
user_profile_result_api_response_from_dict = UserProfileResultApiResponse.from_dict(user_profile_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


