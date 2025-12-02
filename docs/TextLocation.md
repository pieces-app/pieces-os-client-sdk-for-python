# TextLocation

This is a generic model that is used for text location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** | this is the end index within the original string. | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**start** | **int** | this is the start index within the original string. | 
**text** | **str** | this is the value that was found. | 

## Example

```python
from pieces_os_client.models.text_location import TextLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TextLocation from a JSON string
text_location_instance = TextLocation.from_json(json)
# print the JSON string representation of the object
print(TextLocation.to_json())

# convert the object into a dict
text_location_dict = text_location_instance.to_dict()
# create an instance of TextLocation from a dict
text_location_from_dict = TextLocation.from_dict(text_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


