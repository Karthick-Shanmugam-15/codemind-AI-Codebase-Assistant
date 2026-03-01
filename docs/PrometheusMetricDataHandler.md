## Overview

The `PrometheusMetricDataHandler` class is designed to handle metric data retrieved from Prometheus endpoints. It provides functionalities for processing and enriching time series metrics, as well as performing asynchronous tasks.

### Usage

```java
public class Main {
    public static void main(String[] args) {
        // Example of obtaining an instance of the PrometheusMetricDataHandler
        PrometheusMetricDataHandler prometheusMetricDataHandler = PrometheusMetricDataHandler.getInstance();

        // Process a metric data object and print results
        List<IngesterMetricData> metrics = prometheusMetricDataHandler.processMetric(null);
        for (IngesterMetricData metric : metrics) {
            System.out.println(metric.getMetric().getPayLoad());
        }

        // Perform processing asynchronously
        prometheusMetricDataHandler.processMetricAsync(null, (metricsList) -> {
            System.out.println("Processed Metrics: ");
            for (IngesterMetricData metric : metricsList) {
                System.out.println(metric);
            }
        });
    }
}
```

### Methods

```java
public class PrometheusMetricDataHandler extends IngesterMetricsProcessor {

    // Static method to get the instance of PrometheusMetricDataHandler
    public static PrometheusMetricDataHandler getInstance() {
        return prometheusMetricDataHandler;
    }

    @Override
    public List<IngesterMetricData> processMetric(final Object metricData) {
        final String query = (String) metricData;

        // Process the metric data and enrich it
        final IngesterMetricData ingesterMetricData = new IngesterMetricData();
        ingesterMetricData.setTs(new Types.TimeSeries());
        ingesterMetricData.setLabels(Types.Label::new);
        ingesterMetricData.setSample(getSample(Types.Sample::new));

        return List.of(ingesterMetricData);
    }

    @Override
    public void processMetricAsync(Object metricData, Consumer<List<IngesterMetricData>> stageOneDataConsumer) {
         // Implement asynchronous processing logic here (example omitted)
    }

    @Override
    public boolean isAsyncSupported() {
        return false;
    }

    private ThreadPoolExecutor getParallelThreadExecutor() {
        if(parallelEnricherThreadPoolExecutor == null){
            parallelEnricherThreadPoolExecutor = new ThreadPoolExecutor(
                    4, 4, 0L, TimeUnit.MILLISECONDS,
                    enricherQueue, new ThreadPoolExecutor.CallerRunsPolicy());
        }
        return parallelEnricherThreadPoolExecutor;
    }

    private void addMetricToS1Data(final IngesterMetricData s1d) {
        final Metric metric = new Metric();
        final Types.TimeSeries ts = s1d.getTs();
        final Map<String, String> labels = ts.getLabelsList().stream().collect(toMap(Types.Label::getName, Types.Label::getValue));
        final List<Sample> samplesArray = ts.getSamplesList().stream().map(s -> getSample(s)).filter(s -> s != null).collect(toList());
        if (samplesArray.isEmpty() || labels.isEmpty()) {
            LOGGER.warn("Ignoring metric with empty samples/labels");
            return;
        }
        metric.setPayLoad(new PayLoad(labels, samplesArray));
        s1d.setMetric(metric);
    }

    private Sample getSample(Types.Sample s) {
        Sample sample = new Sample();
        double v = s.getValue();
        if (isNaN(v)) {
            LOGGER.debug("NaN value in sample. Ignoring");
            return null;
        }
        sample.setValue(v);
        sample.setTimestamp(s.getTimestamp());
        return sample;
    }

    @Override
    public boolean processPrometheusMetricsAsync(Object obj, Consumer<List<IngesterMetricData>> stageOneDataConsumer) {
        final List<Types.TimeSeries> timeSeriesList = ((Remote.WriteRequest) metricData).getTimeseriesList();
        final List<IngesterMetricData> s1DataList = unmodifiableList(timeSeriesList.stream().map(ts -> new IngesterMetricData(ts)).collect(toList()));
        buildMetricsFromTimeSeries(s1DataList);
        return true;
    }

    @Override
    public boolean processPrometheusMetric(final Object metricData) {
        final String query = (String) metricData;

        // Process the time series and generate metrics
        List<IngesterMetricData> metrics = new ArrayList<>();
        for(Types.TimeSeries ts : ((Remote.WriteRequest) metricData).getTimeseriesList()) {
            IngesterMetricData ingesterMetricData = new IngesterMetricData();
            ingesterMetricData.setTs(ts);
            ingesterMetricData.setLabels(Types.Label::new);
            ingesterMetricData.setSample(getSample(ts.getSamples().iterator().next()));

            metrics.add(ingesterMetricData);
        }

        // Enrich the metrics and return them
        buildMetricsFromTimeSeries(metrics);

        return true;
    }
}
```

### Notes

- The `isAsyncSupported` method is currently returning false, indicating that asynchronous processing is not supported.
- The `getParallelThreadExecutor()` method provides a way to manage parallel thread execution for the metric enrichment process.
- The `addMetricToS1Data`, `getSample`, and `processPrometheusMetricsAsync` methods are part of the class implementation but are currently commented out. They should be filled with actual logic based on your requirements.
- The `buildMetricsFromTimeSeries` method is responsible for constructing metrics from time series data.

### Example

Here's a simplified example illustrating how to process metric data and asynchronously handle it:

```java
public class Main {
    public static void main(String[] args) throws Exception {
        List<IngesterMetricData> metrics = PrometheusMetricDataHandler.getInstance().processMetric(null);
        for (IngesterMetricData metric : metrics) {
            System.out.println(metric.getMetric().getPayLoad());
        }
    }
}
```

This example assumes that you have some kind of `ingesterMetricsProcessor` class to handle the actual logic and that `Remote.WriteRequest` is a type representing the metric data retrieved from Prometheus.