## Overview

The `K8sNormalizer` class is designed to normalize data extracted from Kubernetes ConfigMaps and Secret objects. It maps the normalized values back into a `ConfigEvent` object for further processing in your rule engine.

### Usage

The class's primary method, `execute`, takes several parameters:
- `ruleRunner`: An instance of `RuleEngine.RuleRunner`.
- `payLoad`: A map containing the payload to be processed.
- `ruleOutput`: The output map where results will be stored.
- `consumer`: A consumer function that receives results.

The class utilizes various methods for normalization, such as mapping attributes, extracting entity identifiers, and processing edges. It also includes utility functions like `getValueAsString`, `generateCombinations`, and `extractAttributesAsJsonString`.

### Methods

#### Method: `execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer) throws Exception`

- **Description**: The entry point for processing ConfigMaps/Secrets. It maps the payload to the appropriate class and processes it accordingly.
  
```java
public void execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer) throws Exception {
    // implementation...
}
```

#### Method: `normalizeAttributes(Map<String, Object> jsonObject, ConfigEvent configEvent)`

- **Description**: Normalizes the attributes of a Kubernetes resource based on provided patterns and validation rules.

```java
public Map<String, Object> normalizeAttributes(Map<String, Object> jsonObject, ConfigEvent configEvent) {
    // implementation...
}
```

#### Method: `processEntity(Map<String, Object> entity, Map<String, Object> attributesResult, ConfigEvent configEvent)`

- **Description**: Validates and normalizes the entities based on provided configurations.

```java
private Pair<Boolean,Vertex> processEntity(Map<String, Object> entity, Map<String, Object> attributesResult, ConfigEvent configEvent) {
    // implementation...
}
```

#### Method: `processEdges(Map<String, Object> jsonObject, Map<String, Object> attributesResult, ConfigEvent configEvent)`

- **Description**: Processes the edges for a Kubernetes resource based on provided configurations.

```java
private void processEdges(Map<String, Object> jsonObject, Map<String, Object> attributesResult, ConfigEvent configEvent) {
    // implementation...
}
```

#### Method: `getIdentifiers(List<Map<String, Map<String, Object>>> identifiers, Map<String, Object> attributesResult)`

- **Description**: Extracts entity identifiers from a list of identifiers.

```java
private List<Map<String, String>> getIdentifiers(List<Map<String, Map<String, Object>>> identifiers, Map<String, Object> attributesResult) {
    // implementation...
}
```

#### Method: `extractAttributesAsJsonString(Map<String, Object> attributesResult, Map<String, Map<String, Object>> entityAtt)`

- **Description**: Extracts JSON string representation of attributes.

```java
private String extractAttributesAsJsonString(Map<String, Object> attributesResult, Map<String, Map<String, Object>> entityAtt) {
    // implementation...
}
```

#### Method: `getValueAsString(Object value)`

- **Description**: Converts a raw object to its JSON string representation if it is an instance of `Object`.

```java
private String getValueAsString(Object value) {
    // implementation...
}
```

#### Method: `generateCombinations(Map<String, Object> data)`

- **Description**: Generates all possible combinations of keys and values.

```java
private List<Map<String, String>> generateCombinations(Map<String, Object> data) {
    // implementation...
}
```

#### Method: `generateCombinationsRecursively(List<Map<String, String>> combinations, Map<String, String> current, List<List<String>> allValues, List<String> keys, int depth)`
  
- **Description**: Recursively generates combinations for a given key and its values.

```java
private void generateCombinationsRecursively(List<Map<String, String>> combinations, Map<String, String> current, List<List<String>> allValues, List<String> keys, int depth) {
    // implementation...
}
```

#### Method: `getObjectValues(Map<String, Object> attributesResult, Map<String, Map<String, Object>> mapObject, boolean isObject, boolean isIdentifierCall)`
  
- **Description**: Retrieves values based on configurations and identifier calls.

```java
private Map<String, Object> getObjectValues(Map<String, Object> attributesResult, Map<String, Map<String, Object>> mapObject, boolean isObject, boolean isIdentifierCall) {
    // implementation...
}
```

These methods collectively provide a robust solution for normalizing Kubernetes objects extracted from ConfigMaps/Secrets and processing them according to specified rules.