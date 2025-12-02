# TunnelRefreshOutput

Response after refreshing tunnel connection(s)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**TunnelStatus**](TunnelStatus.md) |  | 

## Example

```python
from pieces_os_client.models.tunnel_refresh_output import TunnelRefreshOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelRefreshOutput from a JSON string
tunnel_refresh_output_instance = TunnelRefreshOutput.from_json(json)
# print the JSON string representation of the object
print(TunnelRefreshOutput.to_json())

# convert the object into a dict
tunnel_refresh_output_dict = tunnel_refresh_output_instance.to_dict()
# create an instance of TunnelRefreshOutput from a dict
tunnel_refresh_output_from_dict = TunnelRefreshOutput.from_dict(tunnel_refresh_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


