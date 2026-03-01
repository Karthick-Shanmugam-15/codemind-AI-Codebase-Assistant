## Overview

The `WindowsProcessGroupNormalizer` class is designed to normalize and process metric records for Windows processes. It specifically looks for edges from a "process" type entity to a "process group" type entity, then attempts to find the process name using cached vertex information. This method helps standardize how metrics are presented in a normalized way.

## Usage

### Example
Here's an example of how you might use this class:

```java
// Assuming you have already set up your tenant and metric records:
Tenant tenant = (Tenant) payLoad.get("tenant");
Metric metric = (Metric) payLoad.get("metricRecord");

// Define the process group id list for the specific metric
List<String> idList = Arrays.asList("ip=192.168.1.10,pid=5678"); // Replace with actual values

// Execute the rule and get results back
try {
    WindowsProcessGroupNormalizer norm = new WindowsProcessGroupNormalizer();
    RuleEngine.RuleRunner ruleRunner = new RuleEngine.RuleRunner();
    Map<String, Object> payLoad = null;
    RuleOutput ruleOutput = new RuleOutput();
    Consumer<Object> consumer = (Object x) -> { /* Do something with the output */ };
    norm.execute(ruleRunner, payLoad, ruleOutput, consumer);

    // Access results
    String processName = norm.getProcessName(tenant, idList);
    System.out.println("Normalized process name: " + processName);
} catch (Exception e) {
    e.printStackTrace();
}
```

## Methods

### Method 1: execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer)

**Description**: This method executes the normalization logic for a Windows Process Group Normalizer rule.

- **Parameters**:
  - `ruleRunner`: A RuleEngine instance responsible for executing rules.
  - `payLoad`: A map containing necessary data such as tenant and metric information.
  - `ruleOutput`: An object representing the output of the rule, typically used to store or return results.
  - `consumer`: A consumer that receives outputs from this method.

**Returns**: None

- **Throws**: Exception if an error occurs during execution.

### Method 2: getProcessName(Tenant tenant, List<String> idList)

**Description**: This private method attempts to find the process name based on cached vertex information for a given set of IDs. It uses the `DBQueryCacheHandler` to fetch the process details and returns the name if found.

- **Parameters**:
  - `tenant`: The Tenant object containing context information.
  - `idList`: A list of strings representing identifiers (e.g., host IP, PID).

**Returns**: String — The process name or null if not found.

### Example Usage

The following code snippet demonstrates how to use the `getProcessName` method:

```java
try {
    Tenant tenant = // Get your tenant object...
    List<String> idList = Arrays.asList("ip=192.168.1.10,pid=5678"); // Replace with actual values

    String processName = WindowsProcessGroupNormalizer.getProcessName(tenant, idList);
    System.out.println("Found process name: " + processName);

} catch (Exception e) {
    e.printStackTrace();
}
```

This class is designed to be used within a larger rule engine context where rules need to parse metric records and update them accordingly.