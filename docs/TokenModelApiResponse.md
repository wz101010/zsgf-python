# TokenModelApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**TokenModel**](TokenModel.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.token_model_api_response import TokenModelApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenModelApiResponse from a JSON string
token_model_api_response_instance = TokenModelApiResponse.from_json(json)
# print the JSON string representation of the object
print(TokenModelApiResponse.to_json())

# convert the object into a dict
token_model_api_response_dict = token_model_api_response_instance.to_dict()
# create an instance of TokenModelApiResponse from a dict
token_model_api_response_from_dict = TokenModelApiResponse.from_dict(token_model_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


