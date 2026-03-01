# DnsIPMapper

## Overview

The `DnsIPMapper` class is designed to map a metric record's resolved IP address (`dns_resolved_address`) to the FQDN used for querying DNS records (`dns_query_fqdn`). This mapping helps in efficiently storing and retrieving the relationship between an IP address and its corresponding DNS query, which can be useful for various network monitoring or analysis purposes.

## Usage

### How to Use It:

```java
import com.example.DnsIPMapper;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Example usage
        Map<String, Object> metricRecord = new HashMap<>();
        metricRecord.put("metricName", "example_metric");
        metricRecord.put("metricValue", 123.456f);
        
        DnsIPMapper mapper = new DnsIPMapper();
        try {
            mapper.execute(ruleRunner, payLoad, ruleOutput, consumer);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Example

This example demonstrates how to create an instance of `DnsIPMapper` and call the `execute` method:

```java
Map<String, Object> metricRecord = new HashMap<>();
metricRecord.put("metricName", "example_metric");
metricRecord.put("metricValue", 123.456f);

// Create an instance of DnsIPMapper
DnsIPMapper mapper = new DnsIPMapper();

try {
    // Call the execute method with appropriate parameters
    mapper.execute(ruleRunner, payLoad, ruleOutput, consumer);
} catch (Exception e) {
    e.printStackTrace();
}
```

### Methods

#### execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer)

- **Description:** Executes the mapping of metric records' resolved IP addresses to their corresponding FQDNs based on the rules specified in a `RuleEngine`.

- **Parameters:**
  - `ruleRunner`: An instance of `RuleEngine.RuleRunner` used to run the rules.
  - `payLoad`: A map containing the payload for the rule, which includes the metric record details.
  - `ruleOutput`: An object that represents the output from the rule engine, typically containing information about the execution.
  - `consumer`: A consumer function (optional) that can be used to consume any additional data or perform post-processing.

- **Returns:** None

- **Example:**
```java
try {
    mapper.execute(ruleRunner, payLoad, ruleOutput, consumer);
} catch (Exception e) {
    System.err.println("An error occurred while mapping metric records: " + e.getMessage());
}
```

### Method Details:

- `metric`: The metric record to be processed.
- `resolvedAddress`: The resolved IP address from the metric record's payload.
- `queryFqdn`: The FQDN used for querying DNS records.

#### Getters and Setters

```java
public Map<String, Object> getMetric() {
    return this.metric;
}

public void setMetric(Map<String, Object> metric) {
    this.metric = metric;
}
```

This class is designed to be a lightweight utility that simplifies the process of mapping DNS resolution results in network monitoring systems. It provides an efficient way to store and retrieve the relationship between IP addresses and their corresponding DNS queries from metric records.