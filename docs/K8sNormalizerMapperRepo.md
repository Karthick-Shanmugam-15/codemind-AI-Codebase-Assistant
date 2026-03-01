### Overview

This class provides a mapping repository for Kubernetes objects normalization using the K8sNormalizerMapper interface. It interacts with a database manager to fetch and cache mappings, which can then be accessed through this class.

### Usage

#### Example Usage:

```java
DBManager dbManager = new DBManager(...); // Initialize your database manager here.
ConfigManager configManager = new ConfigManager(...); // Initialize your configuration manager here.

// Get the Kubernetes Normalizer Mapper for a specific type of object.
Map<String, String> mapper = k8sNormalizerMapperRepo.getk8sConfigMapper("Deployment", "Kubernetes");

// Alternatively, you can use it with cache:
mapper = k8sNormalizerMapperRepo.getk8sConfigMapper("Service", "Kubernetes");
mapper = k8sNormalizerMapperRepo.getk8sConfigMapper("ClusterRole", "Kubernetes", "v1");
```

### Methods

#### `getDbManager()`

- **Description**: Returns the database manager instance.
- **Parameters**: None
- **Returns**: A `DBManager` object.
- **Example**:
```java
DBManager dbManager = k8sNormalizerMapperRepo.getDbManager();
logger.info("Database Manager is successfully retrieved.");
```

#### `getCollectionName(ConfigManager configManager)`

- **Description**: Retrieves the collection name for Kubernetes objects normalization from configuration manager. Default returns "config_normalize_mapper".
- **Parameters**: None
- **Returns**: A string representing the collection name.
- **Example**:
```java
String collectionName = k8sNormalizerMapperRepo.getCollectionName(configManager);
logger.info("Collection Name is: {}", collectionName);
```

#### `getk8sConfigMapper(String kind, String productType, String productSubType)`

- **Description**: Fetches and caches the Kubernetes configuration mapper for a specific object type.
- **Parameters**:
  - `kind`: The kind of Kubernetes object (e.g., Deployment, Service).
  - `productType`: The main product type of the Kubernetes object.
  - `productSubType`: An optional sub-type if applicable.
- **Returns**: A map representing the configuration mapper for the specified Kubernetes object.
- **Example**:
```java
Map<String, String> configMapper = k8sNormalizerMapperRepo.getk8sConfigMapper("Deployment", "Kubernetes");
logger.info("Loaded Config Mapper: {}", configMapper);

configMapper = k8sNormalizerMapperRepo.getk8sConfigMapper("Service", "Kubernetes", "LoadBalancer");
logger.info("Loaded Config Mapper for LoadBalancer Service: {}", configMapper);
```

This class is designed to handle Kubernetes object normalization efficiently by caching mappings and providing easy access through a simple API.