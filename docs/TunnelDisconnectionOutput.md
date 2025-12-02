# TunnelDisconnectionOutput

Response after disconnecting tunnel(s)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**TunnelStatus**](TunnelStatus.md) |  | 

## Example

```python
from pieces_os_client.models.tunnel_disconnection_output import TunnelDisconnectionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelDisconnectionOutput from a JSON string
tunnel_disconnection_output_instance = TunnelDisconnectionOutput.from_json(json)
# print the JSON string representation of the object
print(TunnelDisconnectionOutput.to_json())

# convert the object into a dict
tunnel_disconnection_output_dict = tunnel_disconnection_output_instance.to_dict()
# create an instance of TunnelDisconnectionOutput from a dict
tunnel_disconnection_output_from_dict = TunnelDisconnectionOutput.from_dict(tunnel_disconnection_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


