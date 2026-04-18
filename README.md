# AI Terraform Plan Reviewer on AWS

This project implements an automated CI/CD pipeline that uses **Amazon Bedrock (Claude 3)** to review Terraform plans before they are deployed.

## Architecture
1. **Source**: AWS CodeCommit repository holds the Terraform code.
2. **CI/CD**: AWS CodePipeline orchestrates the process.
3. **Plan & Review**: AWS CodeBuild runs `terraform plan`, converts it to JSON, and executes a Python script.
4. **AI Review**: The Python script sends the plan to **Amazon Bedrock** for analysis.
5. **Enforcement**: If the AI rejects the plan (e.g., due to security risks), the pipeline fails, blocking deployment.

## Project Structure
- `terraform/cicd`: Infrastructure for the pipeline (CodePipeline, CodeBuild, IAM).
- `terraform/infrastructure`: Sample infrastructure to be reviewed.
- `scripts/ai_reviewer.py`: The logic that interfaces with Bedrock.
- `buildspec.yml`: Build instructions for CodeBuild.

## How to Deploy
1. **Prerequisites**:
   - AWS CLI configured.
   - Terraform installed.
   - **Amazon Bedrock access**: Ensure that "Anthropic Claude 3 Sonnet" is enabled in your AWS account (Bedrock -> Model access).

2. **Deploy the Pipeline**:
   ```bash
   cd terraform/cicd
   terraform init
   terraform apply
   ```

3. **Push Code to CodeCommit**:
   - The `terraform apply` command will output the CodeCommit clone URL.
   - Initialize a git repo in this project root, add the remote, and push:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <CLONE_URL>
   git push origin main
   ```

4. **Monitor the Pipeline**:
   - Go to the AWS CodePipeline console to see the progress.
   - Check the CodeBuild logs to see the AI's detailed review.

## Example AI Review Output
```text
DECISION: REJECTED
REASON: The plan includes an S3 bucket with public access enabled and no server-side encryption defined.
SUGGESTIONS: Enable 'block_public_access' and add an 'aws_s3_bucket_server_side_encryption_configuration' resource.
```
