# UserCommonInterestsResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**UserCommonInterestsResult**](UserCommonInterestsResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.user_common_interests_result_api_response import UserCommonInterestsResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserCommonInterestsResultApiResponse from a JSON string
user_common_interests_result_api_response_instance = UserCommonInterestsResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(UserCommonInterestsResultApiResponse.to_json())

# convert the object into a dict
user_common_interests_result_api_response_dict = user_common_interests_result_api_response_instance.to_dict()
# create an instance of UserCommonInterestsResultApiResponse from a dict
user_common_interests_result_api_response_from_dict = UserCommonInterestsResultApiResponse.from_dict(user_common_interests_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


