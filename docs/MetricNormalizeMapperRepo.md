# MetricNormalizeMapperRepo

## Overview
This class is designed to normalize and map metrics in a database. It provides methods for retrieving metric data, caching it, and handling common and specific attributes.

## Usage
```java
import com.yourpackage.DBManager; // Ensure this imports the DBManager interface or implementation
import com.yourpackage.ConfigManager;  // Ensure this imports the ConfigManager interface or implementation

// Initialize instances of DBManager and ConfigManager
DBManager dbManager = new DBManagerImpl(); // Replace with your actual implementation
ConfigManager configManager = new ConfigManagerImpl(); // Replace with your actual implementation

// Create an instance of MetricNormalizeMapperRepo
MetricNormalizeMapperRepo repo = new MetricNormalizeMapperRepo(dbManager, configManager);

// Retrieve metric mapper for a specific metric name
Map<String, String> metricMapper = repo.getMetricMapper("your_metric_name");

if (metricMapper != null) {
    // Use the mapped data as needed
} else {
    System.out.println("Metric not found or mapping error.");
}
```

## Methods

### getDbManager()
- **Description**: Returns the `DBManager` instance used to interact with the database.
- **Parameters**: None.
- **Returns**: The `DBManager`.
- **Example**:
  ```java
  DBManager dbManager = repo.getDbManager();
  ```

### getMetricMapper(String metricName)
- **Description**: Retrieves a map containing all attributes of a specific metric, which includes both common and operation-specific ignored traits.
- **Parameters**: A `String` representing the name of the metric.
- **Returns**: A map of strings where keys are attribute names and values are their corresponding data types (e.g., "STRING", "NUMBER").
- **Example**:
  ```java
  Map<String, String> mapper = repo.getMetricMapper("your_metric_name");
  ```

### getCollectionName(ConfigManager configManager)
- **Description**: Returns the name of a collection in the database that stores normalized metric data. This is used to map common ignored attributes across operations.
- **Parameters**: A `ConfigManager` instance containing configuration details.
- **Returns**: The name of the collection as a string.
- **Example**:
  ```java
  String colName = repo.getCollectionName(configManager);
  ```

### getCommonIgnoredTraitsAttributes()
- **Description**: Returns a list of common ignored traits attributes for all operations that use this metric normalization mapping.
- **Parameters**: None.
- **Returns**: A `List<String>` containing the names of the common ignored traits attributes.
- **Example**:
  ```java
  List<String> commonIgnoredTraits = repo.getCommonIgnoredTraitsAttributes();
  ```

### getOperationSpecificIgnoreAttributes()
- **Description**: Returns a map where keys are operation IDs and values are lists of ignored trait attribute names specific to each operation.
- **Parameters**: None.
- **Returns**: A `Map<String, List<String>>` where keys are operation IDs and values are lists of ignored traits attributes for that operation.
- **Example**:
  ```java
  Map<String, List<String>> ignoreAttributes = repo.getOperationSpecificIgnoreAttributes();
  ```

This class provides a structured way to interact with the database using specific configurations and mappings related to metric normalization.