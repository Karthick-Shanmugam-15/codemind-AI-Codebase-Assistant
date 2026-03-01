## Overview

The `AzureConfigNormalizer` class is designed to normalize and process Azure configuration data for a rule engine. It receives JSON configurations in the payload and converts them into a normalized state before processing further.

### Usage

```java
// Sample usage of the execute method with an example:
final Map<String, Object> payload = new HashMap<>();
payload.put(PAYLOAD_CONFIG, "{ \"configJson\": {\"id\":\"example\",\"type\":\"azure\",\"properties\":{\"tenantId\":\"default\"}}}");
payload.put(TENANT_ID, "123456");

final RuleRunner ruleRunner = ...; // Initialize your RuleRunner instance
final RuleOutput ruleOutput = new RuleOutput(); // Create an instance of the output

// Call the execute method with the RuleRunner, payload, and consumer as arguments:
ruleRunner.execute(new AzureConfigNormalizer(), payload, ruleOutput, consumer);
```

### Methods

#### groupElementsByTypeAndId(Map<String, JSONArray> config)

This private method groups configuration elements based on their types (e.g., `type` field) and IDs. It takes a map of JSON arrays as input and returns a map with grouped elements.

```java
private Map<String, Object> groupElementsByTypeAndId(Map<String, JSONArray> config) {
    Map<String, Object> groupedElement = new HashMap<>();
    for (Map.Entry<String, JSONArray> configEntry : config.entrySet()) {
        if (configEntry != null && configEntry.getValue() instanceof JSONArray) {
            final JSONArray configData = configEntry.getValue();
            for (Object entityData : configData) {
                final Map<String, Object> entityDataMap = (Map<String, Object>) entityData;
                final String id = valueOf(entityDataMap.get(ID)).toLowerCase();
                entityDataMap.put(ID, id);
                groupedElement.put(id, entityDataMap);
            }
        }
    }
    return groupedElement;
}
```

#### execute(final RuleRunner ruleRunner, final Map<String, Object> payload, final RuleOutput ruleOutput, Consumer<Object> consumer) throws Exception

This method is the primary entry point for executing the `AzureConfigNormalizer`. It:
- Extracts the configuration JSON from the payload.
- Parses and normalizes the config data using a document context.
- Maps configurations to entities with keys such as ID and Tenant ID.
- Groups elements by type and ID.
- Builds and processes ConfigEvents based on the grouped, normalized data.

```java
execute(final RuleRunner ruleRunner, final Map<String, Object> payload, final RuleOutput ruleOutput, Consumer<Object> consumer) throws Exception {
    // ... (code omitted for brevity)
}
```

#### updateAttributes(com.opscruise.ruleengine.api.Vertex v, Map<String, Object> attributes)

This method is used to update a Vertex's attributes with new or existing ones.

```java
protected Map<String, Object> updateAttributes(com.opscruise.ruleengine.api.Vertex v, Map<String, Object> attributes) {
    // Implementation of attribute updating goes here...
}
```

### Example

The provided code snippet demonstrates how the `AzureConfigNormalizer` class processes configuration data from Azure. The example usage shows initializing a payload and RuleRunner instance, then executing the normalize method with a consumer.

### Related Classes and Dependencies

- `RuleRunner`: A dependency for handling rule execution logic.
- `ConfigurationManager`: A part of the rule engine that provides detailed section information related to collections like "collections_names".
- `DocumentContext`: The context in which rules are executed, helping manage data transformations during normalization.