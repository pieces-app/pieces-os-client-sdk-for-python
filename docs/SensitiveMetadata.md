# SensitiveMetadata

This is optional metatdata attached to a sensitive piece of data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entropy** | **float** | entropy of the sensitive | [optional] 
**match** | [**TextMatch**](TextMatch.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.sensitive_metadata import SensitiveMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SensitiveMetadata from a JSON string
sensitive_metadata_instance = SensitiveMetadata.from_json(json)
# print the JSON string representation of the object
print(SensitiveMetadata.to_json())

# convert the object into a dict
sensitive_metadata_dict = sensitive_metadata_instance.to_dict()
# create an instance of SensitiveMetadata from a dict
sensitive_metadata_from_dict = SensitiveMetadata.from_dict(sensitive_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


