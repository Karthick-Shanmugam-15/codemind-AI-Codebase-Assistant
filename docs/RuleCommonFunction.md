## RuleCommonFunction Class Documentation

### Overview

The `RuleCommonFunction` class is designed to perform common operations related to rule execution and graph management. This class includes methods for converting identifiers, deleting associated edges based on a specific set of vertices, and handling certain database queries.

### Usage

#### Example 1: Convert Identifiers
```java
import com.example.rules.common.RuleCommonFunction;

List<String> identifiers = List.of("id1=value1", "id2=value2");
List<Map<String, String>> convertedIdentifiers = RuleCommonFunction.convertIdentifier(identifiers);
```

This example converts a list of identifier strings into maps.

#### Example 2: Delete Other App Links
```java
import com.example.rules.common.RuleCommonFunction;
import com.example.database.tenant.Tenant;

Tenant tenant = Tenant.getDefault();
OCVertex appObject = OCVertex.getDefault();

RuleCommonFunction.deleteOtherAppLinks(tenant, appObject, null);
```

This example deletes other application links related to the specified `appObject`.

#### Example 3: Delete Edge
```java
import com.example.rules.common.RuleCommonFunction;
import com.example.database.tenant.Tenant;
import com.example.database.association.OCEdge;

Tenant tenant = Tenant.getDefault();
List<OCEdge> appEdge = DBQueryCacheHandler.getAssociatedEdgesForGivenVertex(tenant, "123");

RuleCommonFunction.deleteEdge(tenant, appEdge, new ArrayList<>());
```

This example deletes an edge from the graph related to a specific vertex.

### Methods

#### convertIdentifier(List<String> identifiers)
- **Description**: Converts a list of identifier strings into maps.
- **Parameters**:
  - `identifiers`: A List of String containing identifiers in the format "id=value".
- **Returns**: Returns a List<Map<String, String>> containing the parsed identifiers.
- **Example**:
```java
List<Map<String, String>> convertedIdentifiers = RuleCommonFunction.convertIdentifier(List.of("id1=value1", "id2=value2"));
```

#### deleteOtherAppLinks(Tenant tenant, OCVertex appObject, OCVertex container)
- **Description**: Deletes other application links related to the specified `appObject`.
- **Parameters**:
  - `tenant`: The Tenant object.
  - `appObject`: An OCVertex representing the target application.
  - `container`: (Optional) An OCVertex representing a container.
- **Throws**:
  - `GraphDBException` if any error occurs during the deletion process.
- **Example**:
```java
RuleCommonFunction.deleteOtherAppLinks(tenant.getDefault(), appObject, null);
```

#### deleteEdge(Tenant tenant, List<OCEdge> appEdge, List<String> vtxIds)
- **Description**: Deletes a specified edge from the graph based on vertex IDs.
- **Parameters**:
  - `tenant`: The Tenant object.
  - `appEdge`: A List of OCEdge representing associated edges in the graph.
  - `vtxIds`: An ArrayList containing vertex IDs to be deleted.
- **Throws**:
  - `GraphDBException` if any error occurs during edge deletion.
- **Example**:
```java
List<OCEdge> appEdges = DBQueryCacheHandler.getAssociatedEdgesForGivenVertex(tenant, "123");
RuleCommonFunction.deleteEdge(tenant.getDefault(), appEdges, new ArrayList<>());
```

This method handles the removal of an edge from a graph based on vertex IDs.