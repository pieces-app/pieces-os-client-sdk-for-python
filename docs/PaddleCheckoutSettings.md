# PaddleCheckoutSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**display_mode** | **str** | e.g. &#39;wide-overlay&#39; | 
**theme** | **str** | e.g. &#39;light&#39; or &#39;dark&#39; | 
**locale** | **str** |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_settings import PaddleCheckoutSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutSettings from a JSON string
paddle_checkout_settings_instance = PaddleCheckoutSettings.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutSettings.to_json()

# convert the object into a dict
paddle_checkout_settings_dict = paddle_checkout_settings_instance.to_dict()
# create an instance of PaddleCheckoutSettings from a dict
paddle_checkout_settings_from_dict = PaddleCheckoutSettings.from_dict(paddle_checkout_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


