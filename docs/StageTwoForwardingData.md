## Overview

`StageTwoForwardingData` is a class designed to encapsulate the necessary information for forward-decoding and forwarding messages in a system that uses stage two processing. This class provides a straightforward way to send data through an intermediate process before it reaches its final destination.

### Usage

To use `StageTwoForwardingData`, you need to provide headers, data, and topic as parameters:

```java
Headers headers = new Headers();
headers.put("X-Topic", "mytopic");
headers.put("Content-Type", "application/json");

Object messageBody = "{ \"key\": \"value\" }";

String topic = "mytopic";

// Create a StageTwoForwardingData instance
StageTwoForwardingData forwardingData = new StageTwoForwardingData(headers, messageBody, topic);
```

### Methods

#### Method: `public void setData(Object data)`
- **Description**: This method is used to set the data that will be sent through the stage two processing. It requires a `data` parameter of type `Object`.
  
  ```java
  public StageTwoForwardingData setData(Object data) {
      this.data = data;
      return this;
  }
  ```
- **Parameters**: `data` (required).
- **Returns**: This method does not return anything.
- **Example**:
  ```java
  // Set new message body after modifying the previous one
  String modifiedMessageBody = "New Message Body";
  forwardingData.setData(modifiedMessageBody);
  ```

#### Method: `public Headers getHeaders()`
- **Description**: This method is used to retrieve the headers associated with the forwarding data.
  
  ```java
  public Headers getHeaders() {
      return this.headers;
  }
  ```
- **Parameters**: None.
- **Returns**: A `Headers` object representing the original headers.
- **Example**:
  ```java
  // Get headers from the forwarded message
  Headers originalHeaders = forwardingData.getHeaders();
  ```

#### Method: `public String getTopic()`
- **Description**: This method is used to retrieve the topic associated with the forwarding data.
  
  ```java
  public String getTopic() {
      return this.topic;
  }
  ```
- **Parameters**: None.
- **Returns**: A `String` representing the original topic.
- **Example**:
  ```java
  // Get the topic from the forwarded message
  String forwardedTopic = forwardingData.getTopic();
  ```

#### Method: `public boolean isLocal()`
- **Description**: This method checks if this data was sent locally (i.e., without going through a stage two process).
  
  ```java
  public boolean isLocal() {
      return this.local;
  }
  ```
- **Parameters**: None.
- **Returns**: A `boolean` indicating whether the forwarding was local or not.
- **Example**:
  ```java
  // Check if data was sent locally
  boolean forwardedLocally = forwardingData.isLocal();
  ```

### Conclusion

The `StageTwoForwardingData` class provides a convenient way to encapsulate and manage the forwarding of messages, ensuring that they are sent through an intermediate stage without affecting their original format or headers.