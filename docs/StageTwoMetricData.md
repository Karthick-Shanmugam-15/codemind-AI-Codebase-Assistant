```markdown

# StageTwoMetricData

## Overview

The `StageTwoMetricData` class is a part of the **Oscruise Metrics** package. It handles the exposure and updating of metrics based on messages and configuration events.

### Methods Summary

- `public JSONObject exposeMetricForMetric(OpscruiseMetricsRegistry registry, Map<String, String> currentMetricHeaders)`: This method updates an exposed metric map with data from a message.
- `public JSONObject exposeMetricForConfigEvent(OpscruiseMetricsRegistry registry, Map<String, String> currentMetricHeaders)`: This method updates an exposed metric map with data from a configuration event.

### Method Details

#### exposeMetricForMetric

```java
public JSONObject exposeMetricForMetric(OpscruiseMetricsRegistry registry, Map<String, String> currentMetricHeaders) {
    // Update the message-specific metrics based on headers and update other metrics accordingly.
}
```

- **Parameters**:
  - `registry`: An instance of `OpscruiseMetricsRegistry`.
  - `currentMetricHeaders`: A map containing headers for updating specific metrics.

- **Returns**: 
  - `JSONObject currentMsgMetricMap` that includes updated message-specific metrics and possibly other metrics.

#### exposeMetricForConfigEvent

```java
public JSONObject exposeMetricForConfigEvent(OpscruiseMetricsRegistry registry, Map<String, String> currentMetricHeaders) {
    // Update the exposed configuration event metrics based on headers.
}
```

- **Parameters**:
  - `registry`: An instance of `OpscruiseMetricsRegistry`.
  - `currentMetricHeaders`: A map containing headers for updating specific metrics.

- **Returns**: 
  - `JSONObject currentMsgConfigMap` that includes updated configuration event-specific metrics and possibly other metrics.
  
## Usage

### Example: Exposing Metrics with a Message Header

```java
OpscruiseMetricsRegistry registry = new OscruiseMetricsRegistry(); // Initialize your registry object
Map<String, String> headers = Map.of("source", "sensor1"); // Define the headers for message exposure

// Update metrics based on current messages and headers
JSONObject updatedMetricMessage = StageTwoMetricData.exposeMetricForMetric(registry, headers);
```

### Example: Exposing Metrics with a Configuration Event Header

```java
OpscruiseMetricsRegistry registry = new OscruiseMetricsRegistry(); // Initialize your registry object
Map<String, String> headers = Map.of("source", "sensor1"); // Define the headers for configuration event exposure

// Update metrics based on current configuration events and headers
JSONObject updatedMetricConfigEvent = StageTwoMetricData.exposeMetricForConfigEvent(registry, headers);
```

### Explanation of Methods

- The `exposeMetricForMetric` method:
  - Updates a metric map with data from a message based on provided headers.
  - Optionally updates other metrics related to the exposed messages.

- The `exposeMetricForConfigEvent` method:
  - Updates an exposure map with data derived from configuration events.
  - This is useful for monitoring and logging specific configurations, often indicating changes or event occurrence.

These methods are crucial for tracking and analyzing the metrics related to messages and configuration events in a system's telemetry. The updates provided help ensure that relevant data about both types of activities is captured accurately for analysis and reporting purposes.
```

### Methods

1. **exposeMetricForMetric**:
   - Parameters: `OpscruiseMetricsRegistry registry`, `Map<String, String> currentMetricHeaders`
   - Returns: `JSONObject currentMsgMetricMap` which includes updated message-specific metrics and possibly other metrics.

2. **exposeMetricForConfigEvent**:
   - Parameters: `OpscruiseMetricsRegistry registry`, `Map<String, String> currentMetricHeaders`
   - Returns: `JSONObject currentMsgConfigEvent` which includes updated configuration event-specific metrics and possibly other metrics.
   
```json
{
  "s2_msgs_in_total": 100,
  "s2_msgs_in_last_timestamp": 54321,
  // Additional metric keys for enriched, none, graph updates...
}
```

These methods help in tracking the number of messages received (`s2_msgs_in_total`), their timestamp (`s2_msgs_in_last_timestamp`), and enriching or not enriching them based on certain conditions (`s2_msgs_in_enriched`, `s2_msgs_in_enriched_none_total`). Additionally, they keep track of graph updates in terms of whether messages are updated (normal) or remain unchanged (`s2_msgs_in_enriched_graph_update`, etc.).