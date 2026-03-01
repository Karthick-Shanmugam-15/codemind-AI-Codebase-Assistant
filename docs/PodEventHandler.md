## Overview

The `PodEventHandler` class is designed to handle Kubernetes pod events emitted by a rule engine. It parses event details, updates container statuses, and deletes associated edges based on specific conditions.

## Usage

### Example

Here's an example of how you might use the `PodEventHandler`:

```java
import com.example.ruleengine.RuleRunner;
import java.util.Map;
import org.apache.geronimo.configs.ruleservice.RULE_ENGINE_CONFIG;

public class PodHandlerExample {
    public static void main(String[] args) throws Exception {
        // Assuming RuleRunner and other necessary objects are initialized

        Map<String, Object> payLoad = new HashMap<>();
        payLoad.put("configRecord", new ConfigEvent());  // Replace with actual payload
        payLoad.put("tenant", ...);  // Initialize tenant object if needed

        try (RuleEngine.RuleRunner ruleRunner = RuleEngine.create().withConfig(RULE_ENGINE_CONFIG)) {
            ruleRunner.execute(payLoad, RULE_ENGINE_OUTPUT, new PodEventHandler());
        }
    }
}
```

### Dependencies
- Ensure you have the necessary dependencies for Apache Geronimo's `ruleservice` module.
- Include `PodEventHandler` in your classpath.

## Methods

### Method: execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer)
```java
@Override
public void execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer) throws Exception {
    // Implementation of event handling logic here
}
```

#### Parameters:
- `RuleEngine.RuleRunner`: The instance of the rule runner which is responsible for executing rules.
- `Map<String, Object>`: Payload containing the details of the pod event.
- `RuleOutput` (Optional): Rule output from a previous rule execution.
- `Consumer<Object>`: A consumer that can be used to provide feedback or further actions.

#### Returns:
This method does not return any value. It executes the event handling logic and may throw an exception if something goes wrong.

### Method: getVertexEventDetails(Vertex vertex, ConfigEvent eventRecord)
```java
public Pair<AllEnums.EntityStatus, String> getVertexEventDetails(Vertex vertex, ConfigEvent eventRecord) {
    // Implementation of parsing vertex attributes to determine pod status
}
```

#### Parameters:
- `Vertex`: The vertex corresponding to the event record.
- `ConfigEvent` (Optional): Contains details about the pod event.

#### Returns:
A `Pair<AllEnums.EntityStatus, String>` object where "status" is the current entity status of the pod and "statusMessage" is a message associated with it. Null values represent default or unspecified statuses.

### Method: updateContainerDetails(Map<String, Object> payLoad, ConfigEvent eventRecord, Vertex vertex, Pair<AllEnums.EntityStatus, String> eventDetail)
```java
public void updateContainerDetails(Map<String, Object> payLoad, ConfigEvent eventRecord, Vertex vertex, Pair<AllEnums.EntityStatus, String> eventDetail) {
    // Implementation of updating container status and deleting associated edges
}
```

#### Parameters:
- `Map<String, Object>`: The payload containing the rules engine's state.
- `ConfigEvent`: Represents a pod event record from Kubernetes.
- `Vertex` (Optional): A vertex corresponding to the event record.
- `Pair<AllEnums.EntityStatus, String>`: Contains the current status and message for the container.

#### Returns:
This method does not return any value. It performs updates and deletes as defined by the conditions in the event details.