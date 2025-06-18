# GeoLocationModelApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**GeoLocationModel**](GeoLocationModel.md) |  | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.geo_location_model_api_response import GeoLocationModelApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeoLocationModelApiResponse from a JSON string
geo_location_model_api_response_instance = GeoLocationModelApiResponse.from_json(json)
# print the JSON string representation of the object
print(GeoLocationModelApiResponse.to_json())

# convert the object into a dict
geo_location_model_api_response_dict = geo_location_model_api_response_instance.to_dict()
# create an instance of GeoLocationModelApiResponse from a dict
geo_location_model_api_response_from_dict = GeoLocationModelApiResponse.from_dict(geo_location_model_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


