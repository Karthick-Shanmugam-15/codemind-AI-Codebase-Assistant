### Overview

The `GCPIPInfo` class is designed to encapsulate and manage a list of Cloud Private (CloudP) subnets in a Google Cloud Platform (GCP) environment. It provides methods to retrieve all available Cloud Private subnets that match the specified prefix.

### Usage

Here's an example of how you can use this class:

```java
import com.example.gcplibinfo.GCPIPInfo;
import com.google.cloud.gcp.v1.Subnet;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Instantiate the GCPIPInfo object for your project and region.
        GCPIPInfo gcpipInfo = new GCPIPInfo();

        try {
            List<CloudService> subnets = gcpipInfo.getCloudSubnets();
            if (subnets != null && !subnets.isEmpty()) {
                subnets.forEach(subnet -> System.out.println("Found Cloud Private Subnet: " + subnet.getName()));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Methods

#### Method Declaration: `getCloudSubnets()`

```java
/**
 * Retrieves all available Cloud Private subnets that match the specified prefix.
 *
 * @return A list of cloud private services matching the prefix.
 */
public List<CloudService> getCloudSubnets() {
    // Implementation for fetching and processing CloudP subnets from GCP.
}
```

### Method Description

- This method retrieves all available Cloud Private (GCP) subnets that match the specified prefix. It processes each prefix to determine if it matches the criteria and then adds it to a list of `CloudService` objects.

#### Parameters

- **Prefix**: An object representing a specific Cloud Private subnet prefix, containing information such as service type and scope.
  
#### Returns

- A List of `CloudService` objects that match the specified prefix. Each `CloudService` contains details about the subnets' CIDRs (Classless Inter-Domain Routing) and other network configurations.

#### Example Usage

This method is designed to be used in conjunction with the Google Cloud Platform API to fetch the necessary information from GCP. The example above shows how you can call this method within a program, which then filters out the subnets that match the provided prefix for further processing or display.