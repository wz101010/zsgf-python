# CreatePostResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**CreatePostResult**](CreatePostResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.create_post_result_api_response import CreatePostResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePostResultApiResponse from a JSON string
create_post_result_api_response_instance = CreatePostResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePostResultApiResponse.to_json())

# convert the object into a dict
create_post_result_api_response_dict = create_post_result_api_response_instance.to_dict()
# create an instance of CreatePostResultApiResponse from a dict
create_post_result_api_response_from_dict = CreatePostResultApiResponse.from_dict(create_post_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


