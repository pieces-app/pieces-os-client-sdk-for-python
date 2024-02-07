# QGPTAgentRoutes

This is apart of the Output and will let the plugin developer know if we reccomend to run specific agent functionality/routes. for instance, related.people, code classification...xyz, for now we start with relatedPeople.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**related** | [**QGPTAgentRelatedRoutes**](QGPTAgentRelatedRoutes.md) |  | [optional] 

## Example

```python
from openapi_client.models.qgpt_agent_routes import QGPTAgentRoutes

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTAgentRoutes from a JSON string
qgpt_agent_routes_instance = QGPTAgentRoutes.from_json(json)
# print the JSON string representation of the object
print QGPTAgentRoutes.to_json()

# convert the object into a dict
qgpt_agent_routes_dict = qgpt_agent_routes_instance.to_dict()
# create an instance of QGPTAgentRoutes from a dict
qgpt_agent_routes_form_dict = qgpt_agent_routes.from_dict(qgpt_agent_routes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


