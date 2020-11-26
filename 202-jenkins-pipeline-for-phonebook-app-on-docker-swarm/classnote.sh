Project-202: Docker Swarm Deployment of Phonebook Application (Python Flask) with
- Infrastructure
    - Public Repository on Github (Codebase, Versionig System)
    - Docker Swarm as Orchestrator
        - 3 Manager
        - 2 Worker
    - Image Repository (AWS ECR)
    - Should be able to
        - Every EC2 is able to talk each other (EC2 Connect CLI, IAM Policy)
        - Grand Master can pull image from ECR and push image to AWS ECR (ECR credential helper, reach ECR with cli command)
        - Other instances (managers and workers) can pull image from (ECR credential helper)
        - Mangers and Workers can pull image from AWS ECR. (ECR credential helper)
- Application Deployement
    - Dockerfile
    - docker-compose.yml (Web server and Mysql)

# https://hub.docker.com/_/mysql
# docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html
# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html
# https://docs.docker.com/engine/swarm/swarm-tutorial/
# pip install ec2instanceconnectcli
# https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html
# https://aws.amazon.com/blogs/compute/authenticating-amazon-ecr-repositories-for-docker-cli-with-credential-helper/
# https://github.com/awslabs/amazon-ecr-credential-helper
# mssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -r us-east-1 <worker-id> or <master-id>
# 

Jenkins server should be capable of:
    - create ECR Repository
    - build docker image 
    - push Docker image to ECR repository 
    - create infrastructure for Athe Application
    - Deploy the application

# <EC@ instance Public IPv4 address>:8080//env-vars.html/ (e.g. 54.165.185.41:8080/env-vars.html/)
# aws ec2 describe-instances --region us-east-1 --instance-ids i-065b7bdaa242205eb --query 'Reservations[*].Instances[*].[PublicIpAddress]' --output text
# 
