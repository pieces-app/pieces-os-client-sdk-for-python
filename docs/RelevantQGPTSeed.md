# RelevantQGPTSeed

This is a generic model used, to wrap a seed, as well as give an identifier used to further identifiy this snippet.  Seed is optional here because you may just want to provide the id, and not the original seed.  id is also optional here as you may provide an id or not here.(however with specific endpoint this ID is a guarentee.)  location:(optional) if a path or an anchor is passed in, this will let us know the specific location within the 'file' that this relevant seed is located           note: if this is null and a path/anchor is present then we will use the entire file that is provided.(this logic will be determined within the relevance flow & not by the user)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | [**ReferencedAnchor**](ReferencedAnchor.md) |  | [optional] 
**asset** | [**ReferencedAsset**](ReferencedAsset.md) |  | [optional] 
**id** | **str** |  | [optional] 
**location** | [**TextLocation**](TextLocation.md) |  | [optional] 
**path** | **str** | This is an optional file path | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**seed** | [**Seed**](Seed.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.relevant_qgpt_seed import RelevantQGPTSeed

# TODO update the JSON string below
json = "{}"
# create an instance of RelevantQGPTSeed from a JSON string
relevant_qgpt_seed_instance = RelevantQGPTSeed.from_json(json)
# print the JSON string representation of the object
print(RelevantQGPTSeed.to_json())

# convert the object into a dict
relevant_qgpt_seed_dict = relevant_qgpt_seed_instance.to_dict()
# create an instance of RelevantQGPTSeed from a dict
relevant_qgpt_seed_from_dict = RelevantQGPTSeed.from_dict(relevant_qgpt_seed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


