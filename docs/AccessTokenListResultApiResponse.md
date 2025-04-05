# AccessTokenListResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**AccessTokenListResult**](AccessTokenListResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.access_token_list_result_api_response import AccessTokenListResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenListResultApiResponse from a JSON string
access_token_list_result_api_response_instance = AccessTokenListResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(AccessTokenListResultApiResponse.to_json())

# convert the object into a dict
access_token_list_result_api_response_dict = access_token_list_result_api_response_instance.to_dict()
# create an instance of AccessTokenListResultApiResponse from a dict
access_token_list_result_api_response_from_dict = AccessTokenListResultApiResponse.from_dict(access_token_list_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


