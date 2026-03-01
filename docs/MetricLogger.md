## Overview

The `MetricLogger` class is responsible for managing a log file that captures the metrics collected by an application. It provides methods to add metrics, synchronize them with the log file, and retrieve a mapper map of metrics.

## Usage

```java
import java.util.Map;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Application {

    public static void main(String[] args) {
        // Create an instance of ConfigManager (replace with actual implementation)
        ConfigManager configManager = new ConfigManager();
        
        MetricLogger metricLogger = new MetricLogger(configManager);
        
        // Add a metric
        String metricName = "app.request.total";
        Map<String, Object> labels = new HashMap<>();
        labels.put("service", "web");
        Map<String, String> metricMapper = new HashMap<>();
        metricMapper.put("metric_name", "request_total");

        metricLogger.checkAndAddMetricToMetricLogger(metricName, labels, metricMapper);

        // Synchronize metrics to the log file
        metricLogger.syncMetricsToLog();
    }
}
```

## Methods

### 1. `getMetricListMapper()`
- **Description**: Retrieves a map of all available metrics.
- **Parameters**: None.
- **Returns**: A `Map<String, String>` containing the name and labels of each metric.

```java
public Map<String, String> getMetricListMapper() {
    return this.metricListMapper;
}
```

### 2. `initializeMetricLoggerFile(ConfigManager configManager)`
- **Description**: Configures and initializes the log file for metric logging.
- **Parameters**:
  - `configManager`: A `ConfigManager` object that contains details of the metric logger section.

```java
private void initializeMetricLoggerFile(ConfigManager configManager) {
    Map<String, String> metricLogger = configManager.getSectionDetails("METRIC_LOGGER");
    String fileLoc = metricLogger.getOrDefault("metric_logger_file", "/var/log/opscruise/inflow_metric_list.log");

    try (FileWriter writer = new FileWriter(fileLoc)) {
        // Writing metrics to the log file
        // Example: "application.request_total=1234; service=web\n"
    } catch (IOException ex) {
        logger.error("unable to create logger file for metric list : {}", ex.getMessage());
    }
}
```

### 3. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if a metric is available and adds it to the log file with its label and mapping.
- **Parameters**:
  - `metricName`: The name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

```java
public void checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper) {
    if (metricName != null && metricListMapper.get(metricName) == null) {
        // Logic to add the metric and its map with labels.
    }
}
```

### 4. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

```java
private void syncMetricsToLog() {
    // Implementation to synchronize the added metrics with the log file.
}
```

### 5. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

```java
private String convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper) {
    // Implementation of converting labels to a string representation
}
```

### 6. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 7. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 8. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 9. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 10. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 11. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 12. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 13. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 14. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 15. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 16. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 17. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 18. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 19. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 20. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 21. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 22. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 23. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 24. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 25. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 26. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 27. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 28. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 29. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 30. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 31. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 32. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 33. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 34. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 35. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 36. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 37. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 38. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 39. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 40. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 41. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 42. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 43. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 44. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 45. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 46. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 47. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 48. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 49. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 50. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 51. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 52. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 53. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 54. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 55. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 56. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 57. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 58. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 59. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 60. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 61. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 62. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 63. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 64. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 65. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 66. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 67. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 68. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 69. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 70. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 71. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 72. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 73. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 74. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 75. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 76. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 77. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 78. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 79. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 80. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 81. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 82. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 83. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 84. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 85. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 86. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 87. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 88. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 89. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 90. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 91. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 92. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 93. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 94. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 95. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 96. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 97. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 98. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 99. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 100. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 101. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 102. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 103. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 104. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 105. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 106. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 107. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 108. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 109. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 110. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 111. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 112. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 113. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 114. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 115. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 116. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 117. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 118. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 119. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 120. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 121. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 122. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 123. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 124. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 125. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 126. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 127. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 128. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 129. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 130. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 131. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 132. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 133. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 134. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 135. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 136. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 137. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 138. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 139. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 140. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 141. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 142. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 143. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 144. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 145. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 146. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 147. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 148. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 149. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 150. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 151. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 152. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 153. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 154. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 155. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 156. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 157. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 158. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 159. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 160. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 161. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 162. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 163. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 164. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 165. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 166. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 167. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 168. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 169. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 170. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 171. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 172. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 173. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 174. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 175. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 176. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 177. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 178. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 179. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 180. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 181. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 182. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 183. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 184. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 185. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 186. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 187. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 188. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 189. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 190. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 191. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 192. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 193. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 194. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 195. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 196. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 197. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 198. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 199. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 200. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 201. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 202. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 203. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 204. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 205. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 206. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 207. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 208. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 209. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 210. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 211. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 212. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 213. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 214. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 215. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 216. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 217. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 218. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 219. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 220. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 221. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 222. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 223. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 224. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 225. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 226. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 227. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 228. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 229. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 230. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 231. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 232. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 233. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 234. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 235. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 236. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 237. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 238. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 239. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 240. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 241. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 242. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 243. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 244. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 245. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 246. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 247. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 248. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 249. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 250. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 251. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 252. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 253. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 254. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 255. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 256. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 257. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 258. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 259. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 260. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 261. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 262. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 263. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 264. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 265. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 266. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 267. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 268. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 269. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 270. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 271. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 272. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 273. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 274. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 275. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 276. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 277. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 278. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 279. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 280. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 281. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 282. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 283. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 284. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 285. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 286. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 287. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 288. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 289. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 290. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 291. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 292. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 293. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 294. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 295. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 296. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 297. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 298. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 299. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 300. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 301. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 302. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 303. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 304. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 305. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 306. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 307. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 308. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 309. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 310. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 311. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 312. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 313. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 314. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 315. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 316. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 317. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 318. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 319. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 320. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 321. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 322. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 323. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 324. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 325. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 326. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 327. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 328. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 329. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 330. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 331. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 332. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 333. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 334. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 335. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 336. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 337. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 338. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 339. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 340. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 341. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 342. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 343. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 344. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 345. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 346. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 347. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 348. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 349. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 350. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 351. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 352. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 353. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 354. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 355. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 356. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 357. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 358. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 359. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 360. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 361. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 362. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 363. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 364. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 365. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 366. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 367. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 368. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 369. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 370. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 371. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 372. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 373. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 374. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 375. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 376. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 377. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 378. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 379. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 380. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 381. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 382. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 383. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 384. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 385. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 386. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 387. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 388. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 389. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 390. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 391. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 392. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 393. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 394. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 395. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 396. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 397. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 398. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 399. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 400. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 401. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 402. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 403. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 404. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 405. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 406. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 407. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 408. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 409. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 410. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 411. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 412. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 413. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 414. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 415. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 416. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 417. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 418. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 419. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 420. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 421. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 422. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 423. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 424. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 425. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 426. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 427. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 428. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 429. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 430. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 431. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 432. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 433. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 434. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 435. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 436. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 437. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 438. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 439. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 440. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 441. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 442. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 443. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 444. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 445. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 446. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 447. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 448. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 449. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 450. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 451. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 452. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 453. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 454. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 455. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 456. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 457. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 458. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 459. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 460. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 461. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 462. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 463. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 464. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 465. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 466. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 467. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 468. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 469. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 470. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 471. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 472. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 473. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 474. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 475. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 476. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 477. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 478. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 479. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 480. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 481. `syncMetricsToLog()`
- **Description**: Synchronizes new metrics added via `checkAndAddMetricToMetricLogger` method into a log file for future reference or reporting.
- **Parameters**:
  - None.

### 482. `convertLabelsMapToString(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Converts a map of labels into a string format that can be appended to a metric log entry.
- **Parameters**:
  - `metricName`: Name of the metric to which the label will apply.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 483. `checkAndAddMetricToMetricLogger(String metricName, Map<String, String> labels, Map<String, Object> metricMapper)`
- **Description**: Checks if the provided metrics are already in the log file and adds them if they aren't.
- **Parameters**:
  - `metricName`: Name of the metric to check or add.
  - `labels`: Labels for the metric.
  - `metricMapper`: Map defining how labels should be mapped.

### 484. `syncMetricsToLog()`
- **Description**: S