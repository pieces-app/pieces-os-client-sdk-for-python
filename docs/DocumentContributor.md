# DocumentContributor

A DocumentContributor is a preseeded representation of a Person  This can be used in the case of the browser, or in the IDE  If they are apart of an IDE, we can in the future provide git information (IE add a Git object for their commits)  person: this is most important part which is the email/name xyz

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**classification** | [**Classification**](Classification.md) |  | [optional] 
**value** | [**TransferableString**](TransferableString.md) |  | [optional] 
**person** | [**PersonBasicType**](PersonBasicType.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.document_contributor import DocumentContributor

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentContributor from a JSON string
document_contributor_instance = DocumentContributor.from_json(json)
# print the JSON string representation of the object
print DocumentContributor.to_json()

# convert the object into a dict
document_contributor_dict = document_contributor_instance.to_dict()
# create an instance of DocumentContributor from a dict
document_contributor_from_dict = DocumentContributor.from_dict(document_contributor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


