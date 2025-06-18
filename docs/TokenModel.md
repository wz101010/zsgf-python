# TokenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 

## Example

```python
from ZSGF.Client.models.token_model import TokenModel

# TODO update the JSON string below
json = "{}"
# create an instance of TokenModel from a JSON string
token_model_instance = TokenModel.from_json(json)
# print the JSON string representation of the object
print(TokenModel.to_json())

# convert the object into a dict
token_model_dict = token_model_instance.to_dict()
# create an instance of TokenModel from a dict
token_model_from_dict = TokenModel.from_dict(token_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


