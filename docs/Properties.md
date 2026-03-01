## Overview
The `Properties` class is an empty placeholder designed to be used as a base class for classes that manage properties or configurations. This ensures that all subclasses of `Properties` are immutable and thread-safe.

## Usage
### Example

```java
import org.javacord.api.properties.Properties;
import java.util.Map;

public class ConfigurationManager extends Properties {

    private Map<String, String> config = new HashMap<>();

    public ConfigurationManager() {
        // Initialize the map to store configuration settings.
    }

    /**
     * Adds a property to the map with its value.
     *
     * @param key The unique identifier for this property.
     * @param value The value of the property.
     */
    protected void addProperty(String key, String value) {
        config.put(key, value);
    }
}

// Example usage
ConfigurationManager manager = new ConfigurationManager();
manager.addProperty("serverPort", "8080");
```

### Explanation

- **`public Properties()`**: This is the constructor for the `Properties` class. It has no parameters and initializes the class.
  
- **Methods**:

  - `protected void addProperty(String key, String value)`: This method allows subclasses to add properties to a map-like structure that stores configuration settings. The `protected` access level means it can be overridden in any subclass.

### Notes

This empty base class is useful for managing configurations or properties in Java applications where you need an immutable and thread-safe way of holding data without exposing the implementation details.