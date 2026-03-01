## Overview

The `AzureEventNormalizer` class is a component designed to process and normalize events for Azure use cases. It reads an event JSON payload from the input and then parses it using Jackson's DocumentContext, extracting specific configuration details such as tenant ID.

### Usage

```java
// Assuming you have already created an instance of AzureEventNormalizer named 'azureNormalizer'
final RuleRunner ruleRunner = new RuleRunner();
final Map<String, Object> payload = getPayloadFromInput(); // Replace with actual input
final RuleOutput ruleOutput = new RuleOutput();

azureNormalizer.execute(ruleRunner, payload, ruleOutput);
```

### Methods

#### Method: execute(final RuleRunner ruleRunner, final Map<String, Object> payload, final RuleOutput ruleOutput, Consumer<Object> consumer)

This method is the entry point for processing events. It takes a `RuleRunner` instance, a map containing event data, a `RuleOutput`, and a `Consumer` to process the output.

- **Parameters:**
  - `ruleRunner`: An instance of `RuleRunner` that contains configuration details.
  - `payload`: A map containing the event JSON payload.
  - `ruleOutput`: The output object where processed events will be added.
  - `consumer`: A `Consumer` to process any generated ConfigEvent objects.

- **Returns:**
  This method does not return anything but modifies the `RuleOutput` instance by adding ConfigEvents derived from the input event data.

#### Method: updateAttributes(com.opscruise.ruleengine.api.Vertex v, Map<String, Object> attributes)

This protected method is used to update an existing vertex with new attributes based on the given map of attributes and the original vertex. It updates vertices that have an attribute named `VALUE` in their attributes for readability or other processing purposes.

### Example

```java
final String eventJson = "{\"id\": \"event1\", \"tenantId\": \"my_tenant_id\"}";
final Map<String, Object> payload = new HashMap<>();
payload.put(PAYLOAD_EVENT, eventJson);
payload.put(TENANT_ID, "my_tenant_id");

RuleRunner ruleRunner = new RuleRunner();
ruleRunner.getConfigManager().getSectionDetails(COLLECTION_NAMES); // Assuming this method returns a map

AzureEventNormalizer azureNormalizer = new AzureEventNormalizer();

azureNormalizer.execute(ruleRunner, payload, ruleOutput);
```

In the example above:
- An event JSON string is created and stored in the payload.
- A `RuleRunner` instance is instantiated to handle configuration details.
- The `execute` method processes the events, extracting tenant ID from the payload for use in subsequent processing.

This setup can be further extended with additional configurations or custom logic as needed.