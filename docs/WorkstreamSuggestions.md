# WorkstreamSuggestions

This is a list of the materials used in the workstream suggestions.  The feed will return a list of individual material that will be required to be fetched and re-referenced.(the materials that is.)  Considering if we want to have all the materaials just being referenced( ie ReferencedWebsite/ReferencedWorkstreamSummary/...xyz) && rebuilt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[WorkstreamSuggestion]**](WorkstreamSuggestion.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**types** | [**List[WorkstreamSuggestionType]**](WorkstreamSuggestionType.md) | This is iterable &lt;WorkstreamSuggestionType&gt;[] that gives the type of each of the items in the iterable. I.E. types[0] is the suggestion type of the item at iterable[0]. | [optional] 

## Example

```python
from pieces_os_client.models.workstream_suggestions import WorkstreamSuggestions

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSuggestions from a JSON string
workstream_suggestions_instance = WorkstreamSuggestions.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSuggestions.to_json())

# convert the object into a dict
workstream_suggestions_dict = workstream_suggestions_instance.to_dict()
# create an instance of WorkstreamSuggestions from a dict
workstream_suggestions_from_dict = WorkstreamSuggestions.from_dict(workstream_suggestions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


