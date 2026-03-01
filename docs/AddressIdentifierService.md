## Overview

`AddressIdentifierService` is a class designed to facilitate the identification of cloud services based on IP addresses and port numbers. It supports discovery, caching, and updates for various Cloud Service types such as AWS, Azure, Google Cloud Platform (GCP), Private Network.

## Usage

### Example of How to Use `AddressIdentifierService`

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();

        // Find a cloud service by IP address and port
        CloudService subnetInfo = service.isIPandPortExistsInCache("192.168.0.1", "443");
        if (subnetInfo != null && !subnetInfo.equals(CloudService.UNMAPPED)) {
            System.out.println(subnetInfo);
        } else {
            System.out.println("No matching subnet found.");
        }

        // Discover Cloud Services
        service.updateSubnetInfo();
        
        // Get Cloud CIDR for a specific IP address and port
        String ipAddress = "192.168.0.1";
        String port = "443";
        CloudService subnetCIDR = service.getCloudCIDR(ipAddress, port);
        if (subnetCIDR != null) {
            System.out.println(subnetCIDR.toString());
        } else {
            System.out.println("No matching CIDR found.");
        }
    }
}
```

### Example of Disabling DNS Grouping

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main2 {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();
        service.setDNS_GROUPING_ENABLED(false);
        
        // Disable the ability to group DNS names and regex patterns for easier testing or configuration changes.
    }
}
```

### Example of Setting Private Network

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main3 {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();
        
        // Set the private network in your environment
        service.setPrivateNW();

        // You can then check if it's successfully set up.
        CloudService privateNetwork = service.getPrivateNW();
        if (privateNetwork != null && !privateNetwork.equals(CloudService.UNMAPPED)) {
            System.out.println("Private Network Successfully Set Up.");
        } else {
            System.out.println("Failed to set up the Private Network.");
        }
    }
}
```

### Example of Discovering Cloud Services

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main4 {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();

        // List all discovered cloud services
        for (CloudService cs : service.getCLOUD_SERVICES()) {
            System.out.println(cs);
        }

        if (!service.isINITIALIZED()) {
            System.out.println("Initialization not complete, unable to list Cloud Services.");
        }
    }
}
```

### Example of Checking DNS Grouping Configuration

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main5 {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();
        
        // Check if DNS grouping is enabled or disabled.
        boolean dnsEnabled = service.isDNS_GROUPING_ENABLED();

        System.out.println("Is DNS Grouping Enabled: " + (dnsEnabled ? "Enabled" : "Disabled"));
    }
}
```

### Example of Setting Grouped Ports

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main6 {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();

        // Add groupable port information to the system.
        service.setGroupPorts("192.168.0.0/24:53, 172.16.0.0/16:80");
        
        if (service.isINITIALIZED()) {
            System.out.println("Port groups added successfully.");
        } else {
            System.out.println("Initialization not complete, unable to add port group information.");
        }
    }
}
```

### Example of Checking Grouped DNS

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main7 {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();

        // Check if the grouped domain names exist in the system.
        boolean groupDNSEnabled = service.isDnsNameExistInRegexPattern("example.com");
        
        System.out.println("Does 'example.com' match any regex patterns? " + (groupDNSEnabled ? "Yes" : "No"));
    }
}
```

### Example of Setting Grouped DNS Names

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main8 {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();

        // Set up groupable DNS names.
        service.setGroupDNS("example.com:*.googleusercontent.com, example.org:*.twitter.com");

        if (service.isINITIALIZED()) {
            System.out.println("DNS groups successfully set.");
        } else {
            System.out.println("Initialization not complete, unable to set up grouped DNS groups.");
        }
    }
}
```

### Example of Setting Enabled State

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main9 {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();
        
        // Enable or disable the system.
        boolean enabledState = true; // Change this to false if you want to disable it.

        service.setEnabled(enabledState);
        
        if (service.isEnabled()) {
            System.out.println("Address Identifier Service is now " + (enabledState ? "Enabled" : "Disabled") + ".");
        } else {
            System.out.println("Initialization not complete, unable to enable/disable the Address Identifier Service.");
        }
    }
}
```

### Example of Setting Azure Public IP Range

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main10 {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();
        
        // Set up the endpoint URL for fetching Azure's public IP ranges.
        String azureIpRangesJsonURL = "https://raw.githubusercontent.com/Azure/azure-public-network-records/master/public-ip.json";
        
        service.setAzureIpRangesJsonURL(azureIpRangesJsonURL);
        
        if (service.isINITIALIZED()) {
            System.out.println("Azure Public IP Range set up successfully.");
        } else {
            System.out.println("Initialization not complete, unable to fetch Azure public IP ranges.");
        }
    }
}
```

### Example of Setting DNS Grouping Enabled

```java
import com.example.addressidentifier.AddressIdentifierService;

public class Main11 {
    public static void main(String[] args) {
        AddressIdentifierService service = AddressIdentifierService.getInstance();
        
        // Set up the configuration for enabling or disabling DNS groupings.
        boolean enableGrouping = true;
        service.setDNS_GROUPING_ENABLED(enableGrouping);
        
        if (service.isDNS_GROUPING_ENABLED()) {
            System.out.println("DNS Grouping enabled.");
        } else {
            System.out.println("DNS Grouping disabled.");
        }
    }
}
```