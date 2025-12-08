# TunnelDisconnectionInput

Request body for disconnecting tunnel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.tunnel_disconnection_input import TunnelDisconnectionInput

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelDisconnectionInput from a JSON string
tunnel_disconnection_input_instance = TunnelDisconnectionInput.from_json(json)
# print the JSON string representation of the object
print(TunnelDisconnectionInput.to_json())

# convert the object into a dict
tunnel_disconnection_input_dict = tunnel_disconnection_input_instance.to_dict()
# create an instance of TunnelDisconnectionInput from a dict
tunnel_disconnection_input_from_dict = TunnelDisconnectionInput.from_dict(tunnel_disconnection_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


