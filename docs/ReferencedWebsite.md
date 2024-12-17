# ReferencedWebsite


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference** | [**FlattenedWebsite**](FlattenedWebsite.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_website import ReferencedWebsite

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedWebsite from a JSON string
referenced_website_instance = ReferencedWebsite.from_json(json)
# print the JSON string representation of the object
print ReferencedWebsite.to_json()

# convert the object into a dict
referenced_website_dict = referenced_website_instance.to_dict()
# create an instance of ReferencedWebsite from a dict
referenced_website_from_dict = ReferencedWebsite.from_dict(referenced_website_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


