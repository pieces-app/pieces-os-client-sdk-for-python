# AnchorPoints

This is the plural of AnchorPoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an AnchorPoint id. | [optional] 
**iterable** | [**List[AnchorPoint]**](AnchorPoint.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.anchor_points import AnchorPoints

# TODO update the JSON string below
json = "{}"
# create an instance of AnchorPoints from a JSON string
anchor_points_instance = AnchorPoints.from_json(json)
# print the JSON string representation of the object
print(AnchorPoints.to_json())

# convert the object into a dict
anchor_points_dict = anchor_points_instance.to_dict()
# create an instance of AnchorPoints from a dict
anchor_points_from_dict = AnchorPoints.from_dict(anchor_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


