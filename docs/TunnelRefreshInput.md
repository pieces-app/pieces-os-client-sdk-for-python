# TunnelRefreshInput

Request body for refreshing tunnel connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.tunnel_refresh_input import TunnelRefreshInput

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelRefreshInput from a JSON string
tunnel_refresh_input_instance = TunnelRefreshInput.from_json(json)
# print the JSON string representation of the object
print(TunnelRefreshInput.to_json())

# convert the object into a dict
tunnel_refresh_input_dict = tunnel_refresh_input_instance.to_dict()
# create an instance of TunnelRefreshInput from a dict
tunnel_refresh_input_from_dict = TunnelRefreshInput.from_dict(tunnel_refresh_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


