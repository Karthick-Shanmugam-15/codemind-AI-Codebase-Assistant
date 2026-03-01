## Overview

The `IngesterMetricData` class is designed to manage metric data for ingestion purposes. It wraps a `Types.TimeSeries` object, allowing for easy handling of time series-related functionalities.

### Usage

```java
// Assuming you have a Types.TimeSeries instance named ts
IngesterMetricData ingester = new IngesterMetricData(ts);

// Now you can use the metrics as part of your ingestion process.
```

## Methods

### Methods:

1. **Constructor: `public IngesterMetricData(Types.TimeSeries ts)`**
    - **Description:** The constructor initializes an instance of `IngesterMetricData` with a given `Types.TimeSeries`.
    - **Parameters:**
        - `ts`: A `Types.TimeSeries` object representing the time series data.
    - **Returns:** Returns an instance of `IngesterMetricData`.
    - **Example:**
        ```java
        Types.TimeSeries ts = new Types.TimeSeries(); // Assuming this is initialized elsewhere
        IngesterMetricData ingester = new IngesterMetricData(ts);
        ```

### Summary

The `IngesterMetricData` class is designed to encapsulate time series data, making it easy for developers to manage and use in their ingestion processes. The constructor directly takes a `Types.TimeSeries` object as input, allowing seamless integration with other parts of your application's logic.