# cognizance-demo

Requires kubernetes cluster to be pre-setup and kubeconfig populated with cluster information.

Navigate to the app/ directory and build and tag the Docker image in this repository using the command `docker build . -t public.ecr.aws/m5k5k5p2/python-crypto`

Authenticate with AWS ECR using the command `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 962331039642.dkr.ecr.region.amazonaws.com`
