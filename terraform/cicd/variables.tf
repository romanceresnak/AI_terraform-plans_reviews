variable "aws_region" {
  description = "The AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "The name of the project"
  type        = string
  default     = "ai-tf-reviewer"
}

variable "repository_name" {
  description = "The name of the CodeCommit repository"
  type        = string
  default     = "terraform-infra"
}
