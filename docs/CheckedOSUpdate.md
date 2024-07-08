---
title: CheckedOSUpdate | Python SDK
---

# CheckedOSUpdate

This is the model for the progress of the current update of Pieces os.  /os/update/check/stream && /os/update/check/  we will emit on a progress update  updated: is an optional property that will let us know when the update was checked last.  NOTE: it is reccommended to use the stream instead of pulling. NOTE: lets think about if we want to have a closing(as well as how we want to handle restarts)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**UpdatingStatusEnum**](UpdatingStatusEnum.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**percentage** | **float** | Optionally if the update is in progress you will recieve a download percent(from 0-100). | [optional] 


