# AppSelfLink

## Overview
The `AppSelfLink` class is a crucial component for managing and updating relationships within an application's topology. It is responsible for automatically creating, linking, or deleting connections between applications based on certain rules defined in the application.

### Usage
To use the `AppSelfLink` class effectively, you need to follow these steps:

1. **Set Up Logging**: Ensure that you have proper logging set up to monitor the execution of this method.
2. **Prepare Input Data**: The method expects input data in a specific format:
   - `tenant`: An instance of `Tenant`.
   - `payLoad`: A map containing the necessary metadata for the operation, such as tenant information and metric records.
3. **Specify Output**: The method processes the output data to determine if it needs to create or update application relationships.
4. **Handle Exceptions**: If an exception occurs during execution, appropriate logging should be performed.

### Example

```java
// Sample input structure
Map<String, Object> payLoad = new HashMap<>();
payLoad.put("tenant", tenant);
payLoad.put("metricRecord", metric);

// Setup logging (ensure you have your logger initialized)
AppSelfLink appSelfLink = new AppSelfLink();
appSelfLink.execute(ruleRunner, payLoad, ruleOutput, consumer);
```

### Methods

#### execute(RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer) throws Exception
- **Description**: This method is the entry point for the `AppSelfLink` class. It orchestrates the entire process of creating, updating, or deleting application relationships based on provided rules and input data.
  
  - **Parameters**:
    - `ruleRunner`: The `RuleRunner`, which provides the necessary rule engine functionalities.
    - `payLoad`: A map containing metadata for the operation, such as tenant information and metric records.
    - `ruleOutput`: Provides output from the previous stage of execution.
    - `consumer`: A `Consumer` object that can be used to consume or modify outputs during this process.

  - **Returns**: This method does not return a value but performs operations based on the provided input parameters.
  
  - **Example**:
    ```java
    try {
        appSelfLink.execute(ruleRunner, payLoad, ruleOutput, consumer);
    } catch (Exception e) {
        logger.error("An error occurred while executing the AppSelfLink method: {}", e.getMessage());
    }
    ```

### Methods Detail

1. **execute(RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer)**

   - **Description**: This is the main execution point of the `AppSelfLink` class.
  
   - **Parameters**:
     - `ruleRunner`: The `RuleRunner`, which provides the necessary rule engine functionalities.
     - `payLoad`: A map containing metadata for the operation, such as tenant information and metric records.
     - `ruleOutput`: Provides output from the previous stage of execution.
     - `consumer`: A `Consumer` object that can be used to consume or modify outputs during this process.

   - **Returns**: This method does not return a value but performs operations based on the provided input parameters.

2. **handlePdms(String ip)**
   - This method handles the processing of PDMS (Performance Data Management System) IP addresses. It is part of the logic to handle pods and services.

3. **getEdgeById(Long id)**

   - Retrieves an edge from the graph database by its unique identifier.
  
4. **validatePod(String podName, String namespace, Tenant tenant)**

   - Verifies if a given pod exists in the system based on provided name, namespace, and tenant information.
   - Returns `true` if the pod is valid; otherwise returns false.

5. **deleteOtherAppLinks(Tenant tenant, Vertex appObject, Vertex container)**
  
   - Deletes any other links between the application object and containers that were previously created by this method.

6. **checkIfLinkAlreadyExists(Vertex source, Vertex target)**

   - Checks if a link already exists between two vertices in the graph database.
   - Returns `true` if the link is found; otherwise returns false.

7. **findPod(String identifier, Tenant tenant)**
  
   - Attempts to find a pod by its provided identifier within the system.
   - Returns an instance of `OCVertex` that represents the found pod or null if not found.

8. **getEdgeByNames(List<String> names)**

   - Retrieves an edge from the graph database based on its unique identifiers in the list.

9. **checkIfLinkIsBetweenTwoPods(Vertex source, Vertex target)**

   - Verifies whether a link is between two pods.
   - Returns `true` if there's such a connection; otherwise returns false.

10. **getContainerByIdAndTypes(Tenant tenant, List<String> types, Map<String, String> identifiers)**
  
    - Retrieves a container from the graph database based on provided identifiers and entity types.

### Conclusion
The `AppSelfLink` class is essential for maintaining and updating the application topology by managing relationships between applications. It leverages predefined rules and metadata to ensure that these connections are accurately managed according to established standards.