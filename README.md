# cognizance-demo

Requires kubernetes cluster to be pre-setup and kubeconfig populated with cluster information.

Navigate to the app/ directory and build and tag the Docker image in this repository using the command `docker buildx build --platform=linux/amd64 --tag python-crypto . --load` I am using the buildx command since I'm building on an M1 Mac.

Authenticate with AWS ECR using the command `aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/m5k5k5p2`

Tag the image with the command `docker tag python-crypto:latest public.ecr.aws/m5k5k5p2/python-crypto:latest`

Push the image to ECR with the command `docker push public.ecr.aws/m5k5k5p2/python-crypto:latest`

Deploy the application with the manifests in manifests/ `kubectl apply -f service.yaml -f deployment.yaml`
