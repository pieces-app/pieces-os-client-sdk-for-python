# DescopeUserMetadata

User Metadata from Descope

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**global_id** | **str** |  | 
**vanityname** | **str** | this is the vanityname of the user.(set from their custom CNAME dns record.) ie mark.pieces.cloud where \&quot;mark\&quot; is the vanityname. | [optional] 
**allocation** | [**Auth0UserAllocationMetadata**](Auth0UserAllocationMetadata.md) |  | [optional] 
**open_ai** | [**Auth0OpenAIUserMetadata**](Auth0OpenAIUserMetadata.md) |  | [optional] 
**beta** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 
**descope_id** | **str** |  | 

## Example

```python
from pieces_os_client.models.descope_user_metadata import DescopeUserMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DescopeUserMetadata from a JSON string
descope_user_metadata_instance = DescopeUserMetadata.from_json(json)
# print the JSON string representation of the object
print DescopeUserMetadata.to_json()

# convert the object into a dict
descope_user_metadata_dict = descope_user_metadata_instance.to_dict()
# create an instance of DescopeUserMetadata from a dict
descope_user_metadata_from_dict = DescopeUserMetadata.from_dict(descope_user_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


