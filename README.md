# Demo project for S3 Events Processing

This project is a demo for how to create a serverless application that can handle specific AWS S3 events

## Local Setup

1. Create virtual environment

```console
lambdas/events_processor$ python -m venv .venv
lambdas/events_processor$ source .venv/bin/activate
```

2. Install dependencies

   2.1. For Development (VSCode)

   ```console
   (.venv) lambdas/events_processor/src$ pip install cfn-lint pydot
   ```

   2.2. For Running and Testing

   ```console
   (.venv) lambdas/events_processor/src$ pip install -r requirements.txt
   ```

3. Local Testing

   3.1. Optional: Generate test events

   ```console
   lambdas/events_processor$ sam local generate-event s3 put --bucket demo-bucket --key PutEvents/demo-putted-file.txt > src/tests/events/put.json
   ```

   3.2. Unit and Integration Tests

   ```console
   lambdas/events_processor/src/tests$ pytest
   ```

   3.3. SAM Test

   ```console
   $ sam build
   $ sam local invoke --event lambdas/events_processor/src/tests/events/put.json EventsProcessorFunction
   ```

4. Build, Test and Deploy (Manually)

   4.1. For the first time

   ```console
   scripts$ sam deploy --guided
   ```

   4.2. From the second time on

   ```console
   scripts$ . deploy.sh <dev|prod>
   ```

5. Build and Deploy (Automated)
