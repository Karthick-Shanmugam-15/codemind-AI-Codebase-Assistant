```markdown
# JobIngester Class Documentation

## Overview
The `JobIngester` class is designed to process and trigger jobs based on the job type specified in the input map. It utilizes switch statements to determine which task needs to be executed for each job type, ensuring that only the appropriate method is called.

## Usage

### Example 1: Triggering a Job with Specific Details
```java
Map<String, String> jobDetails = new HashMap<>();
jobDetails.put(JOB_TYPE, "STALE_CONNECTS_TO");
jobDetails.put(ELEMENTS, "vertex1, vertex2");
jobDetails.put(STALE_DURATION, "30");
jobDetails.put(TIME_UNIT, "MINUTES");

triggerJob(jobDetails, "jobId", Tenant.of("tenant-id"));
```
In this example, the job type is `STALE_CONNECTS_TO`, elements include `vertex1` and `vertex2`. The stale duration is set to 30 minutes.

### Example 2: Triggering a Job with Default Parameters
```java
Map<String, String> defaultJobDetails = new HashMap<>();
defaultJobDetails.put(JOB_TYPE, "REMOVE_STALE_TRACE");
defaultJobDetails.put(STALE_DURATION, "15");
defaultJobDetails.put(TIME_UNIT, "SECONDS");

triggerJob(defaultJobDetails, "jobId", Tenant.of("tenant-id"));
```
In this case, the job type is `REMOVE_STALE_TRACE`, elements are not specified in the input map. The stale duration is set to 15 seconds.

### Example 3: Triggering a Job with Specific Tenant Information
```java
Map<String, String> jobDetails = new HashMap<>();
jobDetails.put(JOB_TYPE, "REMOVE_DUPLICATE_VERTEX");
jobDetails.put(ELEMENTS, "vertexA, vertexB, vertexC");

Tenant tenant = Tenant.of("tenant-id", "role-id", "user-name");

triggerJob(jobDetails, "jobId", tenant);
```
This example specifies the job type as `REMOVE_DUPLICATE_VERTEX`, elements include `vertexA`, `vertexB`, and `vertexC`. The job is triggered on a specific tenant with roles and user details.

### Example 4: Handling Exceptions During Job Execution
```java
Map<String, String> exceptionJobDetails = new HashMap<>();
exceptionJobDetails.put(JOB_TYPE, "REMOVE_DUPLICATE_VERTEX");
exceptionJobDetails.put(ELEMENTS, "vertex1, vertex2");
exceptionJobDetails.put(STALE_DURATION, "30");
exceptionJobDetails.put(TIME_UNIT, "HOURS");

triggerJob(exceptionJobDetails, "jobId", Tenant.of("tenant-id"));
```
In this example, a job type of `REMOVE_DUPLICATE_VERTEX` is executed with stale duration set to 30 hours. Since the input map contains an error message ("Exception processing the remove duplicate"), the exception handling mechanism results in logging of an error and skipping execution.

## Methods

### Method: triggerJob(Map<String, String> jobDetails, String jobId, Tenant tenant)

- **Description**: This method triggers a job based on its type and provides a completion signal once completed.
  
- **Parameters**:
  - `jobDetails`: Map containing details of the job to be processed. Key-value pairs typically include job types (e.g., `JOB_TYPE`), elements (`ELEMENTS`), stale duration, and time unit for duration measurement.
  
  - `jobId`: The identifier of the job that needs to be triggered.

- **Returns**: None
  
- **Example**:
  ```java
  triggerJob(jobDetails, "jobId", Tenant.of("tenant-id"));
  ```

### Method: triggerRemoveDuplicateVerticesTask(Tenant tenant, Map<String, String> jobDetails)

- **Description**: This method processes and removes duplicates for vertices based on the provided elements.

- **Parameters**:
  - `tenant`: The tenant information needed to access the graph cache.
  
  - `jobDetails`: Contains details of the task like elements (`ELEMENTS`), stale duration, and time unit for duration measurement.

- **Returns**: None
  
- **Example**:
  ```java
  triggerRemoveDuplicateVerticesTask(Tenant.of("tenant-id", "role-id", "user-name"), jobDetails);
  ```

### Method: getStaleDurationAsMilliSecs(String staleDurationStr, String timeUnit)

- **Description**: This method calculates the duration in milliseconds based on a given string representation of the duration and the unit.

- **Parameters**:
  - `staleDurationStr`: A string representing the duration (e.g., "30m", "1h").
  
  - `timeUnit`: Unit of measurement for the duration, typically "HOURS", "MINUTES", or "SECONDS".

- **Returns**: The calculated duration in milliseconds.

### Method: findAndRemoveStale(Tenant tenant, Map<String, String> jobDetails)

- **Description**: This method finds and removes stale traces based on provided elements and a given duration. 

- **Parameters**:
  - `tenant`: Tenant information needed to interact with the graph cache.
  
  - `jobDetails`: A map of details including elements (`ELEMENTS`), stale duration, and time unit for duration measurement.

- **Returns**: None
  
- **Example**:
  ```java
  findAndRemoveStale(Tenant.of("tenant-id", "role-id", "user-name"), jobDetails);
  ```

### Method: signalJobCompletion(Tenant tenant, String jobId)

- **Description**: This method signals the completion of a job.

- **Parameters**:
  - `tenant`: The tenant information needed to interact with the scheduler service.
  
  - `jobId`: Identifier for the completed job.

- **Returns**: None
  
- **Example**:
  ```java
  signalJobCompletion(tenant, "jobId");
  ```
```

This documentation covers all aspects of the JobIngester class, including its methods and how they can be used in practice.