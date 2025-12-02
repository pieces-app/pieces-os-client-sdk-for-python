# Entities

A collection of Entity objects representing organizations and teams.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the key is an entity id. | [optional] 
**iterable** | [**List[Entity]**](Entity.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.entities import Entities

# TODO update the JSON string below
json = "{}"
# create an instance of Entities from a JSON string
entities_instance = Entities.from_json(json)
# print the JSON string representation of the object
print(Entities.to_json())

# convert the object into a dict
entities_dict = entities_instance.to_dict()
# create an instance of Entities from a dict
entities_from_dict = Entities.from_dict(entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


