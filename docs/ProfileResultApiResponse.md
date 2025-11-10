# ProfileResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**ProfileResult**](ProfileResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.profile_result_api_response import ProfileResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileResultApiResponse from a JSON string
profile_result_api_response_instance = ProfileResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(ProfileResultApiResponse.to_json())

# convert the object into a dict
profile_result_api_response_dict = profile_result_api_response_instance.to_dict()
# create an instance of ProfileResultApiResponse from a dict
profile_result_api_response_from_dict = ProfileResultApiResponse.from_dict(profile_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


