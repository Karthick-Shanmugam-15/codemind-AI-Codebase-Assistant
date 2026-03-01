## Overview

`ContainerConfigEventHandler` class is designed to handle configuration events related to containers. It processes the event details and converts them into a map for further processing or output.

### Usage

```java
// Example usage of the method:
Map<String, Object> payLoad = new HashMap<>();
payLoad.put("configRecord", configRecord);

ContainerConfigEventHandler.execute(ruleRunner, payLoad, ruleOutput, consumer);
```

### Methods

#### execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer)

- **Description:** Executes the specified rule runner on a map of payload and converts it into an output.
- **Parameters:**
  - `ruleRunner`: The RuleEngine that will be used to execute the rules.
  - `payLoad`: A map containing payload information related to configuration events.
  - `ruleOutput`: An instance representing the output of the rule execution.
  - `consumer`: A consumer object that can process and consume the output.

- **Returns:** None
- **Example:**
```java
Map<String, Object> payLoad = new HashMap<>();
payLoad.put("configRecord", configRecord);

ContainerConfigEventHandler.execute(ruleRunner, payLoad, ruleOutput, consumer);
```

#### getVertexEventDetails(Vertex vertex, Map<String, Object> details, ConfigEvent eventRecord)

- **Description:** Retrieves the attributes of a specified vertex and populates them into the `details` map.
- **Parameters:**
  - `vertex`: The vertex to retrieve its attributes from.
  - `details`: A map where the attributes will be populated.
  - `eventRecord`: The configuration event record containing information needed for parsing.

- **Returns:** None
- **Example:**
```java
getVertexEventDetails(vertex, details, configRecord);
```

#### findAndSetActualVertexTypeAsTarget(ConfigEvent eventRecord, Edges edge, Map<String, Object> payLoad)

- **Description:** Identifies the target vertex based on provided configurations and sets its type as specified.
- **Parameters:**
  - `eventRecord`: The configuration event record to base the target type on.
  - `edge`: An edge representing a connection from one vertex to another.
  - `payLoad`: A map containing tenant information used for querying vertices.

- **Returns:** None
- **Example:**
```java
findAndSetActualVertexTypeAsTarget(eventRecord, edge, payLoad);
```

### Conclusion

The `ContainerConfigEventHandler` class is a crucial component of an event-driven architecture designed to manage and process configuration events related to containers. It leverages predefined rules and patterns to ensure accurate conversion of input payload into meaningful outputs or actions as defined by the handler's logic.