# SeededConnectorCreation

A encompasing creation object that can be utilized to create either an asset or a format.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**asset** | [**SeededConnectorAsset**](SeededConnectorAsset.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_connector_creation import SeededConnectorCreation

# TODO update the JSON string below
json = "{}"
# create an instance of SeededConnectorCreation from a JSON string
seeded_connector_creation_instance = SeededConnectorCreation.from_json(json)
# print the JSON string representation of the object
print SeededConnectorCreation.to_json()

# convert the object into a dict
seeded_connector_creation_dict = seeded_connector_creation_instance.to_dict()
# create an instance of SeededConnectorCreation from a dict
seeded_connector_creation_from_dict = SeededConnectorCreation.from_dict(seeded_connector_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


