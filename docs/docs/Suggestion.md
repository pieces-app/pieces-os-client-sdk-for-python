# Suggestion

This is the model return by the connector's suggest endpoint.  Note: assets are the assets that this target was ran against.  distribution is the distribution that we generated from comparing the target to the asset's vectors.(currently uuid(assetid) : value that is the difference between the asset and the target) **could potentially make an additional model here that is an array from most to least relevent.  *** distribution is required but we are currently unable to reflect that with our current dart generation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**reuse** | [**ReuseSuggestion**](ReuseSuggestion.md) |  | 
**save** | [**SaveSuggestion**](SaveSuggestion.md) |  | 
**target** | [**SuggestionTarget**](SuggestionTarget.md) |  | 
**assets** | [**Assets**](Assets.md) |  | 
**distribution** | **Dict[str, float]** |  | [optional] 

## Example

```python
from openapi_client.models.suggestion import Suggestion

# TODO update the JSON string below
json = "{}"
# create an instance of Suggestion from a JSON string
suggestion_instance = Suggestion.from_json(json)
# print the JSON string representation of the object
print Suggestion.to_json()

# convert the object into a dict
suggestion_dict = suggestion_instance.to_dict()
# create an instance of Suggestion from a dict
suggestion_form_dict = suggestion.from_dict(suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


