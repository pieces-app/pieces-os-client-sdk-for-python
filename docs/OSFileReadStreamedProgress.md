# OSFileReadStreamedProgress

This is a model to return stream progress for a file read.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**ModelDownloadProgressStatusEnum**](ModelDownloadProgressStatusEnum.md) |  | 
**percentage** | **float** | Optionally if the download is in progress you will receive a download percent(from 0-100). | [optional] 
**path** | **str** |  | 
**id** | **str** | This is a generated UUID that represents this current stream in progress(can be used to cancel this in the future) | 
**bytes** | [**TransferableBytes**](TransferableBytes.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.os_file_read_streamed_progress import OSFileReadStreamedProgress

# TODO update the JSON string below
json = "{}"
# create an instance of OSFileReadStreamedProgress from a JSON string
os_file_read_streamed_progress_instance = OSFileReadStreamedProgress.from_json(json)
# print the JSON string representation of the object
print OSFileReadStreamedProgress.to_json()

# convert the object into a dict
os_file_read_streamed_progress_dict = os_file_read_streamed_progress_instance.to_dict()
# create an instance of OSFileReadStreamedProgress from a dict
os_file_read_streamed_progress_form_dict = os_file_read_streamed_progress.from_dict(os_file_read_streamed_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


