# EndpointTargetsContainerRule

### Overview

The `EndpointTargetsContainerRule` class is designed to handle rules related to finding and updating endpoints associated with container targets. This class is part of a rule engine framework for managing configuration events in a cloud environment.

### Usage

```java
// Example usage:
public void execute(RuleRunner ruleRunner, Map<String, Object> payload) throws Exception {
    EndpointTargetsContainerRule endpointTargetsContainerRule = new EndpointTargetsContainerRule();
    
    // Assuming you have the necessary data from RuleRunner.payload object and others.
    boolean debugEnabled = true;
    String tenantId = (String) payload.get("tenant");
    ConfigEvent configRecord = (ConfigEvent) payload.get("configRecord");

    Output output = configRecord.getOutputs();
    if (output != null && !output.isEmpty()) {
        List<Edges> edgeList = output.getEdges();

        for (Edges edge : edgeList) {
            if (edge.getEdgeType().equals("targets")) {
                // Further processing can be done here based on the type and other parameters.
            }
        }
    }
}
```

### Methods

#### execute(RuleRunner ruleRunner, Map<String, Object> payload, RuleOutput ruleOutput, Consumer<Object> consumer) throws Exception

- **Description**: This method is executed to process rules related to endpoint targets in a configuration event. It takes `RuleRunner` for execution context, `payload` containing all relevant data, and `consumer` which allows post-processing actions.

- **Parameters**:
  - `ruleRunner`: The rule runner object for executing the rule.
  - `payload`: A map containing all necessary information to execute the rule.
  - `ruleOutput`: Output from the previous rule execution that this rule depends on.
  - `consumer`: Allows post-processing of results.

- **Returns**: None by default but can throw an exception if something goes wrong during processing.
  
- **Example**:
```java
// Example usage:
public void execute(RuleRunner ruleRunner, Map<String, Object> payload) throws Exception {
    EndpointTargetsContainerRule endpointTargetsContainerRule = new EndpointTargetsContainerRule();
    
    // Assuming you have the necessary data from RuleRunner.payload object and others.
    boolean debugEnabled = true;
    String tenantId = (String) payload.get("tenant");
    ConfigEvent configRecord = (ConfigEvent) payload.get("configRecord");

    Output output = configRecord.getOutputs();
    if (output != null && !output.isEmpty()) {
        List<Edges> edgeList = output.getEdges();

        for (Edges edge : edgeList) {
            if (edge.getEdgeType().equals("targets")) {
                // Further processing can be done here based on the type and other parameters.
            }
        }
    }
}
```

- **Example Output**:
```java
// This is a simplified example of what might happen when this rule is executed.
if (isDebugEnabled) {
    logger.debug("Rule executed successfully.");
} else {
    logger.info("Rule execution successful.");
}
```