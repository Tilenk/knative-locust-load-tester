A tool used for load testing HTTP API services.
Used for testing Knative service running autoscaler-go image provided here:
https://knative.dev/docs/serving/autoscaling/autoscale-go/

## How to run
1. Create a cluster with at least 4vCPU and 4GB of memory
2. Install `skaffold`
3. In root directory run `skaffold dev --port-forward`
4. Open `localhost:8089` in your browser

## Increase the throughput
In `k8s/deployment-worker.yaml` increase the number of replicas.

## Change the target
In `k8s/deployment-master.yaml` change the `TARGET_HOST` env value to your hostname.