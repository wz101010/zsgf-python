# BkAgentRespInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bindclrissr_id** | **str** |  | [optional] 
**bindpyeracctbk_id** | **str** |  | [optional] 
**bindtrx_id** | **str** |  | [optional] 
**bkpyeruser_code** | **str** |  | [optional] 
**estter_location** | **str** |  | [optional] 

## Example

```python
from ZSGF.Client.models.bk_agent_resp_info import BkAgentRespInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BkAgentRespInfo from a JSON string
bk_agent_resp_info_instance = BkAgentRespInfo.from_json(json)
# print the JSON string representation of the object
print(BkAgentRespInfo.to_json())

# convert the object into a dict
bk_agent_resp_info_dict = bk_agent_resp_info_instance.to_dict()
# create an instance of BkAgentRespInfo from a dict
bk_agent_resp_info_from_dict = BkAgentRespInfo.from_dict(bk_agent_resp_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


