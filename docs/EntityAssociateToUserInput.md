# EntityAssociateToUserInput

NOTE: this is an optional body provided within the endpoint. This is the input model for associating an Entity with a User.  This body is currently empty but can be extended in the future with additional metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.entity_associate_to_user_input import EntityAssociateToUserInput

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAssociateToUserInput from a JSON string
entity_associate_to_user_input_instance = EntityAssociateToUserInput.from_json(json)
# print the JSON string representation of the object
print(EntityAssociateToUserInput.to_json())

# convert the object into a dict
entity_associate_to_user_input_dict = entity_associate_to_user_input_instance.to_dict()
# create an instance of EntityAssociateToUserInput from a dict
entity_associate_to_user_input_from_dict = EntityAssociateToUserInput.from_dict(entity_associate_to_user_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


