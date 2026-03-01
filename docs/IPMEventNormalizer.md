## Overview

The `IPMEventNormalizer` class is a specialized event normalizer designed to process incoming IPM events. It utilizes the provided configuration manager to extract structured data from JSON payloads and normalize them into specific formats for further processing.

### Usage

```java
public void handleRuleRunner(final RuleRunner ruleRunner, final Map<String, Object> payload) {
    IPMEventNormalizer eventNormalizer = new IPMEventNormalizer();

    try {
        // Assuming 'payload' contains the necessary information to start the normalization process.
        eventNormalizer.execute(ruleRunner, payload);
    } catch (Exception e) {
        logger.error("Error during normalizing event: {}", e.getMessage());
    }
}
```

### Methods

#### Method 1: `execute(final RuleRunner ruleRunner, final Map<String, Object> payload, final RuleOutput ruleOutput, Consumer<Object> consumer)`
- **Description**: Processes the incoming IPM events and normalizes them according to predefined rules. The processed data is then stored in the provided `RuleOutput`.
- **Parameters**:
  - `ruleRunner`: A `RuleRunner` instance which handles all rule operations.
  - `payload`: A map containing all necessary information for event normalization, including payload JSON and tenant ID.
  - `ruleOutput`: An object that captures the output of the rule execution process.
  - `consumer`: A consumer to which the processed data is passed.

- **Returns**: None (the method modifies the `RuleOutput` directly).
  
- **Example**:
```java
Map<String, Object> payload = new HashMap<>();
payload.put(PAYLOAD_EVENT, "event_json_string");
payload.put(TENANT_ID, 12345);

ruleRunner.getOutput();

// Assuming ruleOutput is a valid RuleOutput instance containing the processed event data.
```

#### Method 2: `getOutput(final Vertex v)`
- **Description**: Returns an output object representing the current state of the input vertex in the normalizer process. Useful for debugging or verifying intermediate results.

```java
Output output = IPMEventNormalizer.getOutput(vertex);
System.out.println("Output Data : " + output.toJson());
```

#### Method 3: `updateAttributes(com.opscruise.ruleengine.api.Vertex v, Map<String, Object> attributes)`
- **Description**: Updates the attributes of a vertex based on given input data. This method is used to update the state of a vertex after processing or normalizing events.

```java
IPMEventNormalizer.updateAttributes(vertex, new HashMap<>(attributes));
```

#### Method 4: `createConfigEventObject(final RuleRunner ruleRunner, final String tenantId, final Map<String, String> collectionNames, final String kind, final Map<String, Vertex> vertexMap, final Map<String, ConfigEvent> configEventMap, final Map<String, Object> entityDataMap)`
- **Description**: Builds a configuration event object for IPM events and its vertices based on input data. This method is essential for handling specific configurations in the rule engine.

```java
ConfigEvent configEvent = IPMEventNormalizer.createConfigEventObject(ruleRunner, "tenantId", collectionNames, kind, vertexMap, configEventMap, entityDataMap);
```

### Conclusion

The `IPMEventNormalizer` class is a critical component of the rule engine's ability to process and normalize incoming IPM events. Its methods provide flexible interfaces for event processing, configuration management, and data normalization, making it indispensable for maintaining consistent and accurate rules within complex systems.

```java
// To use this class:
final RuleRunner ruleRunner = new RuleRunner();
final Map<String, Object> payload = new HashMap<>();
payload.put(PAYLOAD_EVENT, "event_json_string");
payload.put(TENANT_ID, 12345);

IPMEventNormalizer eventNormalizer = new IPMEventNormalizer();

try {
    eventNormalizer.execute(ruleRunner, payload);
} catch (Exception e) {
    logger.error("Error during normalizing event: {}", e.getMessage());
}
```