# Ranges

This is a collection of many Ranges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuous** | **bool** |  | [optional] 
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an range id. | [optional] 
**iterable** | [**List[Range]**](Range.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.ranges import Ranges

# TODO update the JSON string below
json = "{}"
# create an instance of Ranges from a JSON string
ranges_instance = Ranges.from_json(json)
# print the JSON string representation of the object
print(Ranges.to_json())

# convert the object into a dict
ranges_dict = ranges_instance.to_dict()
# create an instance of Ranges from a dict
ranges_from_dict = Ranges.from_dict(ranges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


