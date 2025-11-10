# ContributeDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contribute_amount** | **str** |  | [optional] 
**contribute_type** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.contribute_detail import ContributeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ContributeDetail from a JSON string
contribute_detail_instance = ContributeDetail.from_json(json)
# print the JSON string representation of the object
print(ContributeDetail.to_json())

# convert the object into a dict
contribute_detail_dict = contribute_detail_instance.to_dict()
# create an instance of ContributeDetail from a dict
contribute_detail_from_dict = ContributeDetail.from_dict(contribute_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


