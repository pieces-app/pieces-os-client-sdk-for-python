# Anchors

This is the plural of Anchor.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an Anchor id. | [optional] 
**iterable** | [**List[Anchor]**](Anchor.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.anchors import Anchors

# TODO update the JSON string below
json = "{}"
# create an instance of Anchors from a JSON string
anchors_instance = Anchors.from_json(json)
# print the JSON string representation of the object
print Anchors.to_json()

# convert the object into a dict
anchors_dict = anchors_instance.to_dict()
# create an instance of Anchors from a dict
anchors_from_dict = Anchors.from_dict(anchors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


