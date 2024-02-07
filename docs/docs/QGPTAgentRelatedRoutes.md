# QGPTAgentRelatedRoutes

This is specific for all the related materials, like people, tags, websites... xyz

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**people** | **bool** | optional bool, that will say if we reccomend to run related.people on this conversation, IFF set to TRUE. | [optional] 

## Example

```python
from openapi_client.models.qgpt_agent_related_routes import QGPTAgentRelatedRoutes

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTAgentRelatedRoutes from a JSON string
qgpt_agent_related_routes_instance = QGPTAgentRelatedRoutes.from_json(json)
# print the JSON string representation of the object
print QGPTAgentRelatedRoutes.to_json()

# convert the object into a dict
qgpt_agent_related_routes_dict = qgpt_agent_related_routes_instance.to_dict()
# create an instance of QGPTAgentRelatedRoutes from a dict
qgpt_agent_related_routes_form_dict = qgpt_agent_related_routes.from_dict(qgpt_agent_related_routes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


