# GetUserProfileResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**GetUserProfileResult**](GetUserProfileResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.get_user_profile_result_api_response import GetUserProfileResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserProfileResultApiResponse from a JSON string
get_user_profile_result_api_response_instance = GetUserProfileResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserProfileResultApiResponse.to_json())

# convert the object into a dict
get_user_profile_result_api_response_dict = get_user_profile_result_api_response_instance.to_dict()
# create an instance of GetUserProfileResultApiResponse from a dict
get_user_profile_result_api_response_from_dict = GetUserProfileResultApiResponse.from_dict(get_user_profile_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


