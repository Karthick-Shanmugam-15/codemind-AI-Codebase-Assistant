## Overview

The `IstioGWConfigRule` class is designed to extract and populate specific information about the Istio Ingress Gateway container from a tenant's configuration. This class interacts with a database query cache handler to retrieve the necessary vertices related to the tenant and then streams through each edge attached to those vertices, extracting relevant attributes.

## Usage

### Example

```java
RuleRunner ruleRunner = RuleEngine.createRuleRunner();
Map<String, Object> payload = Map.of("tenant", "yourTenantId", "configRecord", yourConfigRecord);
RuleOutput ruleOutput = new RuleOutput(ruleRunner);

Consumer<Object> consumer = output -> System.out.println(output);

IstioGWConfigRule instance = new IstioGWConfigRule();
instance.execute(ruleRunner, payload, ruleOutput, consumer);
```

### Explanation

1. **Payload**: The method receives a `Map<String, Object>` as input:
   - `"tenant"`: Represents the tenant's identifier.
   - `"configRecord"`: Contains configuration records relevant to this application.

2. **`execute()` Method**:
   - This method processes the payload data and retrieves necessary vertices from the database query cache handler based on the provided tenant ID.
   - It then streams through each edge attached to these vertices, extracting specific attributes such as pod IP addresses and container ports.

3. **Attributes Extraction**:
   - For each "container" type edge, it extracts identifiers like "ip".
   - If there are multiple pods associated with the container, it retrieves their port configurations.
   - The extracted information is then mapped to the original payload for further processing or output.

### Error Handling

- **`GraphDBException ex`**: Occurs if no vertex named `istio-ingressgateway` is found in the database query cache handler. This exception helps identify configuration issues related to the tenant's Ingress Gateway.
  
This class effectively simplifies the process of obtaining and populating specific attributes from a tenant's configuration, making it easier for applications to interact with Istio Ingress Gateway information dynamically.