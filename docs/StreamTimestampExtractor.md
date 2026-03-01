## Overview

The `StreamTimestampExtractor` class is designed to extract a timestamp from incoming data records. The extracted timestamp is used for the purpose of ensuring that timestamps are not lost due to network latency or other issues, particularly in a scenario where real-time processing or monitoring might be required.

## Usage

The `extract` method takes two parameters:  
- **ConsumerRecord**: A record representing the received message from Kafka.
- **previousTimestamp**: The timestamp provided for comparison.

This method then calls another method `decodeData`, which decodes data into an object of type `Metric`. If the decoded object is a `Metric`, its payload's samples' timestamp is extracted and returned. If not, the method returns `null`.

### Example

```java
import org.apache.kafka.common.record.ConsumerRecord;
import com.opscruise.common.avro.prometheus.Metric;

public class Test {
    public static void main(String[] args) throws Exception {
        // Create a record with data from Kafka
        byte[] value = new byte[]{/* Your Kafka message bytes here */};
        
        // Define the previous timestamp
        long previousTimestamp = 1609459200L; // Unix epoch
        
        try {
            // Extract and decode the data
            Metric metricData = (Metric) StreamTimestampExtractor.extract(new ConsumerRecord<>(/* Your topic name here */, 0), previousTimestamp);
            
            if (metricData != null) {
                System.out.println("Extracted timestamp: " + metricData.getPayLoad().getSamples().iterator().next().getTimestamp());
            } else {
                System.out.println("No Metric data extracted.");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## Methods

### `extract(ConsumerRecord<Object, Object> record, long previousTimestamp)`

**Description**: Extracts a timestamp from incoming Kafka message records and compares it with the provided `previousTimestamp` to ensure data integrity.

- **Parameters**:  
  - `record`: A `ConsumerRecord` containing the received data.
  - `previousTimestamp`: The timestamp previously extracted or assigned (optional, defaulting to zero if not provided).

**Returns**:  
The extracted timestamp from the message's payload. If no `Metric` is found within a `ConfigEvent`, it returns `null`.

### `decodeData(byte[] value)`

**Description**: Decodes data received via Kafka into an object of type `Metric`. This method handles decoding Avro-encoded binary messages.

- **Parameters**:  
  - `value`: A byte array containing the decoded message.
  - `classType`: The class that is expected to be in the payload (typically a custom `Metric` or `ConfigEvent` subclass).

**Returns**:  
The deserialized object, which can either be a `Metric`, a `ConfigEvent`, or `null`.

### `decodeAvroData(byte[] value, Class<T> classType)`

**Description**: Decodes Avro data into the specified class. This method is part of the overall process where Kafka messages are decoded and transformed.

- **Parameters**:  
  - `value`: A byte array containing the Avro-encoded message.
  - `classType`: The class that needs to be deserialized from the binary data.

**Returns**:  
The deserialized object or `null` if decoding fails.