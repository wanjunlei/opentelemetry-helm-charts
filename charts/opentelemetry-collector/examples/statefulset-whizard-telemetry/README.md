```shell
# Go to the charts/opentelemetry-collector directory
cd ..
helm upgrade --install --force -n opentelemetry --create-namespace -f examples/statefulset-whizard-telemetry/values.yaml opentelemetry-collector-contrib ./
```