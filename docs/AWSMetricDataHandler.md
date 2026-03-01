## README Style Documentation

### Overview

The `AWSMetricDataHandler` class is designed to handle and process AWS Metrics data. It is part of a larger system for ingesting and managing metric records, particularly focusing on ingesting AWS metrics.

### Usage

To use the `AWSMetricDataHandler`, you need to instantiate it with your configuration manager and database manager:

```java
ConfigManager configManager = new ConfigManager();
DBManager dbManager = new DBManager();

AWSMetricDataHandler awsMetricDataHandler = new AWSMetricDataHandler(configManager, dbManager);
```

Once instantiated, the `getInstance()` method can be called to obtain an instance of the handler.

### Methods

1. **`init(ConfigManager configManager, DBManager dbManager)`**
   - This method initializes the system by setting up references for configuration and database management.
   
2. **`getInstance()`**
   - Returns the singleton instance of `AWSMetricDataHandler`.

3. **`processMetric(Object metricData)`**
   - Processes AWS Metrics by extracting relevant data from incoming records.

4. **`processMetricAsync(Object metricData, Consumer<List<IngesterMetricData>> stageOneDataConsumer)`**
   - Processes AWS Metrics asynchronously, consuming the result of the processing and passing it to a specified consumer.

5. **`isAsyncSupported()`**
   - Determines if asynchronous processing is supported by checking configuration settings or database mappings.

6. **`processAWSMetricAsync(final mainrecord metricData, final Consumer<List<IngesterMetricData>> s1DataConsumer)`**
   - Asynchronously processes AWS Metrics and forwards the processed data to a consumer for further processing.

7. **`processAWSMetric(mainrecord obj)`**
   - Processes incoming metrics by parsing JSON strings into ingester objects.
   
8. **`constructMetricLabels(LinkedHashMap metricMap)`**
   - Constructs labels from a given map, which are used as metadata in the ingested data.

9. **`constructMetricSamples(LinkedHashMap metricMap)`**
   - Converts timestamps and values extracted from AWS metrics to Sample records that can be added to ingester objects.

10. **`sortTsByTimestamp(List<Sample> s)`**
    - Sorts a list of Samples based on timestamp, which is often required for certain processing pipelines or analytics.

11. **`deriveRegionFromAvailabilityZone(String s)`**
    - Determines the region associated with an AWS availability zone by removing non-region-specific suffixes from the string.

12. **`setAWSMetricLabelMapper()`**
    - Sets up a mapping between product-subtype pairs and their label keys, which are used to populate metric labels in ingester objects.

### Examples

```java
// Example usage with an object containing AWS Metric data:
mainrecord obj = new mainrecord();
obj.setProdType(new ProdType("metric", "aws"));
obj.setObject(readFromDataSource(...));
List<IngesterMetricData> stageOneDataList;
stageOneDataList = awsMetricDataHandler.processMetric(obj);

// Async processing example
final List<IngesterMetricData> asyncStageOneDataList;
asyncStageOneDataList = awsMetricDataHandler.processAWSMetricAsync(obj, new Consumer<List<IngesterMetricData>>() {
    @Override
    public void accept(List<IngesterMetricData> ingesterMetricDataList) {
        // Handle the processed data here
    }
});
```

This class provides a robust solution for managing and processing AWS metric records in a system where ingestion from diverse sources, such as databases or external APIs, is essential.