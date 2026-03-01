### Overview

The `DeleteEventRule` class in the **delete-event-sub-rule** project is designed to delete event rules associated with specific types of resources within a Kubernetes environment. This method handles the deletion process for Event Rules that match a given configuration and tenant.

### Usage

To use this class, you would typically call it from an application or service that manages event rules. Here's how you might do it:

```java
// Assuming 'configEvent' is your ConfigEvent object and 'tenant' is your Tenant object
DeleteEventRule configEvent = new DeleteEventRule(configEvent, tenant);
configEvent.deleteEventRule();
```

### Methods

#### Method: `DeleteEventRule(ConfigEvent configEvent, Tenant tenant)`

**Description:** Deletes event rules for a specific configuration and tenant. This method processes the graph edges associated with the specified configuration and applies the necessary logic to terminate or update these edges accordingly.

**Parameters:**

- **configEvent:** A ConfigEvent object that contains information about the configuration being processed.
- **tenant:** The Tenant object, which includes details about the current environment context.

**Returns:**
- This method does not return anything. It performs a series of operations on the graph and database to delete event rules.

```java
DeleteEventRule configEvent = new DeleteEventRule(configEvent, tenant);
configEvent.deleteEventRule();
```

#### Example

```java
// Assuming ConfigEvent and Tenant classes are already defined
ConfigEvent configEvent = new ConfigEvent(); // Populate with your configuration data
Tenant tenant = new Tenant();               // Populate with your tenant information

DeleteEventRule deleteEventRule = new DeleteEventRule(configEvent, tenant);
deleteEventRule.deleteEventRule();
```

### Method: `DeleteEdge(String type, List<String> identifiers, Object properties)`

**Description:** This method deletes an edge from a graph based on its type and identifiers. It checks if the specified edge exists in the database and updates it accordingly.

**Parameters:**

- **type:** The type of edge to be deleted (e.g., "StatefulSet", "Endpoint").
- **identifiers:** A list containing one or more identifiers associated with the edge.
- **properties:** Any additional properties that need to be removed from the edge.

```java
OCVertex vtx = DBQueryCacheHandler.getVertexById(tenant, type, identifiers);
if (vtx != null) {
    vtx.removeProperties(properties.keySet());
}
DBQueryCacheHandler.updateVertexCacheIdentifiers(tenant, vtx);
```

### Method: `deleteEdge(String type, List<String> ids)` and `deleteEdge(OCEdge edge)` and `deleteEdge(String edgeId)` and `deleteEdges(List<OCEdge> edges)`

**Description:** These methods are convenience wrappers around the `DeleteEventRule` method to delete multiple event rules or specific event rules associated with a given type. They handle the necessary graph queries for either deleting all matching rules or individual ones.

**Parameters:**

- **type:** The type of edge or rule to be deleted (e.g., "StatefulSet", "Endpoint").
- **ids:** A list containing identifiers that correspond to the edges.
- **edge:** An instance of OCEdge representing a specific event rule.
- **edges:** A list of OCEdge objects representing multiple rules.

```java
deleteEdge("Endpoint", Arrays.asList("1234567890"));
deleteEdges(Arrays.asList(new OCEdge(), new OCEdge()));
```

### Notes

This class is part of the project to manage Kubernetes event rules and involves working with graph databases (GraphDB) and configuration events. The method handles both single edge deletions and bulk rule deletions based on type and identifiers provided.

#### Dependencies

- **GraphDB**: This method interacts with a Graph Database for querying and updating vertices.
- **AllEnums**: This class provides enums for handling different types of entities, which are used in the logic to map between entity types and statuses.
- **Tenant**: Represents the current environment context (e.g., tenant ID).
- **ConfigEvent**: A configuration event object that contains details about the Kubernetes configuration being processed.

#### Debugging

- The `debugLoggingEnabled` variable is set to false by default. This can be changed in the application properties or overridden with a boolean flag for debugging purposes.
- Logging is used throughout the methods to provide detailed information about errors and progress, which can help in diagnosing issues if something goes wrong.

This class forms an integral part of managing Kubernetes event rules and ensures that the graph data is updated accurately after deleting associated Event Rules.