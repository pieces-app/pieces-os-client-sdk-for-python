# SeededExternalProvider

This is the minimum information needed to connect an additional provider.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExternalProviderTypeEnum**](ExternalProviderTypeEnum.md) |  | 

## Example

```python
from openapi_client.models.seeded_external_provider import SeededExternalProvider

# TODO update the JSON string below
json = "{}"
# create an instance of SeededExternalProvider from a JSON string
seeded_external_provider_instance = SeededExternalProvider.from_json(json)
# print the JSON string representation of the object
print SeededExternalProvider.to_json()

# convert the object into a dict
seeded_external_provider_dict = seeded_external_provider_instance.to_dict()
# create an instance of SeededExternalProvider from a dict
seeded_external_provider_form_dict = seeded_external_provider.from_dict(seeded_external_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


