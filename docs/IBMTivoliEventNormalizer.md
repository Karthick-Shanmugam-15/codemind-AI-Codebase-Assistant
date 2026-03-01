## Overview

The `IBMTivoliEventNormalizer` class is designed to parse IBM Tivoli Event data and normalize it according to a specific schema. This class serves as an extension of the `RuleRunner` interface, providing methods to execute rule-based transformations on event payloads.

### Usage

To use this class:

```java
IBMTivoliEventNormalizer normalizer = new IBMTivoliEventNormalizer();
normalizer.execute(ruleRunner, payloadMap, ruleOutput, consumer);
```

### Methods

#### Method: `execute(final RuleRunner ruleRunner, final Map<String, Object> payload, final RuleOutput ruleOutput, Consumer<Object> consumer) throws Exception`
- **Description**: Executes the normalizer logic by parsing the event JSON, creating ConfigEvent objects with their vertices and attributes, establishing edges across entities, and building a rule output.
- **Parameters**:
  - `ruleRunner`: A `RuleRunner` instance that provides necessary configurations for rule execution.
  - `payload`: The input payload containing the IBM Tivoli Event details.
  - `ruleOutput`: The resulting rule output map to be used by other components in the system.
  - `consumer`: A consumer function to handle the results of the normalization process.

- **Returns**: `void`
- **Example**:
```java
Map<String, Object> payload = new HashMap<>();
payload.put(PAYLOAD_EVENT, "{\"event\": \"IBM Tivoli Event Details\"}");
payload.put(TENANT_ID, "tenant123");

IBMTivoliEventNormalizer normalizer = new IBMTivoliEventNormalizer();
normalizer.execute(ruleRunner, payload, ruleOutput, consumer);
```

#### Method: `getOutput(final Vertex v)`
- **Description**: Returns a normalized output format for the given vertex.
- **Parameters**:
  - `v`: The input vertex to be processed.

- **Returns**: `Input Output`
- **Example**:
```java
Vertex v = getVertex();
Output output = normalizer.getOutput(v);
```

#### Method: `updateAttributes(com.opscruise.ruleengine.api.Vertex v, Map<String, Object> attributes)`
- **Description**: Updates the vertex attributes based on provided mappings and original attributes.
- **Parameters**:
  - `v`: The input vertex to be updated.
  - `attributes`: A map containing key-value pairs for updating the vertex.

- **Returns**: `Map<String, Object>`
- **Example**:
```java
Vertex v = new Vertex();
Map<String, Object> originalAttributes = getOriginalAttributes(v);
Map<String, String> updateAttributes = parseUpdateMapping(originalAttributes);
v.updateAttributes(updateAttributes);
```

#### Method: `createConfigEventObject(final RuleRunner ruleRunner, final String tenantId, final Map<String, String> collectionNames, final String kind, final Map<String, Vertex> vertexMap, final Map<String, ConfigEvent> configEventMap, final Map<String, Object> entityDataMap)`
- **Description**: Constructs a `ConfigEvent` object and its associated vertices based on the provided input.
- **Parameters**:
  - `ruleRunner`: A `RuleRunner` instance for rule execution logic.
  - `tenantId`: Tenant ID extracted from the payload.
  - `collectionNames`: Collection names details from the configuration manager.
  - `kind`: Kind of event (IBM Tivoli).
  - `vertexMap`: Map to map vertices to their configurations.
  - `configEventMap`: Map for collecting ConfigEvents.

- **Returns**: `ConfigEvent`
- **Example**:
```java
Map<String, String> entityData = new HashMap<>();
entityData.put("entity", "IBM Tivoli Event Details");
Vertex v = createVertex();
ConfigEvent configEvent = normalizer.createConfigEventObject(ruleRunner, tenantId, collectionNames, kind, vertexMap, configEventMap, entityData);
```

This class is a crucial component in rule-based transformation pipelines designed to process and normalize data from IBM Tivoli Events for further processing or storage.