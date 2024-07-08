# DocumentContributors

This is a plural representation of the DocumentContributor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[DocumentContributor]**](DocumentContributor.md) |  | 

## Example

```python
from pieces_os_client.models.document_contributors import DocumentContributors

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentContributors from a JSON string
document_contributors_instance = DocumentContributors.from_json(json)
# print the JSON string representation of the object
print DocumentContributors.to_json()

# convert the object into a dict
document_contributors_dict = document_contributors_instance.to_dict()
# create an instance of DocumentContributors from a dict
document_contributors_from_dict = DocumentContributors.from_dict(document_contributors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


