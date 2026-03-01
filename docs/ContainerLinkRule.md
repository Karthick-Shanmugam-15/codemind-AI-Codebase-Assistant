# Overview

The `ContainerLinkRule` class is a part of the Rule Engine framework, designed to execute specific logic based on certain rules. It operates by interacting with a `RuleEngine.RuleRunner`, a `Map<String, Object>` containing required payloads, and a `RuleOutput`. The method signature provided in the code snippet indicates that this class has an overridden `execute` method that processes containers' links from metrics records.

# Usage

To use the `ContainerLinkRule` class:

1. Create instances of relevant classes such as `Tenant`, `Metric`, and others.
2. Populate a `Map<String, Object>` with necessary data, including payloads for various types (e.g., `tenant`, `metricRecord`).
3. Pass these parameters to the `execute` method along with other components required by RuleEngine.

```java
ContainerLinkRule rule = new ContainerLinkRule();
Map<String, Object> payload = new HashMap<>();
payload.put("tenant", tenant);
payload.put("metricRecord", metric);

// Ensure all necessary components are available and correctly set up.
ruleRunner.execute(rule, payload, output, consumer);
```

# Methods

### Method: `execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payload, RuleOutput ruleOutput, Consumer<Object> consumer) throws Exception`

- **Description**: This method processes the execution of a specific rule within the Rule Engine framework. It requires interaction with a `RuleEngine.RuleRunner`, which is used to trigger the logic defined by this rule.
  
- **Parameters**:
  - `ruleRunner`: A `RuleEngine.RuleRunner` instance that serves as the engine for executing rules.
  - `payload`: A `Map<String, Object>` containing data needed to execute the rule. This typically includes key-value pairs representing rule-specific information.
  - `ruleOutput`: The output from the execution of this rule, used for logging or other purposes after it is completed.
  - `consumer`: A consumer that receives an object as input and performs actions on it.

- **Returns**: Not explicitly stated in the method signature but implies a return value expected to be handled by the caller.

- **Example**:

```java
try {
    ruleRunner.execute(rule, payload, output, consumer);
} catch (Exception e) {
    // Handle exceptions during execution.
}
```

### Method: `execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payload, RuleOutput ruleOutput, Consumer<Object> consumer)`
- **Description**: This is the public method that calls the internal `execute` method. It serves as an entry point for external clients to invoke the logic defined by this class.

- **Parameters**:
  - Similar parameters to the internal `execute` method: `ruleRunner`, `payload`, `ruleOutput`, and `consumer`.

- **Returns**: Not explicitly stated but implies a return value or handling of exceptions within the execution process.

### Notes

The provided code snippet is part of an implementation where specific rules, triggered by payloads containing tenant and metric data, perform actions based on certain criteria. The method iterates over edges (representing links from metrics to containers), checking if the target vertex is a container with identifiable IP addresses. If matched, it attempts to resolve the container's details using different methods depending on the failure of direct lookup.

The `execute` method throws an exception when necessary operations fail, ensuring that the execution fails gracefully and properly logs errors.