# NamespaceDeleteEventRule

This class is designed to handle and execute rules related to namespace delete events, specifically in a rule engine environment. It provides methods for processing specific types of events (delete) that involve deleting namespaces.

## Overview

NamespaceDeleteEventRule handles the deletion event by fetching the tenant information and relevant configuration event details. It then identifies the identifiers associated with the namespace being deleted and performs necessary actions related to container termination if applicable, before updating the vertex status and attributes in the graph database.

### Usage

```java
// Example usage:
namespaceDeleteEventRule.execute(
    ruleRunner,
    payloadMap, // Map containing tenant and configuration event details
    ruleOutput,  // Optional RuleOutput instance
    consumer     // Consumer to handle output
);

```

## Methods

### execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payload, RuleOutput ruleOutput, Consumer<Object> consumer)

This method is the main entry point for executing the event. It processes the provided payload which includes tenant and configuration event details.

- **Parameters:**
  - `ruleRunner`: The RuleEngine instance.
  - `payloadMap`: A map containing tenant (Tenant) and configuration event (ConfigEvent) details.
  - `ruleOutput`: An optional RuleOutput object to handle output.
  - `consumer`: A consumer which can be used to pass back data for further processing.

- **Returns:**
  - `void`
  
- **Throws:**
  - `Exception` if an error occurs during execution.

### namespaceDeletingEventProcessing(Tenant tenant, List<String> identifiers, String namespace)

This method processes the delete event involving namespaces. It first retrieves the vertex associated with the given namespace and then updates its status to indicate deletion by a user.

- **Parameters:**
  - `tenant`: The Tenant object containing information about the current operation.
  - `identifiers`: A list of identifiers for the namespace being deleted.
  - `namespace`: The name of the namespace to be processed.

### containerTerminationProcess(Tenant tenant, OCVertex podVtx)

This method processes a delete event involving pods. It updates the status and attributes of the associated containers (Pods) after deleting them from the database graph.

- **Parameters:**
  - `tenant`: The Tenant object containing information about the current operation.
  - `podVtx`: The OCVertex representing the Pod to be processed.

## Example

```java
namespaceDeleteEventRule.execute(
    ruleRunner,
    payloadMap, // Map containing tenant and configuration event details
    ruleOutput,  // Optional RuleOutput instance
    consumer     // Consumer to handle output
);
```

This method would call `execute` methods on the rule runner with the appropriate parameters.

### Debug Logging

```java
if (debugLoggingEnabled) {
    logger.debug("processing the namespace deleteEvent=====>" + payload.toString());
}
```
The above line of code is used for debugging purposes, logging a message about processing a namespace delete event. This can be useful in tracing events and understanding how the system handles such actions.

### Graph Database Exceptions Handling

```java
try {
    // Your database operation here.
} catch (GraphDBException ex) {
    logger.error("Event - Namespace Killing Process for the given namespace Name :" + namespace);
}
```
The try-catch block is used to handle any errors that occur during graph operations, logging them in case of exceptions.

This class provides a mechanism for handling and executing specific types of events related to deleting namespaces, pods, and their associated containers.