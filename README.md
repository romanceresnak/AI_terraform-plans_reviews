# AI-Powered Terraform Plan Review

🤖 Automated Terraform security review using AWS Bedrock and Claude AI

## Overview

This project implements an automated CI/CD pipeline that uses artificial intelligence to review Terraform plans before deployment. It analyzes infrastructure changes for security vulnerabilities, cost anomalies, and compliance with best practices.

## Features

- ✅ **Automated Security Analysis**: Every Terraform plan reviewed by Claude AI
- ✅ **Real-time Feedback**: Instant review results in CI/CD pipeline
- ✅ **Cost Optimization**: Detects expensive configurations and cost anomalies
- ✅ **Compliance Checking**: Validates tagging, naming, and organizational standards
- ✅ **Deployment Blocking**: Prevents insecure infrastructure from reaching production
- ✅ **Educational**: Developers learn security best practices from AI feedback

## Architecture

```
Developer → CodeCommit → CodePipeline → CodeBuild → Terraform Plan → AI Analysis (Claude) → APPROVED/REJECTED
```

## Technology Stack

- **AWS CodeCommit**: Git repository
- **AWS CodePipeline**: CI/CD orchestration
- **AWS CodeBuild**: Build environment
- **AWS Bedrock**: Managed AI service
- **Claude Sonnet 4.5**: AI model from Anthropic
- **Terraform**: Infrastructure as Code
- **Python 3.11**: AI reviewer script

## Quick Start

### Prerequisites

- AWS Account with Bedrock access
- Claude Sonnet 4.5 model enabled in Bedrock
- Terraform >= 1.14
- Python >= 3.11

### Installation

1. Deploy CI/CD infrastructure:
```bash
cd terraform/cicd
terraform init
terraform apply
```

2. Push your code to CodeCommit:
```bash
git remote add origin <codecommit-url>
git push origin main
```

3. Watch the automated review in action!

## Project Structure

```
.
├── terraform/
│   ├── cicd/              # CI/CD infrastructure (CodePipeline, CodeBuild)
│   │   ├── main.tf
│   │   ├── iam.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── infrastructure/    # Example infrastructure to review
│       └── main.tf
├── scripts/
│   ├── ai_reviewer.py     # AI review script
│   └── requirements.txt
├── buildspec.yml          # CodeBuild configuration
├── architecture-diagram.md
├── article.md             # Detailed technical article
└── README.md
```

## How It Works

1. **Developer pushes code** to main branch
2. **CodePipeline triggers** automatically
3. **CodeBuild executes**:
   - Installs Terraform and Python dependencies
   - Runs `terraform init`
   - Runs `terraform plan -out=tfplan`
   - Exports plan to JSON format
   - Executes AI reviewer script
4. **Python script** sends plan to AWS Bedrock
5. **Claude AI analyzes** for:
   - Security vulnerabilities (encryption, public access, IAM)
   - Cost anomalies (expensive resources, deletions)
   - Best practices (tagging, naming, compliance)
6. **Returns decision**: APPROVED ✅ or REJECTED ❌
7. **Build succeeds or fails** based on AI decision

## Example Output

### REJECTED (Security Issues)
```
DECISION: REJECTED

REASON: Critical security vulnerabilities:
1. Missing encryption on S3 bucket
2. No public access block configured
3. Missing required tags
4. No access logging enabled

SUGGESTIONS:
- Add aws_s3_bucket_server_side_encryption_configuration
- Add aws_s3_bucket_public_access_block
- Add required tags (Environment, Owner, Project)
- Enable access logging
```

### APPROVED (Secure Configuration)
```
DECISION: APPROVED

REASON: Excellent security practices:
✅ Server-side encryption enabled (AES256)
✅ Public access completely blocked
✅ Comprehensive tagging for governance
✅ Access logging configured
✅ Versioning enabled

SUGGESTIONS:
- Consider KMS encryption for enhanced security
- Implement lifecycle policies for cost optimization
```

## Cost

- **AWS Bedrock (Claude Sonnet 4.5)**: ~$0.03 per review
- **AWS CodeBuild**: ~$0.025 per build (5 minutes)
- **Total**: ~$5.50/month for 100 deployments

**ROI**: Positive after catching just ONE security issue

## Configuration

### Enable Bedrock Model Access
1. AWS Console → Bedrock → Model access
2. Enable "Claude Sonnet 4.5"
3. Confirm access

### Customize AI Reviewer

Edit `scripts/ai_reviewer.py` to customize:
- Security rules
- Compliance requirements
- Cost thresholds
- Custom prompts

## Best Practices

The AI checks for:

### Security
- Encryption at rest and in transit
- Public access configurations
- IAM policies and roles
- Security group rules
- Network isolation
- Secrets management

### Cost Optimization
- Expensive instance types
- Unnecessary resource deletions
- Storage class optimization
- Lifecycle policies

### Compliance
- Required tags (Environment, Owner, Project, CostCenter)
- Naming conventions
- Resource organization
- Backup strategies
- High availability setup

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Author

Roman Ceresňák
- AWS Community Builder
- [LinkedIn](https://www.linkedin.com/in/roman-ceresnak/)

## Acknowledgments

- AWS Bedrock team for managed AI services
- Anthropic for Claude AI model
- HashiCorp for Terraform

---

**Tags:** #AWS #Bedrock #Claude #Terraform #DevOps #AI #Security #IaC #Automation #CloudSecurity
