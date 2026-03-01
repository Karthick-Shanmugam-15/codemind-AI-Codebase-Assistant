## Overview

The `ChangeAppObjectExporterToContainer` class contains methods responsible for executing a RuleEngine rule to change an Application Object (appObject) into an Exporter. It handles side-car and standalone exporters based on the provided parameters.

## Usage

### Example

```java
Map<String, Object> payLoad = new HashMap<>();
payLoad.put("tenant", tenant);
payLoad.put("metricRecord", metric);

RuleEngine.RuleRunner ruleRunner = RuleEngine.create().setConsumer(new Consumer<Object>() {
    @Override
    public void accept(Object value) throws Exception {
        // Handle the result here
    }
}).run(); // Run the rule

boolean result;
try {
    result = changeAppObjectExporterToContainer.execute(ruleRunner, payLoad, ruleOutput, consumer);
} catch (Exception e) {
    logger.error("Error executing Rule: {}", e.getMessage());
}
```

### Usage Explanation

- **`execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer)`**:
  - This method is responsible for running the `ChangeAppObjectExporterToContainer` Rule. It takes a `RuleRunner`, payload (`Map<String, Object>`), output result (`RuleOutput`), and a `Consumer` as parameters.

- **`executeForSideCarExporters(Map<String, Object> payLoad, Tenant tenant, Metric metric, OCVertex container, OCVertex appObject, Vertex changeVtx, Vertex appVtx, Edge edge, boolean singleFlowDebug, StringBuilder debugString)`**:
  - This method handles the side-car exporter rule execution. It checks if the `container` exists and then executes the deletion of application object links.

- **`executeForStandaloneExporters(Map<String, Object> payLoad, Tenant tenant, Metric metric, OCVertex container, OCVertex appObject, Vertex changeVtx, Vertex appVtx, Edge edge, boolean singleFlowDebug, StringBuilder debugString)`**:
  - This method handles the standalone exporter rule execution. It finds the actual container based on the pod and then deletes application object links.

- **`isPartOfMissingLog(OCVertex exporterContainer)`**:
  - This private method logs a warning when there is no `isPartOf` edge between an Exporter and its Container, indicating that the logic for finding containers might be missing or incorrect.

## Methods

### execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer)
- **Description**: Executes the Rule by calling `executeForSideCarExporters` and `executeForStandaloneExporters`.
- **Parameters**:
  - `RuleRunner`: The object that runs this rule.
  - `payLoad`: A map containing required parameters for executing the rule.
  - `ruleOutput`: Holds the result of execution.
  - `consumer`: Consumer to consume any output from the Rule.

### executeForSideCarExporters(Map<String, Object> payLoad, Tenant tenant, Metric metric, OCVertex container, OCVertex appObject, Vertex changeVtx, Vertex appVtx, Edge edge, boolean singleFlowDebug, StringBuilder debugString)
- **Description**: Executes the rule to find and delete application object links for side-car exporters.
- **Parameters**:
  - `payLoad`: Map containing parameters needed for executing the rule.
  - `tenant`: Tenant object which contains tenant specific information.
  - `metric`: Metric record that specifies what needs to be exported.
  - `container`: The container instance of a K8s pod or VM.
  - `appObject`: Application Object for which links need to be deleted.
  - `changeVtx`, `appVtx`: Vertices representing the Exporter and App object respectively in the graph.
  - `edge`: Edge that connects the Exporter (changeVtx) to the appObject (appVtx).
  - `singleFlowDebug`: Boolean indicating whether single flow execution debugging is enabled.
  - `debugString`: StringBuilder used for tracking side-car specific debug information.

### executeForStandaloneExporters(Map<String, Object> payLoad, Tenant tenant, Metric metric, OCVertex container, OCVertex appObject, Vertex changeVtx, Vertex appVtx, Edge edge, boolean singleFlowDebug, StringBuilder debugString)
- **Description**: Executes the rule to find and delete application object links for standalone exporters.
- **Parameters**:
  - `payLoad`: Map containing parameters needed for executing the rule.
  - `tenant`: Tenant object which contains tenant specific information.
  - `metric`: Metric record that specifies what needs to be exported.
  - `container`: The container instance of a K8s pod or VM.
  - `appObject`: Application Object for which links need to be deleted.
  - `changeVtx`, `appVtx`: Vertices representing the Exporter and App object respectively in the graph.
  - `edge`: Edge that connects the Exporter (changeVtx) to the appObject (appVtx).
  - `singleFlowDebug`: Boolean indicating whether single flow execution debugging is enabled.
  - `debugString`: StringBuilder used for tracking standalone specific debug information.

### isPartOfMissingLog(OCVertex exporterContainer)
- **Description**: Logs a warning message when there is no `isPartOf` edge present between an Exporter and its Container, indicating that the logic might be missing or incorrect.