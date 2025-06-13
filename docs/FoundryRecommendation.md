# FoundryRecommendation

This is a model that will let the products know some of our recommendations around Foundry:  for now: will just add a recommendation if the user should even use Foundry or NOT. -- (inference)  inference: IE if we want to recommendation the user to use inference (ie call the model) or not

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**inference** | **bool** | This is a bool that will let the client know if we recommend to use Foundry for inference or not | [optional] 

## Example

```python
from pieces_os_client.models.foundry_recommendation import FoundryRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of FoundryRecommendation from a JSON string
foundry_recommendation_instance = FoundryRecommendation.from_json(json)
# print the JSON string representation of the object
print FoundryRecommendation.to_json()

# convert the object into a dict
foundry_recommendation_dict = foundry_recommendation_instance.to_dict()
# create an instance of FoundryRecommendation from a dict
foundry_recommendation_from_dict = FoundryRecommendation.from_dict(foundry_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


