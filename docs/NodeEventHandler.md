# NodeEventHandler Class

## Overview
The `NodeEventHandler` class is designed to process and handle Kubernetes pod events in a Java application. This class extends the functionality from the `RuleEngine.RuleRunner`, allowing it to interact with various data structures and perform specific operations based on the provided input.

## Usage
### Example 1: Handling Pod Events
```java
Map<String, Object> payLoad = new HashMap<>();
payLoad.put("tenant", tenant);
payLoad.put("configRecord", configEvent);

NodeEventHandler.execute(ruleRunner, payLoad, ruleOutput, consumer);
```

### Example 2: Identifying Event Identifiers
In this example, we assume that the `ConfigEvent` object contains identifiers for a node.
```java
List<String> identifiedIdentifiers = NodeEventHandler.getIdentifiers(configEvent);
logger.info("Node event identifiers: {}", identifiedIdentifiers.toString());
```

## Methods

### execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer)
- **Description**: This method is the entry point for handling a pod event. It processes the given payload to identify and handle the event's details.
- **Parameters**:
  - `ruleRunner`: The `RuleEngine.RuleRunner` instance that provides access to the necessary functionality for executing rules.
  - `payLoad`: A map containing the payload data from which the event details are extracted.
  - `ruleOutput`: An object representing the output of a rule, where events can be stored and processed.
  - `consumer`: A consumer object that can consume the results of the event processing.

- **Returns**: None
- **Example**:
```java
NodeEventHandler.execute(ruleRunner, payLoad, ruleOutput, consumer);
```

### getIdentifiers(ConfigEvent eventRecord)
- **Description**: This method extracts identifiers from a `ConfigEvent` record. It checks if the event has an identifier set in its output and converts it into a list of strings for easier processing.
- **Parameters**:
  - `eventRecord`: The `ConfigEvent` instance containing relevant information about the pod event.

- **Returns**: A `List<String>` containing identifiers from the `ConfigEvent`.

### processNodeEvent(Tenant tenant, ConfigEvent eventRecord, List<String> identifiers)
- **Description**: This method processes node-related events, marking them as terminated if they represent a deletion.
- **Parameters**:
  - `tenant`: The `Tenant` object that contains information about the tenant being managed.
  - `eventRecord`: The `ConfigEvent` instance containing details of the event to be processed.
  - `identifiers`: A list of identifiers extracted from the event record.

- **Returns**: None
- **Example**:
```java
NodeEventHandler.processNodeEvent(tenant, configEvent, identifiers);
```

### Usage Summary

The `NodeEventHandler` class is designed for orchestrating and handling pod events in a Kubernetes environment. It leverages data structures such as maps, lists, and specific rules defined within the application to process event details efficiently.

By implementing methods like `execute`, `getIdentifiers`, and `processNodeEvent`, this class ensures that any pod event can be accurately identified, processed, and acted upon according to predefined rules or configurations.