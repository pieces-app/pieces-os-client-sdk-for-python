# SeededPerson

This is a per-cursor to a full person.  Will throw an error, if asset is passed in but acces.scope is undefined.  can optionally pass in our mechanism here, as the default will be manual unless specified.  TODO consider updating these asset, format to referenced Models  Note: model, access, mechanism will only be added if the asset is passed in.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**asset** | **str** |  | [optional] 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | [optional] 
**access** | [**PersonAccess**](PersonAccess.md) |  | [optional] 
**type** | [**PersonType**](PersonType.md) |  | 
**model** | [**PersonModel**](PersonModel.md) |  | [optional] 
**annotations** | [**List[SeededAnnotation]**](SeededAnnotation.md) |  | [optional] 

## Example

```python
from openapi_client.models.seeded_person import SeededPerson

# TODO update the JSON string below
json = "{}"
# create an instance of SeededPerson from a JSON string
seeded_person_instance = SeededPerson.from_json(json)
# print the JSON string representation of the object
print SeededPerson.to_json()

# convert the object into a dict
seeded_person_dict = seeded_person_instance.to_dict()
# create an instance of SeededPerson from a dict
seeded_person_form_dict = seeded_person.from_dict(seeded_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


