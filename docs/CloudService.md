# CloudService Class

**Overview**: The `CloudService` class is designed to encapsulate various attributes related to a cloud service identifier. This includes details such as the provider name, service type, geographical region, port number, and other configuration information.

### Usage

The `getAttributesMap()` method fetches the attribute map based on whether it has been forced or not. The optional parameter `isForcedMap` dictates if the map should be built regardless of cache limits. If there is a cache hit, it retrieves attributes from the cache; otherwise, it builds new attributes and returns them.

The `getAttributesMap()` method simply calls `getAttributesMap(Boolean isForcedMap)` and returns its result.

### Methods

#### getAttributesMap()

- **Description**: Retrieves the attributes map for cloud service identifier.
  
  - **Parameters**:
    - `isForcedMap`: A boolean flag indicating whether to force attribute map retrieval or not. Defaults to false if it hasn't been forced yet.
  
- **Returns**: A `Map<String, String>` containing key-value pairs representing various attributes of the cloud service.

#### getAddressAttributes()

- **Description**: Retrieves and returns a list of attribute maps representing addresses for an identifier.

  - **Parameters**:
    None

- **Returns**: A `List<Map<String, String>>` containing maps of attribute fields for identifiers.

#### getIdentifiers()

- **Description**: Returns the service's identifiers as a `List<String>`.

  - **Parameters**:
    None

- **Returns**: A `List<String>` where each entry is a unique identifier associated with the service, region, and port.

#### getIdentifiersReference()

- **Description**: Provides access to the cache used for identifiers. This helps in managing cache entries efficiently by returning a `Cache<Map<String, String>, String>`.
  
  - **Parameters**:
    None

- **Returns**: A reference to the cache that is associated with service identifier.

#### getServiceNameIdentifier()

- **Description**: Returns the name of the service as an attribute. 

  - **Parameters**:
    - `service`: The service being referred.
    - `region`: The region where the service resides.
    - `port`: An optional port number for a specific identifier.

  - **Returns**: A string that represents the service with its unique identifier, either based on the region or a blank space followed by the port. If there's no specified port, it defaults to "Unknown".

#### getIdentifierField()

- **Description**: Constructs a key-value pair from an input string for identifying services.

  - **Parameters**:
    - `service`: The service name.
    - `region`: The region where the service is located (may be blank if not provided).
    - `port`: The port number of the identifier, which might be left blank if unspecified.

  - **Returns**: A string that serves as a key in the map for unique identification purposes. It includes:
    - "service" followed by "(region)" if region is supplied.
    - "service" followed by the port number if it's provided and not blank (for example, "service123").
    - "Unknown" if neither service name nor specific identifier details are available.

#### getNewIdentifierCache()

- **Description**: Creates a new cache for identifiers. This method ensures that there’s no more than 1000 entries in the cache to avoid any data overflow issues.
  
  - **Parameters**:
    - `service`: The service being referred.
    - `region`: The region where the service is located.

- **Returns**: A `Cache<Map<String, String>, String>` that serves as a reference point for all identifiers related to the specified service and region.

#### getServiceIdentifier()

- **Description**: Creates an internal map of identifiers keyed by the provided service name.
  
  - **Parameters**:
    - `service`: The service being referred.

  - **Returns**: A `HashMap<String, String>` that provides a unique key for each service identifier.

#### getServiceIdentifierAsString()

- **Description**: Constructs a string representation using an internal hash map of identifiers. This is used for logging purposes and to generate human-readable keys.
  
  - **Parameters**:
    - `service`: The service being referred.
    - `region`: The region where the service is located (may be blank if not provided).
  
  - **Returns**: A string that represents the service with its unique identifier, either based on the region or a blank space followed by the port. If there's no specified port, it defaults to "Unknown".

#### getIdentifierField()

- **Description**: Constructs an attribute field key from input strings for identifying services.

  - **Parameters**:
    - `service`: The service name.
    - `region`: The region where the service is located (may be blank if not provided).
  
  - **Returns**: A string that serves as a key in the map for unique identification purposes. It includes:
    - "service" followed by "(region)" if region is supplied.
    - "service" followed by the port number if it's provided and not blank.

#### getNewIdentifierCache()

- **Description**: Creates an instance of `MapCache<String, String>` to manage entries in a cache for identifiers. This method ensures that there are no more than 1000 entries in the cache to prevent data overflow issues.
  
  - **Parameters**:
    None

- **Returns**: A reference point (as a Map) for all identifiers related to the specified service and region.

### Example Usage

```java
CloudService cloudService = new CloudService();
Map<String, String> attributesMap = cloudService.getAttributesMap(true); // Forces attribute map retrieval.
List<Map<String, String>> addresses = cloudService.getAddressAttributes();   // Retrieves address details for identifiers.
List<String> identifiers = cloudService.getIdentifiers();                   // Fetches identifiers associated with a service.
Cache<Map<String, String>, String> identifierCache = cloudService.getIdentifiersReference();
String newIdentifierCacheKey = cloudService.getNewIdentifierCache("serviceA", "regionB"); // Creates a cache for the specified service and region.

// Using getServiceNameIdentifier method:
String serviceName = cloudService.getServiceNameIdentifier();
```

### Limitations

- The `getAttributesMap` method ensures that only up to 1000 entries are kept in the identifier cache.
- For large datasets, consider implementing additional logic or services to manage identifiers effectively.