# SeededWorkstreamSuggestionsRefresh

This is used in the input of the /workstream/feed/refresh  The application here will let us know if what scope you would like to refresh the stream for. IE an Application will  provide bias in the items that are displayed.  note: context can be used here to provide further bias to the suggestions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | 
**context** | [**WorkstreamEventContext**](WorkstreamEventContext.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_workstream_suggestions_refresh import SeededWorkstreamSuggestionsRefresh

# TODO update the JSON string below
json = "{}"
# create an instance of SeededWorkstreamSuggestionsRefresh from a JSON string
seeded_workstream_suggestions_refresh_instance = SeededWorkstreamSuggestionsRefresh.from_json(json)
# print the JSON string representation of the object
print SeededWorkstreamSuggestionsRefresh.to_json()

# convert the object into a dict
seeded_workstream_suggestions_refresh_dict = seeded_workstream_suggestions_refresh_instance.to_dict()
# create an instance of SeededWorkstreamSuggestionsRefresh from a dict
seeded_workstream_suggestions_refresh_form_dict = seeded_workstream_suggestions_refresh.from_dict(seeded_workstream_suggestions_refresh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


