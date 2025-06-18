# SetupCodeApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**SetupCode**](SetupCode.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.setup_code_api_response import SetupCodeApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetupCodeApiResponse from a JSON string
setup_code_api_response_instance = SetupCodeApiResponse.from_json(json)
# print the JSON string representation of the object
print(SetupCodeApiResponse.to_json())

# convert the object into a dict
setup_code_api_response_dict = setup_code_api_response_instance.to_dict()
# create an instance of SetupCodeApiResponse from a dict
setup_code_api_response_from_dict = SetupCodeApiResponse.from_dict(setup_code_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


