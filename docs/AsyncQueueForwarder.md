# AsyncQueueForwarder

## Overview
`AsyncQueueForwarder` is a class designed to forward messages asynchronously from one topic to another. It uses KafkaProducer to send the encoded data in an asynchronous manner.

## Usage
To use `AsyncQueueForwarder`, you can initialize it and then call its `forward` method with appropriate parameters:

```java
Properties streamsConfiguration = new Properties();
// Configure streams configuration here...

AsyncQueueForwarder forwarder = new AsyncQueueForwarder(streamsConfiguration);
forwarder.forward(new StageTwoForwardingData(), tenant); // Replace 'tenant' with actual Tenant object
```

### Example

```java
Properties streamsConfiguration = new Properties();
streamsConfiguration.put(StreamsConfig.APPLICATION_ID_CONFIG, "example-app");
streamsConfiguration.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");

AsyncQueueForwarder forwarder = new AsyncQueueForwarder(streamsConfiguration);

// Assuming you have a StageTwoForwardingData object named 'data'
data.setTopic("your_topic"); // Set the topic name
data.setOutput(new byte[] { /* Your encoded data bytes */ }); // Encode your data and set it

if (forwarder.forward(data, tenant) && forwarder.forwardedMessage()) {
    System.out.println("Message forwarded successfully.");
} else {
    System.out.println("Failed to forward message.");
}
```

### Methods

#### `init(final Properties streamsConfiguration)`
- **Description**: Initializes the KafkaProducer with the provided configuration.
- **Parameters**:
  - `streamsConfiguration`: The properties object containing the necessary configurations for the KafkaProducer.

```java
public static void init(final Properties streamsConfiguration) {
    forwarder.localProducer = new KafkaProducer<>(streamsConfiguration);
}
```

#### `getInstance()`
- **Description**: Returns an instance of `AsyncQueueForwarder`.
- **Parameters**:
  - None

```java
public static AsyncQueueForwarder getInstance() {
    return forwarder;
}
```

#### `forward(final StageTwoForwardingData data, Tenant tenant)`
- **Description**: Asynchronously forwards the provided message to a Kafka topic.
- **Parameters**:
  - `data`: The data object containing the content and headers to be forwarded.
  - `tenant`: The tenant information needed for routing.

```java
public boolean forward(final StageTwoForwardingData data, Tenant tenant) {
    // Implementation of the method...
}
```

#### `constructAndForwardEncodedData(StageTwoForwardingData data, Tenant tenant)`
- **Description**: Constructs a Kafka producer record and forwards it asynchronously.
- **Parameters**:
  - `data`: The data object containing the content and headers to be forwarded.
  - `tenant`: The tenant information needed for routing.

```java
private void constructAndForwardEncodedData(StageTwoForwardingData data, Tenant tenant) {
    // Implementation of the method...
}
```

#### `getExecutor()`
- **Description**: Returns an executor object that can be used to run asynchronous tasks.
- **Parameters**:
  - None

```java
public Executor getExecutor() {
    if (MSG_FWD_EXECUTOR.getQueue().size() > QUEUE_THRESHOLD) {
        try {
            Thread.sleep(THREAD_SLEEP_MS);
        } catch (InterruptedException interruptedException) {
            LOGGER.error("Error during Thread.sleep", interruptedException);
        }
    }
    return MSG_FWD_EXECUTOR;
}
```

#### `constructProducerRecord(StageTwoForwardingData ingesterData, Tenant tenant)`
- **Description**: Constructs a producer record based on the provided data and tenant details.
- **Parameters**:
  - `data`: The data object containing the content to be encoded.
  - `tenant`: The tenant information needed for routing.

```java
private ProducerRecord<String, byte[]> constructProducerRecord(StageTwoForwardingData ingesterData, Tenant tenant) {
    String key = String.format("%s:%s", tenant.getTenantId(), tenant.getClusterId());
    return new ProducerRecord<>(ingesterData.getTopic(), ingesterData.getPartitionId(), key, ingesterData.getOutput(), ingesterData.getHeaders());
}
```

#### `forwardedMessage()`
- **Description**: Returns a boolean indicating whether the message was successfully forwarded.
- **Parameters**:
  - None

```java
public boolean forwardedMessage() {
    // Implementation of the method...
}
```

### Logging and Debugging
The class includes logging to track errors, such as `LOGGER.error` for critical messages and `LOGGER.debug` for additional information.

```java
private static final String DATA_SIZE_LOG = "Data size: {} bytes";
private boolean isDebugEnabled() {
    return LOGGER.isDebugEnabled();
}

public void set.isDebugEnabled(boolean debug) {
    LOGGER.setLevel(debug ? Level.DEBUG : Level.INFO);
}
```

### Threading and Message Forwarding
The `getExecutor()` method ensures that messages are forwarded asynchronously to a queue, allowing for better performance in scenarios with high throughput.

```java
private static final int QUEUE_THRESHOLD = 100;
private static final long THREAD_SLEEP_MS = 500; // Adjust as needed

public boolean forward(final StageTwoForwardingData data, Tenant tenant) {
    if (localProducer == null) {
        LOGGER.error("Forwarder has not been initialized. Could not forward message");
        return false;
    }
    if (data == null || isBlank(data.getTopic())) {
        LOGGER.error("Invalid data or sink type. Could not forward message.");
        return false;
    }
    try {
        runAsync(() -> localProducer.send(constructProducerRecord(data, tenant)), getExecutor()).whenComplete((unused, throwable) -> {
            if (throwable != null) {
                LOGGER.error("Asynchronous forwarding from stage2 failed with exception.", throwable);
            } else {
                LOGGER.info("Sent record asynchronously to topic: {}, bytes {}", data.getTopic(), data.getOutput().length);
            }
        });
    } catch (final Throwable t) {
        LOGGER.error("Error while encoding data", t);
        return false;
    }

    // Additional logging for debug level
    if (isDebugEnabled()) {
        Map<String, String> headermap = new HashMap<>();
        data.getHeaders().forEach(header -> headermap.put(header.key(), new String(header.value())));
        LOGGER.debug(DATA_SIZE_LOG, (data.getOutput() != null) ? data.getOutput().length : 0, headermap);
    }

    return true;
}
```

### Conclusion
`AsyncQueueForwarder` is a powerful tool for asynchronously forwarding messages to Kafka topics from Apache Kafka Streams applications. It supports configuration and logging, making it easy to integrate with existing applications and environments.