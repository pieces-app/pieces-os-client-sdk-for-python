# TextMatch

Thext Match currently used for sensitive for scales for people, and anything related to text matching.  group: is the entire match subgroup is the inner match within the group.(optional)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**group** | [**TextLocation**](TextLocation.md) |  | 
**subgroup** | [**TextLocation**](TextLocation.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.text_match import TextMatch

# TODO update the JSON string below
json = "{}"
# create an instance of TextMatch from a JSON string
text_match_instance = TextMatch.from_json(json)
# print the JSON string representation of the object
print TextMatch.to_json()

# convert the object into a dict
text_match_dict = text_match_instance.to_dict()
# create an instance of TextMatch from a dict
text_match_from_dict = TextMatch.from_dict(text_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


