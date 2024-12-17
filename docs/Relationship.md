# Relationship

A relationship expresses a graph of like types, to build a relationship graph.   To get the type of relationship, this is for ie Asset, tag, website, format ...etc, you will need to iterate through the edges and get the root or you can just get the first edge's type as a relationship can only be expressed through same type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**edges** | [**Edges**](Edges.md) |  | 
**embeddings** | [**Embeddings**](Embeddings.md) |  | 
**id** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.relationship import Relationship

# TODO update the JSON string below
json = "{}"
# create an instance of Relationship from a JSON string
relationship_instance = Relationship.from_json(json)
# print the JSON string representation of the object
print Relationship.to_json()

# convert the object into a dict
relationship_dict = relationship_instance.to_dict()
# create an instance of Relationship from a dict
relationship_from_dict = Relationship.from_dict(relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


