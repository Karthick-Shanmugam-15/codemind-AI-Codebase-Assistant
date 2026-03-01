## Overview

The `EventObjectHandler` class is designed to handle and process events related to configuration changes in a rule engine environment. It includes methods for converting Pod events into Container events, handling vertex attributes, and managing the configuration records.

## Usage

### Example of Usage:

```java
public class EventExample {

    public static void main(String[] args) {
        // Create a RuleEngine instance
        RuleEngine ruleEngine = new RuleEngine();

        try {
            // Load your rules or events here.
            Map<String, Object> payLoad = loadConfigRecord();
            RuleOutput ruleOutput = new RuleOutput();
            Consumer<Object> consumer = new Consumer<Object>() {
                @Override
                public void accept(Object object) {
                    System.out.println("Processed Output: " + object);
                }
            };

            // Process the event
            EventObjectHandler.execute(ruleEngine.getRuleRunner(), payLoad, ruleOutput, consumer);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static Map<String, Object> loadConfigRecord() throws Exception {
        // Implement your logic to load a configuration record from an external source
        return new HashMap<>();
    }
}
```

### Parameters and Returns

- **Parameters:**

  - `RuleEngine.RuleRunner ruleRunner`: The RuleRunner instance used for executing the rules.
  - `Map<String, Object> payLoad`: A map containing the payload of events or configurations. It includes details such as configuration records (`ConfigEvent`) and other relevant information.
  - `RuleOutput ruleOutput`: An instance where the output is stored after processing.
  - `Consumer<Object> consumer`: A lambda function that receives an object to be processed.

- **Returns:**

  None, but it triggers a method `execute` which handles the event processing with any necessary exception handling.

### Detailed Methods

#### execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer)

The primary entry point that handles the execution of events. This method calls another method to process the specific type of configuration record (`ConfigEvent`) and then stores details in a `RuleOutput` object.

- **Description:** Handles event processing based on the type of `ConfigEvent` present in the payload.
- **Parameters:**
  - `ruleRunner`: The RuleRunner instance used for executing rules. This is typically obtained from an environment setup or configuration management system.
  - `payLoad`: Contains the event record along with other necessary details needed to process it.
- **Returns:** None, but handles execution through another method.

#### processEvent(Map<String, Object> payLoad, ConfigEvent eventRecord, Vertex vertex, Map<String, Object> details)

This method processes events related to vertices. It involves parsing JSON attributes from the current configuration record and updating or setting properties based on a specific type of `ConfigEvent`.

- **Description:** Processes the event by applying transformation rules to determine the new state of vertices.
- **Parameters:**
  - `payLoad`: The map containing the payload with detailed configurations.
  - `eventRecord`: Holds details about the configuration record, including types and fields that need processing.
  - `vertex`: Represents a vertex (node) in the graph where events are processed. This method updates its type according to the event rules.
- **Returns:** None

#### convertPodToContainerEventProcessing(Vertex vertex, JSONObject attributes)

Transforms Pod event records into Container event records by changing the vertex type and setting specific properties like container name based on field paths from the original event.

- **Description:** Converts Pod-related events to Container processing. This involves checking `event_fieldPath` for Kubernetes Pod types and updating the vertex accordingly.
- **Parameters:**
  - `vertex`: The source vertex being processed.
  - `attributes`: A JSON object containing details of the event record.
- **Returns:** None

#### getContainerNameFromEventFieldPath(String eventFieldPath)

Extracts a container name from an event field path string, which could be part of Kubernetes events. It's used in specific conversion scenarios where Pod fields need to be converted into Container format.

- **Description:** Extracts the container name based on field paths found within an event.
- **Parameters:**
  - `eventFieldPath`: The full field path leading to the relevant information needed for processing, such as a Kubernetes event with `{` and `}` fields.
- **Returns:** String (containerName) or null if not found.

### Conclusion

This class provides tools to transform and process configuration events in a rule engine environment, allowing for dynamic adjustments based on specific configurations and rules.