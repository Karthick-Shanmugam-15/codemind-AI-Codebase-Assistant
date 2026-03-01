## Overview

The `Info` class is a basic information holder. It can store and return some fundamental data points about the object, such as an ID number or a name.

## Usage

```java
// Example of using the Info class
public class Main {
    public static void main(String[] args) {
        // Create an instance of the Info class
        Info info = new Info();

        // Set some properties for the Info object
        info.setId(12345);
        info.setName("John Doe");

        // Access and print out some information about the object
        System.out.println(info.getId());
        System.out.println(info.getName());

        // Check if a specific property exists in the Info object
        boolean hasName = info.containsKeyProperty("name");
        System.out.println(hasName);  // Should output true

        // Remove a property from the Info object
        info.removeProperty("age");

        // Print out the updated information
        System.out.println(info.getName());  // Should print "John Doe"
    }
}
```

## Methods

### setId(int value)
- **Description**: Set the ID of the `Info` object.
- **Parameters**: `value` (int) - The new ID to set.
- **Returns**: None
- **Example**:
  ```java
  info.setId(67890);
  System.out.println(info.getId());  // Should output 67890
  ```

### setName(String value)
- **Description**: Set the name of the `Info` object.
- **Parameters**: `value` (String) - The new name to set.
- **Returns**: None
- **Example**:
  ```java
  info.setName("Jane Smith");
  System.out.println(info.getName());  // Should output "Jane Smith"
  ```

### getID()
- **Description**: Return the ID of the `Info` object.
- **Parameters**: None
- **Returns**: int - The current ID value.
- **Example**:
  ```java
  info.setId(12345);
  System.out.println(info.getID());  // Should output 12345
  ```

### getName()
- **Description**: Return the name of the `Info` object.
- **Parameters**: None
- **Returns**: String - The current name value.
- **Example**:
  ```java
  info.setName("John Doe");
  System.out.println(info.getName());  // Should output "John Doe"
  ```

### isPropertyExists(String property)
- **Description**: Check if a specific property exists in the `Info` object. A property can be either an ID or a name.
- **Parameters**: `property` (String) - The name of the property to check for existence.
- **Returns**: boolean - True if the property exists, false otherwise.
- **Example**:
  ```java
  System.out.println(info.containsKeyProperty("name"));  // Should output true
  ```

### removeProperty(String property)
- **Description**: Remove a specific property (ID or name) from the `Info` object. The ID is removed as an integer, while the name remains in the string format.
- **Parameters**: `property` (String) - The name of the property to be removed.
- **Returns**: None
- **Example**:
  ```java
  info.removeProperty("name");
  System.out.println(info.getName());  // Should output ""
  ```

### toString()
- **Description**: Return a string representation of the `Info` object, including its ID and name if available.
- **Parameters**: None
- **Returns**: String - A string containing information about the `Info` object.

```java
System.out.println(info);  // Should output something like "ID: 67890 Name: John Doe"
```

### getClass()
- **Description**: Return the class of the `Info` object.
- **Parameters**: None
- **Returns**: Class<Info> - The class of the `Info` object.

```java
System.out.println(info.getClass());  // Should output <class Info>
```