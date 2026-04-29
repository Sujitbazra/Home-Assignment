PART 1: INFRASTRUCTURE ANALYSIS

Q1. List all security issues in the code (minimum 6)
  Ans: Security Issues in the given Infrastructure Archicture. 
  1. cidr_blocks = ["0.0.0.0/0"] i.e Anyone can attempt SSH
  2. HTTP (port 80) is open to the entire internet without any protection like WAF
  3. No security group is explicitly attached to EC2 instances.
  4. Database credentials are hardcoded in Terraform (username and password).
  5. No encryption enabled for RDS storage.
  6. No IAM roles are assigned to EC2 instances

Q2. List all architectural problems (minimum 5)
  Ans: Architectural problems in the given scenario is.
  1. No private subnets; all resources are deployed in public subnets.
  2. No NAT Gateway for private instances to access the internet.
  3. No load balancer for distributing traffic across EC2 instances.
  4. No Multi-AZ deployment for RDS exposing single point of failure.
  5. No backup strategy for database (backup retention = 0).

Q3. Explain what changes you would make for production-readiness. 
  Ans: This architecture needs following changes to make production-readiness
  1. Add Application Load Balancer (ALB) in front of EC2 instances.
  2. Use Auto Scaling Group for EC2 instances.
  3. Attach IAM roles to EC2 instances.
  4. Introduce public and private subnEnable encryption for RDS and S3.ets across multiple AZs.
  5. Enable encryption for RDS and S3.
  6. Block public access to S3 bucket.
  7. Add AWS WAF for security.
  8. Enable CloudWatch logging and monitoring.