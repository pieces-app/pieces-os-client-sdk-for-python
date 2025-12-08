# TunnelConnectionInput

Request body for connecting to tunnel service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.tunnel_connection_input import TunnelConnectionInput

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelConnectionInput from a JSON string
tunnel_connection_input_instance = TunnelConnectionInput.from_json(json)
# print the JSON string representation of the object
print(TunnelConnectionInput.to_json())

# convert the object into a dict
tunnel_connection_input_dict = tunnel_connection_input_instance.to_dict()
# create an instance of TunnelConnectionInput from a dict
tunnel_connection_input_from_dict = TunnelConnectionInput.from_dict(tunnel_connection_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


