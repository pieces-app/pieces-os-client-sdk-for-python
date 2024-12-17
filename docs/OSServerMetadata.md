# OSServerMetadata

This will return metadata (total materials) in your pieces drive.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**totals** | [**TrackedSummaryTotals**](TrackedSummaryTotals.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.os_server_metadata import OSServerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OSServerMetadata from a JSON string
os_server_metadata_instance = OSServerMetadata.from_json(json)
# print the JSON string representation of the object
print OSServerMetadata.to_json()

# convert the object into a dict
os_server_metadata_dict = os_server_metadata_instance.to_dict()
# create an instance of OSServerMetadata from a dict
os_server_metadata_from_dict = OSServerMetadata.from_dict(os_server_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


