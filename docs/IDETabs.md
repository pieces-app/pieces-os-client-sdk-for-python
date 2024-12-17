# IDETabs

This is a plural representation of a IDETab

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[IDETab]**](IDETab.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.ide_tabs import IDETabs

# TODO update the JSON string below
json = "{}"
# create an instance of IDETabs from a JSON string
ide_tabs_instance = IDETabs.from_json(json)
# print the JSON string representation of the object
print IDETabs.to_json()

# convert the object into a dict
ide_tabs_dict = ide_tabs_instance.to_dict()
# create an instance of IDETabs from a dict
ide_tabs_from_dict = IDETabs.from_dict(ide_tabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


