# SeededDiscoverableRelatedTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | This is the application id that this request is sent from. | 
**iterable** | [**List[SeededDiscoverableRelatedTag]**](SeededDiscoverableRelatedTag.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_discoverable_related_tags import SeededDiscoverableRelatedTags

# TODO update the JSON string below
json = "{}"
# create an instance of SeededDiscoverableRelatedTags from a JSON string
seeded_discoverable_related_tags_instance = SeededDiscoverableRelatedTags.from_json(json)
# print the JSON string representation of the object
print(SeededDiscoverableRelatedTags.to_json())

# convert the object into a dict
seeded_discoverable_related_tags_dict = seeded_discoverable_related_tags_instance.to_dict()
# create an instance of SeededDiscoverableRelatedTags from a dict
seeded_discoverable_related_tags_from_dict = SeededDiscoverableRelatedTags.from_dict(seeded_discoverable_related_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


