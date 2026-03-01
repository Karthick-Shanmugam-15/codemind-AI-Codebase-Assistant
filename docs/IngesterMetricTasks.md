### Overview

The `IngesterMetricTasks` class is a part of a data processing system designed to handle ingestion metrics for ingesters. It manages the accumulation and updating of various metric-related fields in ingesters based on their input data.

### Usage

This class provides methods to populate specific metrics based on certain conditions related to whether an Ingester's metric has been enriched or not, as well as updates for grouped metric tasks depending on edge vs vertex type of ingested information.

#### Example

```java
IngesterMetricData ingesterData = new IngesterMetricData();
StageTwoMetricData metricData = new StageTwoMetricData();

populateGroupedMetricTasks(ingesterData);
```

### Methods

1. **Method: `populateMetricForMetric(IngesterMetricData ingesterData, StageTwoMetricData metricData)`**
    - **Description:** This method populates specific fields of a given `StageTwoMetricData` based on the enriched status of an Ingester's metric.
    - **Parameters:**
      1. `ingesterData`: An instance of `IngesterMetricData`.
      2. `metricData`: An instance of `StageTwoMetricData`.
    - **Returns:** None
    - **Example:**
      ```java
      populateMetricForMetric(ingesterData, metricData);
      ```

2. **Method: `populateGroupedMetricTasks(IngesterMetricData s2)`**
    - **Description:** This method populates either edge or vertex related metric tasks based on the ingested data type and whether the Ingester's metric has been enriched.
    - **Parameters:**
      1. `s2`: An instance of `IngesterMetricData`.
    - **Returns:** None
    - **Example:**
      ```java
      populateGroupedMetricTasks(s2);
      ```

### Methods

3. **Method: `populateEdgeTask()`**
   - **Description:** This method adds a task to the list of edge tasks that will update based on specific conditions.
   - **Parameters:**
     None
   - **Returns:** None
   - **Example:**
     ```java
     this.getEdgeTask().add(task);
     ```

4. **Method: `populateVertexTask()`**
   - **Description:** This method adds a task to the list of vertex tasks that will update based on specific conditions.
   - **Parameters:**
     None
   - **Returns:** None
   - **Example:**
     ```java
     this.getVertexTask().add(task);
     ```

5. **Method: `populateEdgeRuleTask()`**
   - **Description:** This method adds a task to the list of edge rule tasks that will update based on specific conditions.
   - **Parameters:**
     None
   - **Returns:** None
   - **Example:**
     ```java
     this.getEdgeRuleTask().add(task);
     ```

6. **Method: `populateVertexRuleTask()`**
   - **Description:** This method adds a task to the list of vertex rule tasks that will update based on specific conditions.
   - **Parameters:**
     None
   - **Returns:** None
   - **Example:**
     ```java
     this.getVertexRuleTask().add(task);
     ```

7. **Method: `populateEdgeNonRuleTask()`**
   - **Description:** This method adds a task to the list of edge non-rule tasks that will update based on specific conditions.
   - **Parameters:**
     None
   - **Returns:** None
   - **Example:**
     ```java
     this.getEdgeNonRuleTask().add(task);
     ```

8. **Method: `populateVertexNonRuleTask()`**
   - **Description:** This method adds a task to the list of vertex non-rule tasks that will update based on specific conditions.
   - **Parameters:**
     None
   - **Returns:** None
   - **Example:**
     ```java
     this.getVertexNonRuleTask().add(task);
     ```

This class is crucial for processing ingested data and updating metrics accordingly, ensuring accurate tracking of ingestion activity.