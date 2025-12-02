# TunnelInformation

Information about a specific tunnel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** | This is the auth_token for a user to access their tunnel url. | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**id** | **str** | Unique tunnel identifier | 
**port** | **int** | Local port being exposed | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**TunnelStatusEnum**](TunnelStatusEnum.md) |  | 
**url** | **str** | Full public URL for the tunnel | 

## Example

```python
from pieces_os_client.models.tunnel_information import TunnelInformation

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelInformation from a JSON string
tunnel_information_instance = TunnelInformation.from_json(json)
# print the JSON string representation of the object
print(TunnelInformation.to_json())

# convert the object into a dict
tunnel_information_dict = tunnel_information_instance.to_dict()
# create an instance of TunnelInformation from a dict
tunnel_information_from_dict = TunnelInformation.from_dict(tunnel_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


