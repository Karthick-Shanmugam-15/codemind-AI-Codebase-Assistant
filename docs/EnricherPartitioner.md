# EnricherPartitioner Class

## Overview

The `EnricherPartitioner` class is a utility that is part of Kafka Streams, an open-source implementation for building stream processing applications. It is responsible for distributing messages across partitions based on the key-value pairs provided to it.

### Usage

To use the `EnricherPartitioner`, you typically pass it keys and values as strings or other objects in your Kafka streams configuration. The class then forwards these messages to different partitions based on the specified partitioning strategy (which is determined by the type of `partition` method called).

#### Example Usage:

```java
KafkaStreams kafkaStreams = new KafkaStreams(...);

// Assuming you have keys like "topic-partition1" and values like "some-key-value"
kafkaStreams.setStream("input-topic", 
        Collections.singletonMap("key-type", "String"),
        Collections.singletonMap("value-type", "Object"),
        // Optionally, specify the number of partitions if needed
        new EnricherPartitioner());

// To forward messages to a specific partition,
// you can use:
kafkaStreams.forwardTo("output-topic-1");
```

### Methods

#### method: `partition(String topic, Object key, Object value, int numPartitions)`
```java
@Override
public Integer partition(String topic, Object key, Object value, int numPartitions) {
    if(debugLoggingEnabled) logger.debug("Forwarding the message to partition number: {}", (String)key);
    return Integer.parseInt((String)key);
}
```

- **Description**: This method is a part of the `partition` parameter in Kafka Streams. It forwards messages based on the key provided, which is expected to be an integer string.

- **Parameters**:
  - `topic`: The topic name where messages are being sent.
  - `key`: A String or Object representing the partitioning key for this message.
  - `value`: An Object that represents the value of the message. This could be any type supported by Kafka Streams.
  - `numPartitions`: The number of partitions to which the message should be forwarded.

- **Returns**: `Integer.parseInt((String)key)` returns an integer representing the partition key as a string, and forwards messages to this specified partition.

### Debugging

The method includes logging for debugging purposes. It outputs a debug message with the forwarding details before returning the partition number as a parsed integer.

### Example Usage:

```java
KafkaStreams kafkaStreams = new KafkaStreams(...);

// Assuming you have keys like "topic-partition1" and values like "some-key-value"
kafkaStreams.setStream("input-topic", 
        Collections.singletonMap("key-type", "String"),
        Collections.singletonMap("value-type", "Object"),
        // Optionally, specify the number of partitions if needed
        new EnricherPartitioner());

// To forward messages to a specific partition,
// you can use:
kafkaStreams.forwardTo("output-topic-1");
```

### Additional Notes

- The `EnricherPartitioner` class is not part of Kafka Streams itself but rather an external utility used within a Kafka Streams configuration.
- If you need more control over the partitioning, consider using a different Kafka Streams component or configuration method.

This implementation allows for flexible message distribution across partitions based on key-value pairs.