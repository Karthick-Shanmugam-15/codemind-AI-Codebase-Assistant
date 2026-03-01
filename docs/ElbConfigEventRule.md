# ElbConfigEventRule Class

## Overview

The `ElbConfigEventRule` class is designed to handle configuration and event rules for a graph-based system. It processes input configurations, events, tenants, and identifies vertices (either ELB or ELBv2) in the graph database based on specific identifiers. The method `applyElbRule` ensures that the appropriate Elb Config or Event Rule is applied to the identified vertex. Additionally, it builds and updates vertex data, pushes edges into the graph cache, and appends relevant output details for Kafka.

## Usage

### How to Use It with Examples

```java
// Example 1: Applying an ElbConfigRule to a Vertex
Map<String, Object> ruleInput = new HashMap<>();
ruleInput.put("configOrEvent", configOrEvent);
ruleInput.put("tenant", tenant);
ruleInput.put("isConfig", Boolean.TRUE);

Map<String, Object> ruleOutput = new HashMap<>();

// Example 2: Applying an ElbConfigRule to a Vertex (Edge Case)
List<Edges> edges = Arrays.asList(edge1, edge2);
Map<String, Object> edgeInput = new HashMap<>();
edgeInput.put("configOrEvent", configOrEvent);
edgeInput.put("tenant", tenant);

for(Edges edge: edges) {
    // Apply Elb Config Rule for each Edge
    applyElbRule(tenant, elbv2Type, edge.getSource());
    applyElbRule(tenant, elbv2Type, edge.getTarget());
}

// Example 3: Constructing and Applying an Event Rule to an Edge
Map<String, Object> ruleInputEdge = new HashMap<>();
ruleInputEdge.put("configOrEvent", configOrEvent);
ruleInputEdge.put("tenant", tenant);

for(Edges edge : edges) {
    applyElbRule(tenant, elbv2Type, edge.getSource());
    applyElbRule(tenant, elbv2Type, edge.getTarget());

    // Construct and Apply Event Rule for Edge
    OCEdge edgeData = ConfigEventIngester.getEdgeBaseDetails(edge, sourceVertexData, targetVertexData);
    List<DBActionResult> graphOutput = StageTwoDBQueryHandler.pushEdge(tenant, edgeData, sourceVertexData, targetVertexData, isConfig, tenant.isK8sEnv());
}
```

## Methods

### method_declaration: execute(Map<String, Object> ruleInput, Map<String, Object> ruleOutput)

```java
public void execute(Map<String, Object> ruleInput, Map<String, Object> ruleOutput) throws Exception {
    // Implementation of the main logic for executing configuration and event rules
}
```

#### Description

This method handles the execution of configuration or event rules based on input parameters. It identifies vertices (either ELB or ELBv2), applies configured Elb Config or Event Rule, builds vertex data, pushes edges into graph cache, and appends relevant output details for Kafka.

#### Parameters

- **ruleInput**: The input map containing the rule configuration, tenant information, event type, etc.
- **ruleOutput**: A map to store the result of the execution process.

#### Returns

The method does not return a value but sets `ruleOutput` as a placeholder indicating successful execution or failure with errors.

### method_declaration: applyElbRule(Tenant tenant, String vtxType, Vertex vertex)

```java
private void applyElbRule(Tenant tenant, String vtxType, Vertex vertex) {
    // Implementation of applying an Elb Config Rule to the specified vertex type and vertex
}
```

#### Description

This method applies a configured Elb Config or Event Rule to a vertex based on specific criteria. It filters out DNSName identifiers from all identifiers, checks for existence of the identified ELB or ELBv2 vertex, and updates its status and description accordingly.

#### Parameters

- **tenant**: The tenant information used to identify vertices.
- **vtxType**: The type of vertex (ELB or ELBv2).
- **vertex**: The vertex to be applied the Elb Config Rule on.

#### Returns

No return value but sets `ruleOutput` as a placeholder indicating successful execution or failure with errors.

### method_declaration: getDNSNameIdentifier(List<String> identifiers)

```java
private List<String> getDNSNameIdentifier(List<String> identifiers) {
    String dnsIdentifier = identifiers.stream()
        .filter(m-> (m.contains("ElbDNSName=") || m.contains("Elbv2DNSName=")))
        .findAny()
        .orElse(null);
    
    List<String> l = new ArrayList(1);
    l.add(dnsIdentifier);

    return l;
}
```

#### Description

This method finds the DNS name identifier from a list of identifiers. It filters out any identifier that matches the format "ElbDNSName=" or "Elbv2DNSName=" and returns it.

#### Parameters

- **identifiers**: A list containing all possible identifiers to be filtered.

#### Returns

A list with only the DNS name identifier found, if present in the input list. Otherwise, it returns `null`.

This documentation serves as a guide for understanding the functionality of the `ElbConfigEventRule` class and how you can use it within your graph-based system architecture.