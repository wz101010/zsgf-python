# MySqlGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_coordinate** | **float** |  | [optional] [readonly] 
**y_coordinate** | **float** |  | [optional] [readonly] 
**srid** | **int** |  | [optional] [readonly] 
**is_null** | **bool** |  | [optional] 
**value** | **bytearray** |  | [optional] [readonly] 

## Example

```python
from ZSGF.Client.models.my_sql_geometry import MySqlGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of MySqlGeometry from a JSON string
my_sql_geometry_instance = MySqlGeometry.from_json(json)
# print the JSON string representation of the object
print(MySqlGeometry.to_json())

# convert the object into a dict
my_sql_geometry_dict = my_sql_geometry_instance.to_dict()
# create an instance of MySqlGeometry from a dict
my_sql_geometry_from_dict = MySqlGeometry.from_dict(my_sql_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


