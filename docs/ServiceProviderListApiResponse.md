# ServiceProviderListApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码 | [optional] [default to 200]
**data** | [**List[ServiceProvider]**](ServiceProvider.md) | 响应数据 | [optional] 
**error** | **str** | 错误信息 | [optional] [default to '']

## Example

```python
from ZSGF.Client.models.service_provider_list_api_response import ServiceProviderListApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProviderListApiResponse from a JSON string
service_provider_list_api_response_instance = ServiceProviderListApiResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceProviderListApiResponse.to_json())

# convert the object into a dict
service_provider_list_api_response_dict = service_provider_list_api_response_instance.to_dict()
# create an instance of ServiceProviderListApiResponse from a dict
service_provider_list_api_response_from_dict = ServiceProviderListApiResponse.from_dict(service_provider_list_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


