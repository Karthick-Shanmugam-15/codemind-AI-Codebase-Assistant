# Overview

The `EventRule` class is designed to handle rule execution for events, particularly in a context where event rules are defined and managed. This class implements an abstract method that is typically overridden by concrete implementations to perform specific actions based on the type of event.

# Usage

To use the `EventRule` class, you can instantiate it as a part of a rule engine system. Here's a basic example:

```java
// Assuming RuleEngine and RuleRunner are already defined and initialized

RuleEngine.RuleRunner ruleRunner = new RuleEngine().getRuleRunner(); // Replace with your actual logic

Map<String, Object> payload = new HashMap<>();
payload.put("configRecord", configEvent);
payload.put("tenant", tenant);

Consumer<Object> consumer = new Consumer<>();

try {
    EventRule eventRule = new EventRule();
    eventRule.execute(ruleRunner, payload, RuleOutput.DEFAULT_OUTPUT, consumer);
} catch (Exception e) {
    System.err.println("An error occurred while executing the rule: " + e.getMessage());
}
```

# Methods

## `execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payload, RuleOutput ruleOutput, Consumer<Object> consumer)` Method

### Description

This method is overridden by concrete implementations of the `EventRule` class to perform specific actions for each event type. The parameters are passed through and can be customized based on the rules defined in your system.

### Parameters

- `ruleRunner`: A `RuleEngine.RuleRunner` instance used to execute the rule.
- `payload`: A map containing all the necessary data required by the event rule, such as identifiers of entities involved in the event (e.g., configuration record).
- `ruleOutput`: An enum representing the output format for the rule execution result. Default is `RuleOutput.DEFAULT_OUTPUT`.
- `consumer`: A `Consumer` instance to handle any extra outputs or side effects from the rule.

### Returns

This method does not return a value but handles exceptions that might occur during its execution and logs them using the `logger`.

### Example

Here's an example of how the concrete implementation of the `EventRule` class could look for handling specific types of events:

```java
public class ConfigEventSubRule extends EventRule {

    @Override
    public void execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payload, RuleOutput ruleOutput, Consumer<Object> consumer) throws Exception {
        super.execute(ruleRunner, payload, ruleOutput, consumer);
        
        // Custom logic for a specific type of event, say "create"
        if (payload.get("configRecord") instanceof ConfigEventSubRule.ConfigEvent && ((ConfigEvent) payload.get("configRecord")).getCrud() == "create") {
            LOGGER.info("Processing the Create Event {}", payload.toString());
            
            // Example: Perform custom actions or logic here
            String eventName = ((ConfigEvent) payload.get("configRecord")).getName();
            Configuration configuration = new Configuration();  // Assume this is a configuration object
            
            // Here you can add your specific rules for handling create events such as updating configurations, etc.
        }
    }

    public static class ConfigEvent extends EventRule.ConfigEvent {
        
        public String name;
        public CrudType crud;

        @Override
        public void setName(String name) {
            this.name = name;
        }

        public enum CrudType { CREATE, UPDATE, DELETE };
    }
}
```

In the example above:
- The `execute` method is overridden.
- A custom logic for handling "create" events (e.g., updating configurations) is added to a subclass of `EventRule`.
- This subclass (`ConfigEventSubRule`) registers it with the rule engine system.

This mechanism allows your system to dynamically handle different types of rules and events based on their type, which can be crucial in complex event-driven systems.