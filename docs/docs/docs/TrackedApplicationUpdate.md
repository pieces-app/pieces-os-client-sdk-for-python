# TrackedApplicationUpdate

This is a model used to track when an Application is Updated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**current** | [**TrackedApplication**](TrackedApplication.md) |  | 
**previous** | [**TrackedApplication**](TrackedApplication.md) |  | [optional] 
**user** | [**TrackedUserProfile**](TrackedUserProfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracked_application_update import TrackedApplicationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedApplicationUpdate from a JSON string
tracked_application_update_instance = TrackedApplicationUpdate.from_json(json)
# print the JSON string representation of the object
print TrackedApplicationUpdate.to_json()

# convert the object into a dict
tracked_application_update_dict = tracked_application_update_instance.to_dict()
# create an instance of TrackedApplicationUpdate from a dict
tracked_application_update_form_dict = tracked_application_update.from_dict(tracked_application_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


