## README Style Documentation

### Overview

The `AzureMetricDataHandler` class is designed to process and handle data from Azure Metrics. This implementation leverages an external metric mapper repository to normalize the input metrics before processing them.

### Usage

Here's how you can use the `AzureMetricDataHandler` class:

```java
// Initialize with ConfigManager, DBManager, and MetricNormalizeMapperRepo
ConfigManager configMgr = new ConfigManager();
DBManager dbMgr = new DBManager();
MetricNormalizeMapperRepo metricNormalizeMapperRepo = new MetricNormalizeMapperRepo();

// Create an instance of AzureMetricDataHandler
AzureMetricDataHandler azureMetricDataHandler = AzureMetricDataHandler.getInstance();

// Example usage:
// Assuming you have a metric data object in the format: (AzureMetrics) metricData;
List<IngesterMetricData> result = azureMetricDataHandler.processMetric(metricData);
```

### Methods

Here are the methods of `AzureMetricDataHandler` with their descriptions, parameters, and return values:

1. **`init(ConfigManager configMgr, DBManager dbMgr, MetricNormalizeMapperRepo metricNormalizeMapperRepo)`**
   - **Description**: Initializes the AzureMetricDataHandler using provided configurations.
   - **Parameters**:
     - `configMgr`: The configuration manager to use for accessing configuration details.
     - `dbMgr`: The database manager to interact with databases.
     - `metricNormalizeMapperRepo`: The metric mapper repository containing normalization mappings.
   - **Returns**: None
   - **Example**: 
     ```java
     azureMetricDataHandler.init(configMgr, dbMgr, metricNormalizeMapperRepo);
     ```

2. **`getConfigMgr()`**
   - **Description**: Returns the ConfigManager instance used for configuration initialization.
   - **Parameters**:
     - `None`
   - **Returns**: ConfigManager
   - **Example**: 
     ```java
     ConfigManager config = azureMetricDataHandler.getConfigMgr();
     ```

3. **`getInstance()`**
   - **Description**: Returns the singleton instance of AzureMetricDataHandler.
   - **Parameters**:
     - `None`
   - **Returns**: AzureMetricDataHandler
   - **Example**: 
     ```java
     AzureMetricDataHandler azure = AzureMetricDataHandler.getInstance();
     ```

4. **`processMetric(Object metricData)`**
   - **Description**: Processes a single metric data object.
   - **Parameters**:
     - `metricData`: The input metric data in the form of an object.
   - **Returns**: List<IngesterMetricData>
   - **Example**: 
     ```java
     List<IngesterMetricData> ingesters = azureMetricDataHandler.processMetric(metric);
     ```

5. **`processMetricAsync(Object metricData, Consumer<List<IngesterMetricData>> stageOneDataConsumer)`**
   - **Description**: Processes a single metric data object asynchronously.
   - **Parameters**:
     - `metricData`: The input metric data in the form of an object.
     - `stageOneDataConsumer`: A consumer function to process the first batch of ingesters.
   - **Returns**: None
   - **Example**: 
     ```java
     azureMetricDataHandler.processMetricAsync(metric, (data) -> {
         stageOneDataConsumer.accept(data);
     });
     ```

6. **`isAsyncSupported()`**
   - **Description**: Checks if asynchronous processing is supported.
   - **Parameters**:
     - `None`
   - **Returns**: boolean
   - **Example**: 
     ```java
     boolean asyncSupported = azureMetricDataHandler.isAsyncSupported();
     ```

7. **`processAzureMetricsAsync(final AzureMetrics obj, final Consumer<List<IngesterMetricData>> stageOneDataConsumer)`**
   - **Description**: Processes the given Azure Metrics asynchronously.
   - **Parameters**:
     - `obj`: The input AzureMetrics object to process.
     - `stageOneDataConsumer`: A consumer function to handle the first batch of ingesters after asynchronous processing.
   - **Returns**: None
   - **Example**: 
     ```java
     supplyAsync(() -> processAzureMetrics(obj)).whenComplete(
         (s1Data, exception) -> {
             if (exception != null) {
                 LOGGER.error("Error while processing Azure Metrics", exception);
             } else {
                 stageOneDataConsumer.accept(s1Data);
             }
         }
     );
     ```

8. **`processAzureMetrics(final AzureMetrics azureMetrics)`**
   - **Description**: Processes a single AzureMetric object.
   - **Parameters**:
     - `azureMetrics`: The input AzureMetric object to process.
   - **Returns**: List<IngesterMetricData>
   - **Example**: 
     ```java
     List<IngesterMetricData> ingesters = azureMetricDataHandler.processAzureMetrics(azureMetrics);
     ```

9. **`getMetricName(MetricInnerRecord i, String resourceType)`**
   - **Description**: Returns the metric name from a MetricInnerRecord object based on the provided resource type.
   - **Parameters**:
     - `i`: The input MetricInnerRecord object.
     - `resourceType`: The resource type (e.g., "ResourceGroup", "Subscription").
   - **Returns**: String
   - **Example**: 
     ```java
     String metricName = azureMetricDataHandler.getMetricName(i, "ResourceGroup");
     ```

10. **`getSamples(final MetricInnerRecord record, final String aggregationType)`**
    - **Description**: Retrieves the samples for a given metric based on the provided aggregation type.
    - **Parameters**:
      - `record`: The input MetricInnerRecord object.
      - `aggregationType`: The aggregation type (e.g., "count", "maximum").
    - **Returns**: List<Sample>
    - **Example**: 
       ```java
       List<Sample> samples = azureMetricDataHandler.getSamples(i, "maximum");
       ```

11. **`getValueForAggregationType(final MetricValueRecord metricValueRecord, final String aggregationType)`**
   - **Description**: Returns the value for a given aggregation type.
   - **Parameters**:
     - `metricValueRecord`: The input MetricValueRecord object.
     - `aggregationType`: The aggregation type (e.g., "count", "maximum").
   - **Returns**: Double
   - **Example**: 
      ```java
      double value = azureMetricDataHandler.getValueForAggregationType(metricValueRecord, "maximum");
      ```

12. **`getLabels(final MetricInnerRecord metricRecord, final String resourceId, final String resourceType)`**
    - **Description**: Retrieves the labels for a given metric based on the provided resource IDs and type.
   - **Parameters**:
     - `metricRecord`: The input MetricInnerRecord object.
     - `resourceId`: The resource ID (e.g., "resourceName").
     - `resourceType`: The resource type (e.g., "ResourceGroup", "Subscription").
   - **Returns**: Map<String, String>
   - **Example**: 
      ```java
      Map<String, String> labels = azureMetricDataHandler.getLabels(metricRecord, "resourceId", "ResourceGroup");
      ```

13. **`setAzureMetricLabelMapper()`**
    - **Description**: Initializes the Azure metric label mapper by reading configurations from a collection.
   - **Parameters**:
     - `None`
   - **Returns**: None
   - **Example**: 
      ```java
      azureMetricDataHandler.setAzureMetricLabelMapper();
      ```

14. **`getResouceName(String resouceID)`**
    - **Description**: Returns the resource name based on the provided resource ID.
   - **Parameters**:
     - `resouceID`: The input resource ID (e.g., "resourceGroupName").
   - **Returns**: String
   - **Example**: 
      ```java
      String resourceName = azureMetricDataHandler.getResouceName("resourceId");
      ```

### Conclusion

The `AzureMetricDataHandler` class is a crucial component for handling and processing Azure Metrics in an asynchronous manner. It ensures the data is processed efficiently, allowing for optimal performance and scalability.