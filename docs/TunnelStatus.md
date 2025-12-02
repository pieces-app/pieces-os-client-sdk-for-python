# TunnelStatus

Current status of tunnels and connections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**tunnels** | [**List[TunnelInformation]**](TunnelInformation.md) |  | 
**version** | **str** | NGrok client version | [optional] 

## Example

```python
from pieces_os_client.models.tunnel_status import TunnelStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelStatus from a JSON string
tunnel_status_instance = TunnelStatus.from_json(json)
# print the JSON string representation of the object
print(TunnelStatus.to_json())

# convert the object into a dict
tunnel_status_dict = tunnel_status_instance.to_dict()
# create an instance of TunnelStatus from a dict
tunnel_status_from_dict = TunnelStatus.from_dict(tunnel_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


