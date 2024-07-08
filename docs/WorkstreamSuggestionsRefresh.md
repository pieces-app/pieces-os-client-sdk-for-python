# WorkstreamSuggestionsRefresh

This will return the new refreshed suggestions, about what data changed, and the data that was used to bias the suggestions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**suggestions** | [**WorkstreamSuggestions**](WorkstreamSuggestions.md) |  | 

## Example

```python
from pieces_os_client.models.workstream_suggestions_refresh import WorkstreamSuggestionsRefresh

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSuggestionsRefresh from a JSON string
workstream_suggestions_refresh_instance = WorkstreamSuggestionsRefresh.from_json(json)
# print the JSON string representation of the object
print WorkstreamSuggestionsRefresh.to_json()

# convert the object into a dict
workstream_suggestions_refresh_dict = workstream_suggestions_refresh_instance.to_dict()
# create an instance of WorkstreamSuggestionsRefresh from a dict
workstream_suggestions_refresh_from_dict = WorkstreamSuggestionsRefresh.from_dict(workstream_suggestions_refresh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


