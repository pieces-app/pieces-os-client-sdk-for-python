# CreatedExternalProviderApiKey

This is the outputmodel for /external_provider/api_key/create

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**metadata** | [**Auth0UserMetadata**](Auth0UserMetadata.md) |  | 

## Example

```python
from openapi_client.models.created_external_provider_api_key import CreatedExternalProviderApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedExternalProviderApiKey from a JSON string
created_external_provider_api_key_instance = CreatedExternalProviderApiKey.from_json(json)
# print the JSON string representation of the object
print CreatedExternalProviderApiKey.to_json()

# convert the object into a dict
created_external_provider_api_key_dict = created_external_provider_api_key_instance.to_dict()
# create an instance of CreatedExternalProviderApiKey from a dict
created_external_provider_api_key_form_dict = created_external_provider_api_key.from_dict(created_external_provider_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


