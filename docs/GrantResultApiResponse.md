# GrantResultApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**GrantResult**](GrantResult.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.grant_result_api_response import GrantResultApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GrantResultApiResponse from a JSON string
grant_result_api_response_instance = GrantResultApiResponse.from_json(json)
# print the JSON string representation of the object
print(GrantResultApiResponse.to_json())

# convert the object into a dict
grant_result_api_response_dict = grant_result_api_response_instance.to_dict()
# create an instance of GrantResultApiResponse from a dict
grant_result_api_response_from_dict = GrantResultApiResponse.from_dict(grant_result_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


