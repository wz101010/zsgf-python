# ExternalAccountBindRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**union_id** | **str** |  | 
**platform** | **str** |  | 
**platform_name** | **str** |  | 
**avatar** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.external_account_bind_request import ExternalAccountBindRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAccountBindRequest from a JSON string
external_account_bind_request_instance = ExternalAccountBindRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalAccountBindRequest.to_json())

# convert the object into a dict
external_account_bind_request_dict = external_account_bind_request_instance.to_dict()
# create an instance of ExternalAccountBindRequest from a dict
external_account_bind_request_from_dict = ExternalAccountBindRequest.from_dict(external_account_bind_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


