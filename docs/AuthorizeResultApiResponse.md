# AuthorizeResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**AuthorizeResult**](AuthorizeResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.authorize_result_api_response import AuthorizeResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeResultApiResponse from a JSON string
authorize_result_api_response_instance = AuthorizeResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(AuthorizeResultApiResponse.to_json())

# convert the object into a dict
authorize_result_api_response_dict = authorize_result_api_response_instance.to_dict()
# create an instance of AuthorizeResultApiResponse from a dict
authorize_result_api_response_from_dict = AuthorizeResultApiResponse.from_dict(authorize_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


