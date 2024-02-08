# ExistingMetadata

This is a shared input model for all the exists endpoints: /tags/exists : if the tag exists you will have a defined tag:ReferencedTag, if not then it doesnt exist. /websites/exists: if the url exists you will have a defined website:ReferencedWebsite, if not then it doesnt exist.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**website** | [**ReferencedWebsite**](ReferencedWebsite.md) |  | [optional] 
**tag** | [**ReferencedTag**](ReferencedTag.md) |  | [optional] 

## Example

```python
from openapi_client.models.existing_metadata import ExistingMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ExistingMetadata from a JSON string
existing_metadata_instance = ExistingMetadata.from_json(json)
# print the JSON string representation of the object
print ExistingMetadata.to_json()

# convert the object into a dict
existing_metadata_dict = existing_metadata_instance.to_dict()
# create an instance of ExistingMetadata from a dict
existing_metadata_form_dict = existing_metadata.from_dict(existing_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


