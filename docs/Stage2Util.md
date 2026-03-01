## Overview

The `Stage2Util` class is designed to facilitate the forwarding of data to specific topics based on the provided configuration parameters. It includes methods for initializing the system with various configurations and handling incoming headers.

### Usage

#### Method 1: `init(String anomalyTop, String configEventTop, String invexpTop, String monQTop, String eventTopic)`
```java
Stage2Util.init("anomaly-top", "config-event-top", "inventory-exp-top", "monitoring-q-top", "event-topic");
```
This method initializes the system with specified configuration topics and an event topic.

#### Method 2: `addHeaders(Headers headers)`
```java
Headers headers = new Headers();
headers.add(new String[]{"key1": "value1"});
headers.add("key2".getBytes());

Stage2Util.addHeaders(headers);
```
This method adds custom headers to the incoming message for processing and forwarding.

#### Method 3: `getIPFromIdentifiers(List<String> srcIdentifiers)`
```java
List<String> identifiers = Arrays.asList("ip1", "ip2, 8.8.8.8");
String ipAddress = Stage2Util.getIPFromIdentifiers(identifiers);
```
This method extracts the IP address from a list of identifiers.

#### Method 4: `getInvExpHeader(Tenant tenant, long syncTimestamp, String eventType)`
```java
Tenant tenant = new Tenant("123", "xyz");
long syncTime = 1625804800;
String eventStr = "event";

Headers invExpHeader = Stage2Util.getInvExpHeader(tenant, syncTime, eventStr);
```
This method generates a header for an inventory exp message.

#### Method 5: `getSchedulerHeader(Tenant tenant, String jobId)`
```java
Tenant tenant = new Tenant("123", "xyz");
String jobID = "01234";
Headers schedulerHeader = Stage2Util.getSchedulerHeader(tenant, jobID);
```
This method generates a header for a scheduler service message.

#### Method 6: `sendDataToInvExp(Tenant tenant, String type, long syncTimeStamp)`
```java
Stage2Util.sendDataToInvExp(new Tenant("123", "xyz"), "inventory", System.currentTimeMillis());
```
This method forwards an inventory exp event to the specified topic based on the provided parameters.

#### Method 7: `signalSchedulerService(Tenant tenant, String jobId, String complete)`
```java
Stage2Util.signalSchedulerService(new Tenant("456", "abc"), "1234", "job completed");
```
This method forwards a job status message to the scheduler service topic indicating that the job is complete.

### Methods

#### Method 8: `init(String anomalyTop, String configEventTop, String invexpTop, String monQTop, String eventTopic)`
```java
Stage2Util.init("anomaly-top", "config-event-top", "inventory-exp-top", "monitoring-q-top", "event-topic");
```
This method initializes the system with specified configuration topics and an event topic.

#### Method 9: `addHeaders(Headers headers)`
```java
Headers headers = new Headers();
headers.add(new String[]{"key1": "value1"});
headers.add("key2".getBytes());

Stage2Util.addHeaders(headers);
```
This method adds custom headers to the incoming message for processing and forwarding.

#### Method 10: `getIPFromIdentifiers(List<String> srcIdentifiers)`
```java
List<String> identifiers = Arrays.asList("ip1", "ip2, 8.8.8.8");
String ipAddress = Stage2Util.getIPFromIdentifiers(identifiers);
```
This method extracts the IP address from a list of identifiers.

#### Method 11: `getInvExpHeader(Tenant tenant, long syncTimestamp, String eventType)`
```java
Tenant tenant = new Tenant("123", "xyz");
long syncTime = 1625804800;
String eventStr = "event";

Headers invExpHeader = Stage2Util.getInvExpHeader(tenant, syncTime, eventStr);
```
This method generates a header for an inventory exp message.

#### Method 12: `getSchedulerHeader(Tenant tenant, String jobId)`
```java
Tenant tenant = new Tenant("123", "xyz");
String jobID = "01234";
Headers schedulerHeader = Stage2Util.getSchedulerHeader(tenant, jobID);
```
This method generates a header for a scheduler service message.

#### Method 13: `sendDataToInvExp(Tenant tenant, String type, long syncTimeStamp)`
```java
Stage2Util.sendDataToInvExp(new Tenant("123", "xyz"), "inventory", System.currentTimeMillis());
```
This method forwards an inventory exp event to the specified topic based on the provided parameters.

#### Method 14: `signalSchedulerService(Tenant tenant, String jobId, String complete)`
```java
Stage2Util.signalSchedulerService(new Tenant("456", "abc"), "1234", "job completed");
```
This method forwards a job status message to the scheduler service topic indicating that the job is complete.

### Summary

The `Stage2Util` class provides essential functionalities for setting up and processing messages, including event handling, header addition, IP extraction, and forwarding operations. The methods are designed to work together seamlessly within a larger system architecture to ensure efficient data flow and message processing.