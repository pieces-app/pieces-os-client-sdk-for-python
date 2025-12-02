# TunnelConnectionOutput

Response after successfully connecting to tunnel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**TunnelStatus**](TunnelStatus.md) |  | 
**tunnel** | [**TunnelInformation**](TunnelInformation.md) |  | 

## Example

```python
from pieces_os_client.models.tunnel_connection_output import TunnelConnectionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelConnectionOutput from a JSON string
tunnel_connection_output_instance = TunnelConnectionOutput.from_json(json)
# print the JSON string representation of the object
print(TunnelConnectionOutput.to_json())

# convert the object into a dict
tunnel_connection_output_dict = tunnel_connection_output_instance.to_dict()
# create an instance of TunnelConnectionOutput from a dict
tunnel_connection_output_from_dict = TunnelConnectionOutput.from_dict(tunnel_connection_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


