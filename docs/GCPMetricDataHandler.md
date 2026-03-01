```markdown
# GCPMetricDataHandler Documentation

## Overview

The `GCPMetricDataHandler` class is designed to handle and process Google Cloud Platform (GCP) metrics data. It provides methods for initializing the handler, handling metric ingestion asynchronously, and processing GCP metrics.

## Usage

### Initialization
- **Usage**: 
```java
ConfigManager configMgr = new ConfigManager();
DBManager dbMgr = new DBManager();

GCPMetricDataHandler gcpMetricDataHandler = GCPMetricDataHandler.getInstance();
gcpMetricDataHandler.init(configMgr, dbMgr);
```

### Processing Metrics
- **Example**:
```java
Object metricData = new GcpMetric("compute.googleapis.com/instance/disk/cpu-utilization");
List<IngesterMetricData> ingestedMetrics = gcpMetricDataHandler.processMetric(metricData);

// Async processing
gcpMetricDataHandler.processMetricAsync(metricData, stageOneDataConsumer);
```

### Configuration Management and Database Interaction
- **Methods**:
```java
public static ConfigManager getConfigMgr(){
    return configMgr;
}

public static GCPMetricDataHandler getInstance() {
    return gcpMetricDataHandler;
}
```
```markdown
## Methods

### `init(ConfigManager, DBManager)`
- **Description**: Initializes the handler with the provided configuration and database managers.
- **Parameters**:
  - `configManager`: An instance of `ConfigManager`.
  - `dbManager`: An instance of `DBManager`.

- **Returns**:
  None.

- **Example**:

```java
GCPMetricDataHandler gcpMetricDataHandler = GCPMetricDataHandler.getInstance();
gcpMetricDataHandler.init(configMgr, dbMgr);
```

### `getConfigMgr()`
- **Description**: Returns the current configuration manager.
- **Parameters**:
  None.
  
- **Returns**:
  A reference to the `ConfigManager` instance.

- **Example**:

```java
ConfigManager configMgr = gcpMetricDataHandler.getConfigMgr();
```

### `processMetric(Object metricData)`
- **Description**: Processes a single GCP metric object and returns a list of ingested metrics.
- **Parameters**:
  - `metricData`: A metric data object containing the metrics to be processed.

- **Returns**:
  A list of `IngesterMetricData` objects representing the processed metrics.

- **Example**:

```java
List<IngesterMetricData> ingestedMetrics = gcpMetricDataHandler.processMetric(metricData);
```

### `processMetricAsync(Object metricData, Consumer<List<IngesterMetricData>> stageOneDataConsumer)`
- **Description**: Processes a single GCP metric object asynchronously and forwards the results to the provided consumer.
- **Parameters**:
  - `metricData`: A metric data object containing the metrics to be processed.
  - `stageOneDataConsumer`: A `Consumer` that will receive the initial stage of data from the processing.

- **Returns**:
  None.

- **Example**:

```java
gcpMetricDataHandler.processMetricAsync(metricData, stageOneDataConsumer);
```

### `isAsyncSupported()`
- **Description**: Checks if asynchronous processing is supported.
- **Parameters**:
  None.
  
- **Returns**:
  A boolean indicating whether the handler supports async processing.

- **Example**:

```java
boolean isAsync = gcpMetricDataHandler.isAsyncSupported();
```

### `processGCPMetrics(final GcpMetric gcpMetric)`
- **Description**: Processes a single metric containing metrics for Google Cloud Platform.
- **Parameters**:
  - `gcpMetric`: A metric object with metrics to be processed.

- **Returns**:
  A list of `IngesterMetricData` objects representing the processed metrics.

- **Example**:

```java
List<IngesterMetricData> ingestedMetrics = gcpMetricDataHandler.processGCPMetrics(gcpMetric);
```

### `transformToStage1Data(Map.Entry<String, List<byte[]>> e)`
- **Description**: Converts a map entry containing metric data into an `IngesterMetricData` object.
- **Parameters**:
  - `e`: A map entry with the metric details.

- **Returns**:
  An `IngesterMetricData` instance populated with transformed data from the metric's byte array values.

- **Example**:

```java
List<IngesterMetricData> stageOneData = gcpMetricDataHandler.transformToStage1Data(e);
```

### `addAdditionalDiskIdentifier(final Map<String, String> labels, final Map<String, String> metricIncomingLabels)`
- **Description**: Adds additional disk identifier to the metric labels based on provided resource details.
- **Parameters**:
  - `labels`: A map of labels for the metric.
  - `metricIncomingLabels`: The incoming metric's labels.

- **Returns**:
  None.

- **Example**:

```java
gcpMetricDataHandler.addAdditionalDiskIdentifier(labels, metricIncomingLabels);
```

### `getSampleValue(int vType, Point p)`
- **Description**: Converts a time series point into an appropriate sample value.
- **Parameters**:
  - `vType`: The type of the value to be converted (e.g., boolean, int, double).
  - `p`: A point representing the data.

- **Returns**:
  An appropriately cast or zeroed value based on the input types and provided conditions.

- **Example**:

```java
double sampleValue = gcpMetricDataHandler.getSampleValue(1, p);
```

### `getLabels(final TimeSeries ts, final String resourceId, final String resourceType)`
- **Description**: Extracts labels for a metric from its time series data.
- **Parameters**:
  - `ts`: The time series representing the metric's values.
  - `resourceId`, `resourceType`: Details of the resource.

- **Returns**:
  A map containing the extracted labels, or an empty map in case of failure or missing key.

- **Example**:

```java
Map<String, String> labels = gcpMetricDataHandler.getLabels(ts, resourceId, resourceType);
```

### `getMetricName(final String metricPrefix, final TimeSeries timeSeries)`
- **Description**: Extracts the full metric name from a given metric prefix and its type.
- **Parameters**:
  - `metricPrefix`: A part of the metric's type.
  - `timeSeries`: The complete time series entry.

- **Returns**:
  A string representing the fully qualified metric name.

- **Example**:

```java
String metricName = gcpMetricDataHandler.getMetricName("compute.googleapis.com/instance/disk", timeSeries);
```

### `getMetricPrefix(final TimeSeries timeSeries)`
- **Description**: Extracts the full metric prefix from a given type.
- **Parameters**:
  - `timeSeries`: The complete time series entry.

- **Returns**:
  A string representing the fully qualified metric name, or empty if not found.

- **Example**:

```java
String metricPrefix = gcpMetricDataHandler.getMetricPrefix(timeSeries);
```

### `setGCPMetricLabelMapper()`
- **Description**: Configures mappings for GCP metrics labels.
- **Parameters**:
  None.
  
- **Returns**:
  None.

- **Example**:

```java
gcpMetricDataHandler.setGCPMetricLabelMapper();
```
```markdown
## Conclusion

`GCPMetricDataHandler` is designed to handle and process data from Google Cloud Platform metrics efficiently. It provides methods for initializing the handler, handling metric ingestion asynchronously, and processing specific types of GCP metrics such as disk usage. The class also includes utility methods for additional label mapping and extraction, making it a comprehensive solution for integrating with cloud-based monitoring systems.
```