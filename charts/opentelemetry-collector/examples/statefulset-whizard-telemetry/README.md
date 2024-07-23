## Using OpenTelemetry for observability of AI applications

### Launch a LLM service locally with Ollama
- Following [the instrunctions](https://github.com/ollama/ollama) to install Ollama
- Launch a LLM service like Llama3 locally with `ollama run llama3`

### Install OpenTelemetry Collector in a K8s cluster
```shell
# Go to the charts/opentelemetry-collector directory
cd ..
helm upgrade --install --force -n opentelemetry --create-namespace -f examples/statefulset-whizard-telemetry/values.yaml opentelemetry-collector-contrib ./
```
Suppose your OpenTelemetry Collector expose its service at `http://172.31.18.2:30318`

### Config OpenLIT to send observability data to OpenTelemetry Collector in AI applications

You can add code below to your AI applications, refer to [this example](./ollama-api.py) for more details of an AI application.

```python
import openlit
openlit.init(otlp_endpoint="http://172.31.18.2:30318")
```

### Run the AI application locally and observe metrics & tracing data from OpenTelemetry Collector

Run the sample AI Applications like this:
```shell
python3 ./ollama-api.py
```

Take a look at the AI application's metrics & tracing data from OpenTelemetry Collector: 
```shell
kubectl -n opentelemetry logs opentelemetry-collector-contrib-0 opentelemetry-collector -f
```

You'll see something like this:
```shell
2024-07-23T09:34:06.301Z	info	MetricsExporter	{"kind": "exporter", "data_type": "metrics", "name": "debug", "resource metrics": 1, "metrics": 5, "data points": 5}
2024-07-23T09:34:06.301Z	info	ResourceMetrics #0
Resource SchemaURL:
Resource attributes:
     -> service.name: Str(default)
     -> deployment.environment: Str(default)
     -> telemetry.sdk.name: Str(openlit)
ScopeMetrics #0
ScopeMetrics SchemaURL:
InstrumentationScope openlit.otel.metrics 0.1.0
Metric #0
Descriptor:
     -> Name: gen_ai.total.requests
     -> Description: Number of requests to GenAI
     -> Unit: 1
     -> DataType: Sum
     -> IsMonotonic: true
     -> AggregationTemporality: Cumulative
NumberDataPoints #0
Data point attributes:
     -> telemetry.sdk.name: Str(openlit)
     -> gen_ai.application_name: Str(default)
     -> gen_ai.system: Str(ollama)
     -> gen_ai.environment: Str(default)
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.request.model: Str(llama3)
StartTimestamp: 2024-07-23 09:34:05.946654 +0000 UTC
Timestamp: 2024-07-23 09:34:05.9468 +0000 UTC
Value: 1
Metric #1
Descriptor:
     -> Name: gen_ai.usage.total_tokens
     -> Description: Number of total tokens processed.
     -> Unit: 1
     -> DataType: Sum
     -> IsMonotonic: true
     -> AggregationTemporality: Cumulative
NumberDataPoints #0
Data point attributes:
     -> telemetry.sdk.name: Str(openlit)
     -> gen_ai.application_name: Str(default)
     -> gen_ai.system: Str(ollama)
     -> gen_ai.environment: Str(default)
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.request.model: Str(llama3)
StartTimestamp: 2024-07-23 09:34:05.946673 +0000 UTC
Timestamp: 2024-07-23 09:34:05.9468 +0000 UTC
Value: 376
Metric #2
Descriptor:
     -> Name: gen_ai.usage.completion_tokens
     -> Description: Number of completion tokens processed.
     -> Unit: 1
     -> DataType: Sum
     -> IsMonotonic: true
     -> AggregationTemporality: Cumulative
NumberDataPoints #0
Data point attributes:
     -> telemetry.sdk.name: Str(openlit)
     -> gen_ai.application_name: Str(default)
     -> gen_ai.system: Str(ollama)
     -> gen_ai.environment: Str(default)
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.request.model: Str(llama3)
StartTimestamp: 2024-07-23 09:34:05.946679 +0000 UTC
Timestamp: 2024-07-23 09:34:05.9468 +0000 UTC
Value: 368
Metric #3
Descriptor:
     -> Name: gen_ai.usage.prompt_tokens
     -> Description: Number of prompt tokens processed.
     -> Unit: 1
     -> DataType: Sum
     -> IsMonotonic: true
     -> AggregationTemporality: Cumulative
NumberDataPoints #0
Data point attributes:
     -> telemetry.sdk.name: Str(openlit)
     -> gen_ai.application_name: Str(default)
     -> gen_ai.system: Str(ollama)
     -> gen_ai.environment: Str(default)
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.request.model: Str(llama3)
StartTimestamp: 2024-07-23 09:34:05.946684 +0000 UTC
Timestamp: 2024-07-23 09:34:05.9468 +0000 UTC
Value: 8
Metric #4
Descriptor:
     -> Name: gen_ai.usage.cost
     -> Description: The distribution of GenAI request costs.
     -> Unit: USD
     -> DataType: Histogram
     -> AggregationTemporality: Cumulative
HistogramDataPoints #0
Data point attributes:
     -> telemetry.sdk.name: Str(openlit)
     -> gen_ai.application_name: Str(default)
     -> gen_ai.system: Str(ollama)
     -> gen_ai.environment: Str(default)
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.request.model: Str(llama3)
StartTimestamp: 2024-07-23 09:34:05.946689 +0000 UTC
Timestamp: 2024-07-23 09:34:05.9468 +0000 UTC
Count: 1
Sum: 0.000000
Min: 0.000000
Max: 0.000000
ExplicitBounds #0: 0.000000
ExplicitBounds #1: 5.000000
ExplicitBounds #2: 10.000000
ExplicitBounds #3: 25.000000
ExplicitBounds #4: 50.000000
ExplicitBounds #5: 75.000000
ExplicitBounds #6: 100.000000
ExplicitBounds #7: 250.000000
ExplicitBounds #8: 500.000000
ExplicitBounds #9: 750.000000
ExplicitBounds #10: 1000.000000
ExplicitBounds #11: 2500.000000
ExplicitBounds #12: 5000.000000
ExplicitBounds #13: 7500.000000
ExplicitBounds #14: 10000.000000
Buckets #0, Count: 1
Buckets #1, Count: 0
Buckets #2, Count: 0
Buckets #3, Count: 0
Buckets #4, Count: 0
Buckets #5, Count: 0
Buckets #6, Count: 0
Buckets #7, Count: 0
Buckets #8, Count: 0
Buckets #9, Count: 0
Buckets #10, Count: 0
Buckets #11, Count: 0
Buckets #12, Count: 0
Buckets #13, Count: 0
Buckets #14, Count: 0
Buckets #15, Count: 0
	{"kind": "exporter", "data_type": "metrics", "name": "debug"}
2024-07-23T09:34:06.439Z	info	TracesExporter	{"kind": "exporter", "data_type": "traces", "name": "debug", "resource spans": 1, "spans": 1}
2024-07-23T09:34:06.440Z	info	ResourceSpans #0
Resource SchemaURL:
Resource attributes:
     -> service.name: Str(default)
     -> deployment.environment: Str(default)
     -> telemetry.sdk.name: Str(openlit)
ScopeSpans #0
ScopeSpans SchemaURL:
InstrumentationScope openlit.otel.tracing
Span #0
    Trace ID       : fd068f02892b30cc90bef2be6faf5f62
    Parent ID      :
    ID             : e303e7f29c61228c
    Name           : ollama.chat
    Kind           : Client
    Start time     : 2024-07-23 09:33:58.269293 +0000 UTC
    End time       : 2024-07-23 09:34:05.946708 +0000 UTC
    Status code    : Ok
    Status message :
Attributes:
     -> telemetry.sdk.name: Str(openlit)
     -> gen_ai.system: Str(ollama)
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.endpoint: Str(ollama.chat)
     -> gen_ai.environment: Str(default)
     -> gen_ai.application_name: Str(default)
     -> gen_ai.request.model: Str(llama3)
     -> gen_ai.request.is_stream: Bool(true)
     -> gen_ai.usage.prompt_tokens: Int(8)
     -> gen_ai.usage.completion_tokens: Int(368)
     -> gen_ai.usage.total_tokens: Int(376)
     -> gen_ai.usage.cost: Int(0)
     -> gen_ai.prompt: Str(user: Why is the sky blue?)
     -> gen_ai.completion: Str(The sky appears blue to our eyes because of a phenomenon called scattering, which occurs when sunlight interacts with the tiny molecules of gases in the Earth's atmosphere.

Here's what happens:

1. Sunlight enters the Earth's atmosphere and is made up of all the colors of the visible spectrum (red, orange, yellow, green, blue, indigo, and violet).
2. When this light encounters the small molecules of gases like nitrogen (N2) and oxygen (O2), it scatters in all directions.
3. The shorter wavelengths of light, such as blue and violet, are scattered more than the longer wavelengths, like red and orange. This is because the smaller molecules are more effective at scattering shorter wavelengths.
4. As a result, the blue light is distributed evenly throughout the atmosphere, reaching our eyes from all parts of the sky.
5. The other colors of light, particularly red and orange, continue to travel in a more direct path to our eyes, reaching us from specific directions (e.g., the sun's position).

The combined effect of this scattering and absorption of light is what makes the sky appear blue during the daytime. The color can vary depending on factors like:

* Atmospheric conditions: Dust, pollution, or water vapor can scatter light in different ways, changing the apparent color of the sky.
* Time of day: As the sun rises or sets, the angle of incidence changes, and the scattering patterns alter the perceived color of the sky.
* Altitude and atmospheric layers: The higher you go, the more the atmosphere scatters shorter wavelengths, making the sky appear even bluer.

So, to summarize, the sky appears blue because the tiny molecules in the Earth's atmosphere scatter shorter wavelengths of sunlight, like blue and violet, in all directions, while longer wavelengths continue on their original paths.)
	{"kind": "exporter", "data_type": "traces", "name": "debug"}
```
