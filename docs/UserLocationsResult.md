# UserLocationsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_locations** | **int** |  | [optional] 
**data** | [**List[GeoLocationResponseModel]**](GeoLocationResponseModel.md) |  | [optional] 

## Example

```python
from ZSGF.Client.models.user_locations_result import UserLocationsResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserLocationsResult from a JSON string
user_locations_result_instance = UserLocationsResult.from_json(json)
# print the JSON string representation of the object
print(UserLocationsResult.to_json())

# convert the object into a dict
user_locations_result_dict = user_locations_result_instance.to_dict()
# create an instance of UserLocationsResult from a dict
user_locations_result_from_dict = UserLocationsResult.from_dict(user_locations_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


