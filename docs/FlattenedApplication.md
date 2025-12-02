# FlattenedApplication

Flattened version of the Application(for now just the same properties)  VERY important note about `descriptor` (currently used for MCP client names): typically applications are normalized on ApplicationNameEnum. for this property we will be normalized on the ApplicationNameEnum as well as the `descriptor`, so that we can have multiple mcp Applications all with their own specific mcp client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic_unload** | **bool** | This is a proper that will let us know if we will proactivity unload all of your machine learning models.by default this is false. | [optional] 
**capabilities** | [**CapabilitiesEnum**](CapabilitiesEnum.md) |  | [optional] 
**descriptor** | **str** | A descriptor for additional application context. Currently used for MCP client names to identify specific connected MCP clients. | [optional] 
**id** | **str** | The ID of the application at the device level | 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | [optional] 
**name** | [**ApplicationNameEnum**](ApplicationNameEnum.md) |  | 
**onboarded** | **bool** |  | 
**platform** | [**PlatformEnum**](PlatformEnum.md) |  | 
**privacy** | [**PrivacyEnum**](PrivacyEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**version** | **str** | This is the specific version number 0.0.0 | 

## Example

```python
from pieces_os_client.models.flattened_application import FlattenedApplication

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedApplication from a JSON string
flattened_application_instance = FlattenedApplication.from_json(json)
# print the JSON string representation of the object
print(FlattenedApplication.to_json())

# convert the object into a dict
flattened_application_dict = flattened_application_instance.to_dict()
# create an instance of FlattenedApplication from a dict
flattened_application_from_dict = FlattenedApplication.from_dict(flattened_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


