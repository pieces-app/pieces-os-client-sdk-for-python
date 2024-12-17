# DiscoveredSensitives



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** |  | 
**iterable** | [**List[DiscoveredSensitive]**](DiscoveredSensitive.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.discovered_sensitives import DiscoveredSensitives

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveredSensitives from a JSON string
discovered_sensitives_instance = DiscoveredSensitives.from_json(json)
# print the JSON string representation of the object
print DiscoveredSensitives.to_json()

# convert the object into a dict
discovered_sensitives_dict = discovered_sensitives_instance.to_dict()
# create an instance of DiscoveredSensitives from a dict
discovered_sensitives_from_dict = DiscoveredSensitives.from_dict(discovered_sensitives_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


