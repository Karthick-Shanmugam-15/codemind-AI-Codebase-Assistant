## Overview

The `NodeConfigHandler` class is responsible for parsing and updating the attributes of nodes in a graph. It executes based on specific configurations provided through a payLoad object, which typically contains rules or other configuration details.

### Usage

```java
import org.springframework.batch.core.Job;
import org.springframework.batch.item.ItemProcessor;

public class YourJob {
    private NodeConfigHandler nodeConfigHandler;

    public void execute(String configRecord) throws Exception {
        Map<String, Object> payLoad = new HashMap<>();
        payLoad.put("configRecord", configRecord);
        
        Job job = JobBuilderFactory.get("your-job-name").build();
        job.setStep(this.createUpdateNodeAttributesStep(payLoad));
        job.initialize();

        // Start the job
        job.launchAndReturnJobExecution();
    }

    private Step createUpdateNodeAttributesStep(Map<String, Object> payLoad) {
        return stepBuilderFactory....
    }
}
```

### Methods

#### execute(RuleEngine.RuleRunner ruleRunner, Map<String, Object> payLoad, RuleOutput ruleOutput, Consumer<Object> consumer)

- **Description**: Executes the `NodeConfigHandler` class based on the provided `payLoad`. It parses and updates the attributes of nodes according to the configurations.
  
  - The `RuleEngine.RuleRunner` is used for triggering or executing rules. It might be necessary if you are using a rule-based workflow system like Spring Batch.

- **Parameters**:
  - `ruleRunner`: An instance of `RuleEngine.RuleRunner`. This parameter is not being utilized in this method but could be relevant if you are implementing the flow based on a Rule Engine.
  - `payLoad`: A map containing the configurations or details needed for processing. In this case, it typically includes the configuration record and other rules.
  
  - `ruleOutput`: An instance of `RuleEngine.RuleOutput` that captures the results of rule execution.
  
  - `consumer`: A consumer object which can be used to pass data back into another step in your job flow.

- **Returns**:
  - None

- **Example**

```java
Map<String, Object> payLoad = new HashMap<>();
payLoad.put("configRecord", "your-config-record");

NodeConfigHandler nodeConfigHandler = new NodeConfigHandler();
nodeConfigHandler.execute(ruleRunner, payLoad, ruleOutput, consumer);
```

### Inner Class: ConfigEvent

- **Description**: Represents an event related to configuration events in a batch job.
  
  - It contains information like the type of production and outputs from vertices or edges. This class is likely used internally within the `NodeConfigHandler`.

#### parseBytesValueToGi(String bytes)
- **Description**: Converts byte value to gigabytes (Gi).
  
  - If you are parsing configurations that might be in kilobytes, megabytes, etc., this method would convert them into gigabytes for easier management or processing.

### Notes

This class is part of a batch job setup where it parses and updates node attributes based on the configuration details provided. It's utilized within an `@StepBuilderFactory` to create steps within a Spring Batch Job that handle these configurations.