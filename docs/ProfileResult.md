# ProfileResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**union_id** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**user_name** | **str** |  | [optional] 
**phone_is_valid** | **bool** |  | [optional] 
**data** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_is_valid** | **bool** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.profile_result import ProfileResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileResult from a JSON string
profile_result_instance = ProfileResult.from_json(json)
# print the JSON string representation of the object
print(ProfileResult.to_json())

# convert the object into a dict
profile_result_dict = profile_result_instance.to_dict()
# create an instance of ProfileResult from a dict
profile_result_from_dict = ProfileResult.from_dict(profile_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


