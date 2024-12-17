# IDESelections

Plural model that represent many selections in the browser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[IDESelection]**](IDESelection.md) |  | 

## Example

```python
from pieces_os_client.models.ide_selections import IDESelections

# TODO update the JSON string below
json = "{}"
# create an instance of IDESelections from a JSON string
ide_selections_instance = IDESelections.from_json(json)
# print the JSON string representation of the object
print IDESelections.to_json()

# convert the object into a dict
ide_selections_dict = ide_selections_instance.to_dict()
# create an instance of IDESelections from a dict
ide_selections_from_dict = IDESelections.from_dict(ide_selections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


