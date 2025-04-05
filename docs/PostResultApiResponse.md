# PostResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**PostResult**](PostResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.post_result_api_response import PostResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostResultApiResponse from a JSON string
post_result_api_response_instance = PostResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(PostResultApiResponse.to_json())

# convert the object into a dict
post_result_api_response_dict = post_result_api_response_instance.to_dict()
# create an instance of PostResultApiResponse from a dict
post_result_api_response_from_dict = PostResultApiResponse.from_dict(post_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


