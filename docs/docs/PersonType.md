# PersonType

basic or platform is absolutely required here. basic: if provided is just information that has been either extracted from the piece or other wise added here. platform: is a real Pieces User.(this user will also exist within the user's users collection. && if not then we will just use the data we have.)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**basic** | [**PersonBasicType**](PersonBasicType.md) |  | [optional] 
**platform** | [**UserProfile**](UserProfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.person_type import PersonType

# TODO update the JSON string below
json = "{}"
# create an instance of PersonType from a JSON string
person_type_instance = PersonType.from_json(json)
# print the JSON string representation of the object
print PersonType.to_json()

# convert the object into a dict
person_type_dict = person_type_instance.to_dict()
# create an instance of PersonType from a dict
person_type_form_dict = person_type.from_dict(person_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


