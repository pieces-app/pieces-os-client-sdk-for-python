# Application

A Model to describe what application a format/analytics event originated.  mechanism: This will let us know where this came from. ie.only 2 enums are used here or else throw and error. default mechanism here is MANUAL- meaning that this came from our user Connecting an application. INTERNAL - means that this came from a shareable link

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic_unload** | **bool** | This is a proper that will let us know if we will proactivity unload all of your machine learning models.by default this is false. | [optional] 
**capabilities** | [**CapabilitiesEnum**](CapabilitiesEnum.md) |  | [optional] 
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
from pieces_os_client.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print Application.to_json()

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


