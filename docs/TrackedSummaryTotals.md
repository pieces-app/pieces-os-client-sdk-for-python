# TrackedSummaryTotals

This is the counts of things that users can add.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | **int** |  | 
**tags** | **int** |  | 
**websites** | **int** |  | 
**persons** | **int** |  | 
**sensitives** | **int** |  | 
**shares** | **int** |  | 
**copilot_sends** | **int** |  | 
**copilot_receives** | **int** |  | 
**copilot_sessions** | **int** |  | 
**copilot_conversations** | **int** |  | 
**productivity_score** | **int** |  | 
**searches** | **int** |  | 
**references** | **int** |  | 
**reuses** | **int** |  | 
**anchor_files** | **int** |  | 
**anchor_folders** | **int** |  | 
**isr_reports** | **int** |  | 

## Example

```python
from pieces_os_client.models.tracked_summary_totals import TrackedSummaryTotals

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedSummaryTotals from a JSON string
tracked_summary_totals_instance = TrackedSummaryTotals.from_json(json)
# print the JSON string representation of the object
print TrackedSummaryTotals.to_json()

# convert the object into a dict
tracked_summary_totals_dict = tracked_summary_totals_instance.to_dict()
# create an instance of TrackedSummaryTotals from a dict
tracked_summary_totals_from_dict = TrackedSummaryTotals.from_dict(tracked_summary_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


